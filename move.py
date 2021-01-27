import pyautogui
import base
import time

x ,y, r, b = base.first()

def toLeft():
  click(25, 442)
  time.sleep(0.5)

def toRight():
  click(419, 442)
  time.sleep(0.5)

def toUp():
  click(150, 207)
  time.sleep(0.5)

def toDown():
  click(166, 800)
  time.sleep(0.5)

def click(a,b):
  pyautogui.moveTo(a+x,b+y,0.1)
  pyautogui.click()
