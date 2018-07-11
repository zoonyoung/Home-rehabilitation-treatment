#grape!
#this file is detecting color card[red,green,blue,yellow]
#using opencv
import argparse
import cv2
import random
#import def detect
from color.detect import detect,color
import time

def colorcard(cap):
    num=int(input(" : 몇장의 카드를 집으시겠습니까?\n : "))
    score =0
    i=0
    kor_color =["빨강색", "초록색", "파랑색", "노랑색"]
    #counting color card
    while i <num:
        p=1
        randNum=random.randint(0,3)
        ending=1
        count=0
        while ending ==1:
            (grabbed, frame) = cap.read()
            frame=cv2.flip(frame,1)
            blurred = cv2.GaussianBlur(frame, (11, 11), 0)
            hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
            count = detect(color[randNum],hsv,frame,randNum,count)
            if p ==1:
                print(" {}카드를 집어주세요!".format(kor_color[randNum]))
                p=0
            if count >=10:
                score+=1
                ending =0
                p=0
                i+=1
                print(" 다음! ")
                time.sleep(1)
            # show the frame to our screen
            cv2.imshow("Frame", frame)
            if score == num:
                print("\n ******\n 축하합니다! 전부다 맞추셨습니다! ")
                time.sleep(1)
                cap.release()
                cv2.destroyAllWindows()
                break

            key = cv2.waitKey(1) & 0xFF
            if key == 27:
                ending=0
                i=num
                break
    return 0,0

    cap.release()
    cv2.destroyAllWindows()
