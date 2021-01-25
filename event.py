import base
import pyautogui
import time
import move

x ,y, r, b = base.first()
no = [135,725]
yes = [310,725]
foxPosition = [130,365]
birdPosition = [340, 260]
tvPosition = [350,310]
crowPositon = [388,266]
ratPosition = [169, 349]
witchPosition = [396, 271]

def fuck_fox():
    time.sleep(2)
    i = 0
    move.click(foxPosition[0], foxPosition[1])
    while i < 10:
        i = i + 1
        pyautogui.click()
        time.sleep(0.1)

def fuck_bird():
    move.click(birdPosition[0],birdPosition[1])
    i=0
    while i < 20:
        i=i+1
        pyautogui.click()
        time.sleep(0.1)

def fuck_tv():
    move.click(tvPosition[0], tvPosition[1])
    time.sleep(0.5)
    adv()

def fuck_panda():
    i = 0
    while i < 10:
        i = i + 1
        o, panda_x, panda_y = base.scan('panda')
        panda_x=panda_x+x
        panda_y=panda_y+y
        move.click(panda_x,panda_y)
        time.sleep(0.1)

def fuck_fine():
    move.click(214, 545)
    time.sleep(0.1)
    move.click(340, 556)

def fuck_crow():
    move.click(crowPositon[0], crowPositon[1])
    time.sleep(0.1)
    move.click(no[0], no[1])
    pyautogui.click()
    time.sleep(0.1)
    pyautogui.click()


def fuck_rat():
    move.click(ratPosition[0], ratPosition[1])
    time.sleep(0.2)
    pyautogui.click()
    time.sleep(0.2)
    pyautogui.click()
    time.sleep(0.2)
    move.click(yes[0], yes[1])
    pyautogui.click()
    time.sleep(0.2)
    move.click(120,300)

def fuck_witch():
    move.click(witchPosition[0], witchPosition[1])
    adv()

def adv():
  move.click(yes[0], yes[1])
  time.sleep(0.1)
  pyautogui.moveTo(x+370, y+75, 0.3)
  time.sleep(1)
  pyautogui.click()
  time.sleep(31)
  move.click(410, 75)
  time.sleep(0.5)
  pyautogui.click()
  time.sleep(0.5)
  pyautogui.click()






