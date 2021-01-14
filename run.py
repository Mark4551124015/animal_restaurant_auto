import keyboard
import multiprocessing
import random
import time
import restaurant
import base


def run(count = 20, mouseMoveSpeed = 0.1):
  print('开始咯...')
  for i in range(count):
    restaurant.adv(mouseMoveSpeed)
    for n in range(4):
        restaurant.orderDishes(mouseMoveSpeed)
        time.sleep(10)
        restaurant.pickUpDriedFish(mouseMoveSpeed)


nb=2
if __name__=='__main__':
  while nb!=1:
      print('按下空格键，开始/继续') 
      keyboard.wait('space')
      p1 = multiprocessing.Process(target=run,args=())
      p1.start()
      keyboard.wait('space')
      print(' ')
      print('已暂停')
      p1.terminate()
      print(' ')