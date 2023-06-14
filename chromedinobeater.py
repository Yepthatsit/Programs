import pyautogui
from PIL import Image, ImageGrab
import keyboard
import time
def duck():
    pyautogui.keyDown("down")
    pyautogui.sleep(0.5)
    pyautogui.keyUp("down")
    return
def jump():
    pyautogui.keyDown("up")
    return
def cactusdet(cos):
       #kaktus
       for i in range(705,773):
            for j in range(290,305):
                if cos[i,j] < 100:
                    jump()
                    return
def ptakdet(cos):#ptak       
       for i in range(705,755):
            for j in range(250,275):
                if cos[i,j] < 170:
                     duck()
                     return
                return
time.sleep(3)
while True:
    screen = ImageGrab.grab().convert("L")
    current = screen.load()
    ptakdet(current)
    cactusdet(current)
    #for i in range(705,755):
    #    for j in range(255,280):
    #         current[i,j] = 0
    #for i in range(705,780):
    #        for j in range(285,305):
    #            current[i,j] = 150
    #screen.show()
    #break
                 
 
 