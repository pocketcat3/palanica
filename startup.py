from winreg import *
# Путь в реестре
key_my = OpenKey(HKEY_CURRENT_USER, 
                 r'SOFTWARE\Microsoft\Windows\CurrentVersion\Run', 
                 0, KEY_ALL_ACCESS)

# Установить скрипт в автозагрузку
SetValueEx(key_my, 'script', 0, REG_SZ, r'C:\Users\pocketcat\Desktop\bebrik progs\test.py')
# Закрыть реестр
CloseKey(key_my)