import matplotlib.pyplot as plt
import numpy as np
import cv2 as cv
import os as os
import time
cap= cv.VideoCapture('tom.mp4')
while(cap.isOpened()):
    #print(entry)
    ret, frame = cap.read()
    r = frame.shape[0]
    c = frame.shape[1]
    m = frame.shape[2]
    #f = open("demofile3.txt", "w")
    for i in range(1,r-50):
        for j in range(1,c):
            print("\033[38;2;%d;%d;%dm "%(frame[i,j,0],frame[i,j,1],frame[i,j,2]) ,end="");
            #print("%03d"%frame[i,j,1] ,end="")
            print("@",end="")
        print('\n',end="")
    #time.sleep(0.1)
    os.system('cls' if os.name == 'nt' else 'clear')
cap.release()
cv2.destroyAllWindows()