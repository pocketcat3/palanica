import os
import time
from playsound import playsound
import keyboard

path = 'C:\\Users\\pocketcat\\Desktop\\bebrik progs\\winda'

# playsound("music.mp3")

# while True:
#     os.system("palanica.jpg")
#     keyboard.press_and_release('f11')
#     time.sleep(0.5)

keyboard.add_hotkey('esc', lambda: os.system("palanica.jpg"), time.sleep(0.1),keyboard.press_and_release('f11'))
keyboard.wait()