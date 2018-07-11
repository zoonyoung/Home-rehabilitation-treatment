#grape!
#this file is dice_recognizer using opencv

import cv2
import numpy as np

def dice_recognition(cap):
    #set parameter
    min_threshold = 10 
    max_threshold = 200  # they can be tweaked depending on the camera distance, camera angle,
    min_area = 100   
    min_circularity = .3
    min_inertia_ratio = .5
    cap.set(15, -4)   # '15' references video's brightness. '-4' sets the brightness.

    counter = 0
    readings = [0, 0]
    display = [0, 0]

    while True:
        if counter >= 90000: 
            counter = 0
            readings = [0, 0]
            display = [0, 0]

        ret, im = cap.read()

        params = cv2.SimpleBlobDetector_Params()   # declare filter parameters.
        params.filterByArea = True
        params.filterByCircularity = True
        params.filterByInertia = True
        params.minThreshold = min_threshold
        params.maxThreshold = max_threshold
        params.minArea = min_area
        params.minCircularity = min_circularity
        params.minInertiaRatio = min_inertia_ratio

        detector = cv2.SimpleBlobDetector_create(params)

        keypoints = detector.detect(im)

        # here we draw keypoints on the frame.
        im_with_keypoints = cv2.drawKeypoints(im, keypoints, np.array([]), (0, 0, 255),
                                              cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

        cv2.imshow("Dice Reader", im_with_keypoints)

        reading = len(keypoints)

        if counter % 10 == 0:
            readings.append(reading)                           

            if readings[-1] == readings[-2] == readings[-3]:    
                display.append(readings[-1])                    

            if display[-1] != display[-2] and display[-1] != 0:
                msg = str(display[-1]) + "\n****"
                return int(display[-1])
                cap.release()
                cv2.destroyAllWindows() 
        
        counter += 1

        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break
    cap.release()
    cv2.destroyAllWindows()

