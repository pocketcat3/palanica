from winreg import *
key_my = OpenKey(HKEY_CURRENT_USER, 
                 r'SOFTWARE\Microsoft\Windows\CurrentVersion\Run', 
                 0, KEY_ALL_ACCESS)

SetValueEx(key_my, 'script', 0, REG_SZ, r'main.py')
CloseKey(key_my)