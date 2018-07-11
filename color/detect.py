#grape!
#this file is supporting card_detect
#using opencv
#using circle detect
import cv2
import numpy as np

#setting
font = cv2.FONT_HERSHEY_SIMPLEX
lower = {'red':(166, 84, 141), 'green':(66, 122, 0), 'blue':(97, 100, 117), 'yellow':(23, 59, 119)} #assign new item lower['blue'] = (93, 10, 0)
upper = {'red':(186,255,255), 'green':(86,255,255), 'blue':(117,255,255), 'yellow':(54,255,255)}
colors = {'red':(0,0,255), 'green':(0,255,0), 'blue':(255,0,0), 'yellow':(0, 255, 217)}
color = ['red','green','blue','yellow']

def detect(a,hsv,frame,randNum,count):
#Set mask
    kernel = np.ones((9,9),np.uint8)
    mask = cv2.inRange(hsv, lower[a], upper[a])
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

# find contours in the mask
    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[-2]
    center = None

# contours > 0
    if len(cnts) > 0:
        c = max(cnts, key=cv2.contourArea)
        ((x, y), radius) = cv2.minEnclosingCircle(c)

# threshold using radius. when color is detection draw rectangle using circle parameter
        if radius > 0.5:
            cv2.rectangle(frame, (int(x-radius), int(y-radius)), (int(x+radius), int(y+radius)), colors[a], 2)
            cv2.putText(frame,a + "card", (int(x-radius),int(y-radius)),font , 0.6,colors[a],2)
    cv2.putText(frame,"pick up {} card".format(color[randNum]), (50,450),font, 1,(0,0,0),2)
    if len(cnts)>0 and radius>0.5:
        count+=1
    return count
