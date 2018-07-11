#this file is supporting pygame_dudaji

import pygame
from pygame.locals import *
import random
import RPi.GPIO as GPIO
import time

#Set pygame

dudog=0

#GPIO setup
GPIO.setmode(GPIO.BCM)
tact=[]
for i in range (22,26):
    GPIO.setup(i,GPIO.IN,pull_up_down=GPIO.PUD_UP)
    tact.append(i)
ResetSW=5
ending=1
TRY=3
GPIO.setup(ResetSW,GPIO.IN,pull_up_down=GPIO.PUD_UP)

#imload(background)
bg_f=pygame.image.load("/home/pi/edison/images/bg_forest2.png")
bg_w=pygame.image.load("/home/pi/edison/images/bg_w.png")
#imload(grass)
soil=pygame.image.load("/home/pi/edison/images/soil2.png")
#imload(digdaout)
digda = pygame.image.load("/home/pi/edison/images/dudogi.png")
#imload(life)
life = pygame.image.load("/home/pi/edison/images/heart.png")
#list
soilpos=[[35,540],[235,540],[435,540],[635,540]]
dudajipos=[[110,570],[310,570],[510,570],[710,570]]
lifepos=[[210,20],[140,20],[70,20]]



def play(dudog,TRY,num,randNum,screen,myfont):

    for j in range(10):
        if dudog==num:
            break
        elif TRY == 0:
            break
        elif GPIO.input(tact[randNum])==0:
            screen.blit(soil,soilpos[randNum])
            dudog += 1
            TRY +=1
            print(" ******\n 잡은 두더지수 : {} / {}".format(dudog,num))
            screen.blit(bg_w,(330,0))
            pygame.display.flip()
            textsurface=myfont.render("dugi : {} / {}".format(dudog,num),False,(0,0,0))
            screen.blit(textsurface,(270,0))
            pygame.display.flip()
            break
        else:
            screen.blit(digda,dudajipos[randNum])
            pygame.display.flip()
            time.sleep(0.5)
    TRY-=1
    if TRY ==2:
        screen.blit(bg_w,lifepos[TRY])
    elif TRY == 1:
        screen.blit(bg_w,lifepos[TRY])
    elif TRY == 0:
        screen.blit(bg_w,lifepos[TRY])
    screen.blit(soil,soilpos[randNum])
    pygame.display.flip()

    return dudog,TRY