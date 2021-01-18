import keyboard
import multiprocessing
import random
import time
import restaurant

def run(count = 20, mouseMoveSpeed = 0.1):
  print('开始咯...')
  for i in range(count):
    restaurant.adv(mouseMoveSpeed)
    for n in range(4):
        restaurant.orderDishes(mouseMoveSpeed)
        time.sleep(10)
    if(i + 1) % 3 == 0:
        restaurant.pickUpDriedFish(mouseMoveSpeed)
        restaurant.fuckFox(mouseMoveSpeed)

if __name__=='__main__':
  p1 = multiprocessing.Process(target=run,args=())
  p1.start() 
  print('按下空格键退出程序') 
  keyboard.wait('space')
  p1.terminate()