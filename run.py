import keyboard
import multiprocessing
import random
import time
import restaurant
import garden
import kitchen
import move
import base
import os
import sys 


def run(count = 50000, publicCityClickCount = 64, mouseMoveSpeed = 0.1):
  print(' ')
  print('开始咯...，按下空格键暂停')
  print(' ')
  #归位
  move.toLeft()
  move.toLeft()
  move.toLeft()
  move.toLeft()
  move.toRight()
  move.toRight()
  
  #开始循环
  for i in range(count):
    restaurant.locateToPublicCityClick(publicCityClickCount, mouseMoveSpeed)
    restaurant.orderDishes(mouseMoveSpeed)
    if(i + 1) % 3 == 0:
      restaurant.pickUpDriedFish(mouseMoveSpeed)
      move.toRight()
      time.sleep(0.2)
      kitchen.pickUpDriedFish(mouseMoveSpeed=mouseMoveSpeed)
      move.toLeft()
      move.toLeft()
      time.sleep(0.2)
      garden.pickUpDriedFish(mouseMoveSpeed=mouseMoveSpeed)
      move.toRight()
#      restaurant.fuckFox(mouseMoveSpeed)  有员工，暂时去除
    if(i + 1) % 10 == 0:
      time.sleep(random.randint(5, 30))
      move.toLeft()
      garden.sowFlower(mouseMoveSpeed)
      move.toRight()


def stop():
        keyboard.wait('p')
        os.system("pause")

check=2
if __name__=='__main__':
  while check!=1:
      print('按下空格键，开始/继续') 
      keyboard.wait('space')
      p1 = multiprocessing.Process(target=run,args=())
      p1.start()
      keyboard.wait('space')
      print(' ')
      print('已暂停')
      p1.terminate()
      print(' ')
      
