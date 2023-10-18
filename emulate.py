import pyautogui as pag
import time

time.sleep(2)

for i in range(17):
    pag.press("down")
    pag.press("end")
    pag.press("left")
    pag.keyDown("shift")
    pag.press("home")
    pag.keyUp("shift")
    pag.press("[")
    pag.press("end")