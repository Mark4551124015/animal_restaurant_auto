import pyautogui
import time
import base

x ,y, r, b = base.first()



driedFishPosition = [
  [50, 270],
  [305, 233]
]


potPosition = [
  [136, 411],
  [226, 546],
  [311, 405],
  [226, 546],
  [135, 525],
  [226, 546],
  [311, 525],
  [226, 546]
]


def pickUpDriedFish(mouseMoveSpeed):
  for items in driedFishPosition:
    move.click(items[0], items[1])


def sowFlower(mouseMoveSpeed):
  for items in potPosition:
    move.click(items[0], items[1])
    time.sleep(0.5)
    pyautogui.click()