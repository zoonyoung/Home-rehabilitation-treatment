#grape!
#this fili is dudaji_game!
#using pygame
#using GPIO(TACT!)
from dudaji.pygame_dudaji_set import ResetSW, life, lifepos, bg_w, bg_f,soil, soilpos, play
import time
import random
import pygame
import RPi.GPIO as GPIO

def dudog(num):
    pygame.init()
    width, height=900, 675
    screen = pygame.display.set_mode((width,height))
    pygame.font.init()
    myfont=pygame.font.SysFont('Comic Sans MS',50)
    screen.fill(0)
    screen.blit(bg_f,[0,0])
    for i in range(4):
        screen.blit(soil,soilpos[i])
    for i in range(3):
        screen.blit(life,lifepos[i])
    pygame.display.flip()

    ending=1
    while 1:
        if ending == 1:
            if GPIO.input(ResetSW)==0:
                print("\n ******\n 게임 시작! ")
                ending=0
                dudog=0
                TRY=3
                for i in range (3):
                    screen.blit(life,lifepos[i])
        elif dudog==num:
            for i in range (3):
                print("\n******\n 축하합니다! 두더지를 다잡았습니다! ")
                time.sleep(1)
                go=int(input("\n 1.게임시작 2.게임종료\n : "))
                if go == 2:
                    return 0,0
                    break
                else: print("\n : Setup 버튼을 눌러주세요! ")
                screen.blit(bg_w,lifepos[i])
                pygame.display.flip()

            ending =1
        elif TRY == 0:
            print("\n******\n 안타까워요! 두더지를 잡지 못했어요... ")
            go=int(input("\n 1.게임시작 2.게임종료\n : "))
            if go == 2 :
                return 0,0
                break
            else : print("\n : Setup 버튼을 눌러주세요! ")
            ending=1
        elif ending==0:
            randNum=random.randint(0,3)
            dudog,TRY= play(dudog,TRY,num,randNum,screen,myfont)
            time.sleep(3)

