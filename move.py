import pyautogui
import base

x ,y, r, b = base.first()

def toLeft():
  click(25, 442)

def toRight():
  click(419, 442)

def toUp():
  click(150, 207)

def toDown():
  click(166, 800)

def click(a,b):
  pyautogui.moveTo(a+x,b+y,0.1)
  pyautogui.click()
