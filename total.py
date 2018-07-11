#grape!
#We have 5 games for patient suffering for paralysis

import card_detect
import hand_gesture
import cv2
import rolling_dice
import pygame_dudaji
import pygame_maze
import time
start=1
cap = cv2.VideoCapture(0)
while start == 1:
	cap.release()
	#select game 1:dice, 2:concentrate_stretch_finger, 3:find and pick up card, 4: dudogi game, 5:maze
	selec = int(input("\n [게임선택]\n1.dice 2.hand_gesture 3.grab_card 4.dudaji 5.maze 6.exit\n : "))
	while selec ==1:
		cap = cv2.VideoCapture(0)
		print("\n [게임설명]\n : 선택하신 횟수만큼 주사위를던져 컴퓨터를 이기시오.\n")
		continue1=1
		while continue1==1:
			continue1, selec=rolling_dice.rolling(cap)
	while selec ==2:
		cap = cv2.VideoCapture(0)
		print("\n [게임설명]\n : 선택하신 횟수만큼 손가락을 오므렸다 폈다 하시오.\n")
		continue2 =1
		while continue2==1:
			continue2, selec=hand_gesture.counting(cap)
	while selec ==3:
		cap = cv2.VideoCapture(0)
		print("\n [게임설명]\n : 요청하는 색깔의 카드를 집으시오.\n")
		continue3 =1
		while continue3 ==1:
			continue3, selec= card_detect.colorcard(cap)
	while selec ==4:
		print("\n [게임설명]\n : 두더지를 잡아주세요!\n")
		num=int(input("몇마리의 두더지를 잡으시겠습니까??\n : "))
		continue4 =1
		print("\n : Setup 버튼을 눌러주세요! ")
		while continue4 ==1:
			continue4, selec=pygame_dudaji.dudog(num)
	while selec ==5:
		print("\n [게임설명]\n : 미로를 탈출해주세요!\n")
		step=int(input(" : 레벨을 결정해주세요. [쉬움(1)~어려움(3)]\n : "))
		continue5 =1
		while continue5 ==1:
			continue5, selec=pygame_maze.maze(step)
	while selec == 6:
		start=0
		break
			 