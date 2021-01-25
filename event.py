import base
import pyautogui
import time

x ,y, r, b = base.first()
no = [135+x,725+y]
yes = [310+x,725+y]
salesmanPosition = [149+x,728+y]

def fuck_fox():
    time.sleep(2)
    i = 0
    while i < 10:
        i = i + 1
        pyautogui.moveTo(130+x,365+y,0.3)
        pyautogui.click()
        time.sleep(0.1)

def fuck_bird():
    pyautogui.moveTo(340 + x, 260 + y, 0.3)
    i=0
    while i < 15:
        i=i+1
        pyautogui.click()
        time.sleep(0.1)

def fuck_tv():
    o, tv_x, tv_y = base.scan('tv')
    tv_x = tv_y + x
    tv_y = tv_y + y
    pyautogui.moveTo(tv_x, tv_y,0.3)
    pyautogui.click()
    time.sleep(0.5)
    adv()

def fuck_panda():
    i = 0
    while i < 10:
        i = i + 1
        o, panda_x, panda_y = base.scan('panda')
        panda_x=panda_x+x
        panda_y=panda_y+y
        pyautogui.moveTo(panda_x,panda_y,0.3)
        pyautogui.click()
        pyautogui.click()
        time.sleep(0.1)

def fuck_fine():
    pyautogui.moveTo(214+x, 545+y,0.3)
    pyautogui.click()

def fuck_crow():
    pyautogui.moveTo(388 + x, 266 + y, 0.3)
    time.sleep(0.1)
    pyautogui.click()
    time.sleep(0.1)
    pyautogui.moveTo(no[0], no[1],0.3)
    pyautogui.click()
    time.sleep(0.1)
    pyautogui.click()


def fuck_rat():
    pyautogui.moveTo(169+x, 349+y, 0.3)
    pyautogui.click()
    time.sleep(0.2)
    pyautogui.click()
    time.sleep(0.2)
    pyautogui.click()
    time.sleep(0.2)
    pyautogui.moveTo(yes[0], yes[1], 0.3)
    time.sleep(0.2)
    pyautogui.click()
    time.sleep(0.2)
    pyautogui.moveTo(120+x,300+y,0.3)

def fuck_witch():
    pyautogui.moveTo(396 + x, 271 + y, 0.3)
    pyautogui.click()
    adv()

def adv():
  pyautogui.moveTo(yes[0], yes[1], 0.3)
  pyautogui.click()
  time.sleep(0.1)
  pyautogui.moveTo(x+370, y+75, 0.3)
  time.sleep(1)
  pyautogui.click()
  time.sleep(31)
  pyautogui.moveTo(x+410, y+75, 0.3)
  pyautogui.click()
  time.sleep(0.5)
  pyautogui.click()
  time.sleep(0.5)
  pyautogui.click()






