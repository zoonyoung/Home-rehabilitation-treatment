#grape!
#this file is finger_concetrating_stretching_recognizer 
#using opencv

import cv2
import numpy as np
import math
from gesture.gesture_set import gesture_set
import time

def counting(cap):
    num=(int(input(" 몇번하시겠습니까? \n : ")))
    p=1
    score = 0
    t=0

    while t<(num):
        ending = 1
        count0 = 0
        count5 = 0
        while ending == 1:

            try:
                l, frame, areacnt, arearatio,mask = gesture_set(cap)
                font = cv2.FONT_HERSHEY_SIMPLEX
                if l==1:
                    if areacnt<2000:
                        k=6
                    else:
                        if arearatio<12:
                            k=0
                        elif arearatio<17.5:
                            k=0
                        else:
                            k=1
                elif l==2:
                    k=2
                elif l==3:

                      if arearatio<27:
                        k=3
                      else:
                        k=3
                elif l==4:
                    k=4
                elif l==5:
                    k=5
                elif l==6:
                    k=6
                else :
                    k=6
                cv2.putText(frame,'count : {}'.format(score),(30,50), font, 1, (0,255,255), 3, cv2.LINE_AA)
                if count0<20:
                    cv2.putText(frame,' concentrate your finger ',(0,450), font, 1, (0,0,0), 3, cv2.LINE_AA)
                if p==1 :
                    if k==0:
                        count0+=1
                if p==0:
                    if k==4 or k==5 :
                        count5+=1
                if count0>=20:
                    p=0
                    cv2.putText(frame,' stretch your finger ',(0,450), font, 1, (0,0,0), 3, cv2.LINE_AA)
                    if count5>=15:
                        score+=1
                        count0=0
                        count5=0
                        ending=0
                        t+=1
                        p=1
                if count5>=15:
                    p=1
                    cv2.putText(frame,' concentrate your finger ',(0,450), font, 1, (0,0,0), 3, cv2.LINE_AA)
                    if count0>=20:
                        score+=1
                        count0=0
                        count5=0
                        p=0
                        ending=0
                        t+=1

                #show the windows
                cv2.imshow('frame',frame)
            except:
                pass


            k = cv2.waitKey(5) & 0xFF
            if k == 27:
                cv2.destroyAllWindows()
                cap.release()
                t=num
                break

    print(" ******\n 축하합니다! 완료하였습니다! \n")
    time.sleep(1)
    cv2.destroyAllWindows()
    cap.release()
    return 0, 0


