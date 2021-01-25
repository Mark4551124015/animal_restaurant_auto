import time
import random
import pyautogui
import base
import move

x ,y, r, b = base.first()

driedFishPosition = [
  [50, 300],
  [380, 340],
  [200, 650],
  [145, 400],
  [85, 400],
  [340, 510],
]

def pickUpDriedFish():
  for items in driedFishPosition:
    move.click(items[0], items[1])