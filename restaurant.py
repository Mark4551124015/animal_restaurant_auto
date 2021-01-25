import time
import random
import pyautogui
import base
import event
import move
x ,y, r, b = base.first()


orderPositions = [
  [140, 400],
  [240, 400],
  [340, 400],
  [140, 530],
  [240, 530],
  [340, 530]
]

driedFishPosition = [
  [200, 400],
  [300, 400],
  [400, 400],
  [200, 530],
  [300, 530],
  [400, 530],
  [80, 370],
  [200, 720],
  [220, 650],
  [170, 610],
  [220, 620],
  [220, 620]
]


foxPosition = [130, 370]
publicCityClickPosition=[412,788]



# 点菜
def orderDishes():
  time.sleep(random.randint(0, 3))
  for items in orderPositions:
    move.click(items[0], items[1])

# 拾取鱼干
def pickUpDriedFish():
  for items in driedFishPosition:
    move.click(items[0], items[1])

# 去nm的臭鼬
def fuckFox():
  move.click(foxPosition[0], foxPosition[1])
  for i in range(20):
    pyautogui.click()

# 宣传按钮
def locateToPublicCityClick(publicCityClickCount):
  move.click(publicCityClickPosition[0], publicCityClickPosition[1])
  for i in range(random.randint(1, publicCityClickCount)):
      pyautogui.click()
      time.sleep(0.1)
  check_event()


#检查特殊任务
def check_event():
  event.fuck_fine()
  base.get_screen_img()
  bird_exist, bird_x, bird_y = base.scan('bird')
  tv_exist, tv_x, tv_y = base.scan('tv')
  witch_exist, witch_x, witch_y = base.scan('witch')
  witch_exist2, witch_x, witch_y = base.scan('witch2')
  rat_exist, rat_x, rat_y = base.scan('rat')
  crow_exist, crow_x, crow_y = base.scan('crow')
  # print("witch" + str(witch_exist+witch_exist2))
  # print("bird" + str(bird_exist))
  # print("tv" + str(tv_exist))
  # print("rat" + str(rat_exist))
  # print("crow" + str(crow_exist))
  if witch_exist+witch_exist2 != 0:
    print("有魔法师，看广告")
    event.fuck_witch()
  elif bird_exist == 1:
    print("有鸟，放歌")
    event.fuck_bird()
  elif tv_exist == 1:
    print("有电视，看广告")
    event.fuck_tv()
  elif rat_exist == 1:
    print("有老鼠，玩他")
    event.fuck_rat()
  elif crow_exist == 1:
    print("神秘商人，干他")
    event.fuck_crow()
