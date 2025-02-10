
import winreg

def remove_from_autostart():
    try:
        reg_path = r"Software\Microsoft\Windows\CurrentVersion\Run"
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, reg_path, 0, winreg.KEY_WRITE)
        winreg.DeleteValue(key, "minecraft.exe")
        winreg.CloseKey(key)
        print("Deleted from regedit.")
    except Exception as e:
        print(f"Error while deleting from regedit: {e}")


if __name__ == "__main__":
    remove_from_autostart()
