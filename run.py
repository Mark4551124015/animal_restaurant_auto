import keyboard
import multiprocessing
import random
import time
import restaurant
import garden
import kitchen
import move
import base
import event
import win32gui

witch_count=0
bird_count=0
tv_count=0
rat_count  = 0
crow_count = 0
times=0

def run(count = 50000, publicCityClickCount = 64):
  print('开始咯...')
  win32gui.SetForegroundWindow(win32gui.FindWindow(None, '动物餐厅'))
  for times in range(count):
    restaurant.locateToPublicCityClick(publicCityClickCount)
    restaurant.orderDishes()
    restaurant.pickUpDriedFish()
    if (times + 1) % 10 == 0:
      allfries()
      time.sleep(random.randint(5, 30))
    if (times + 1) % 51 == 0:
      flowers()



def allfries():
    move.toRight()
    time.sleep(0.2)
    kitchen.pickUpDriedFish()
    move.toLeft()
    move.toLeft()
    time.sleep(0.2)
    garden.pickUpDriedFish()
    move.toRight()
    time.sleep(1)

def flowers():
    time.sleep(random.randint(5, 30))
    move.toLeft()
    garden.sowFlower()
    move.toRight()



if __name__=='__main__':
  print('空格开始')
  keyboard.wait('space')
  p1 = multiprocessing.Process(target=run, args=())
  p1.start()
  print('按下空格键退出程序') 
  keyboard.wait('space')
  p1.terminate()
  print('本次结果')
  # print('老鼠' + str(rat_count) + '只')
  # print('歌手' + str(bird_count) + '只')
  # print('魔法师' + str(witch_count) + '只')
  # print('商人' + str(crow_count) + '只')
  # print('小电视' + str(tv_count) + '只')
  # print('循环'+str(times))
  keyboard.wait('space')


