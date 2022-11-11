import ctypes, os, sys

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if is_admin():
    answer = ctypes.windll.user32.MessageBoxW(0, "Are you sure you want to bluescreen your computer?", "Confirmation", 4)

    if answer == 6:
      os.system("taskkill /f /im svchost.exe")
    else: 
     print("pussy")
else:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
