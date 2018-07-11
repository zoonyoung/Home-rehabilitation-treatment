#grape!
#This game is rolling_dice
#If you win the game, you can read good words.
import random
import time
import cv2
import numpy as np
import turtle
from dice.dice_reader import dice_recognition
from dice.dice_generator import generate, dice
from dice.sayings import group

def rolling(cap):
  min = 1
  max = 6
  num = int(input(" : 몇번 던지시겠습니까?\n : "))
  ending=1
  for i in range(num):
    s_x=0
    s_y=0
    while ending == 1 :
      for i in range(num):
        randNum= random.randint(min,max)
        print("\nYour Turn!\n")
        x= dice_recognition(cap)
        s_x+=x
        print("")
        time.sleep(0.5)
        print("Ok. My Turn!")
        for k in range(5,0,-1):
          print("rolling the dice...\n wait...{}seconds plz".format(k))
          time.sleep(1)
        cv2.destroyAllWindows()                                   # since we exited the loop above, end the script.
        y=randNum
        s_y+=y
        generate(y,num,i)
        dice(y)
        print("This turn [You]: {}, [Me]: {}\nT o t a l [You]: {}, [Me]: {} ".format(x,y,s_x,s_y))
      l=group()
      if s_x==s_y:
        print('\n 게임 종료\n') #end game
        time.sleep(1)
        print("비겼어요!!") #draw
      elif s_x>s_y:
        print('\n 게임 종료\n') #end game
        time.sleep(1)
        print("축하합니다! 이기셨습니다.") # won
        print("*******\n")
        print(l[random.randint(0,5)])
        print("\n*******\n")
      elif s_x<s_y:
        print('\n 게임 종료\n') #end game
        time.sleep(1)
        print("지셨습니다. 다음기회에....") # lost
      time.sleep(2)
      return 0,0
      break





