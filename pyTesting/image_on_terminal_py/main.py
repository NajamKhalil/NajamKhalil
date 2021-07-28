import matplotlib.pyplot as plt
import numpy as np
import cv2 as cv

im= cv.imread('lina.png')

r = im.shape[0]
c = im.shape[1]
m = im.shape[2]
f = open("demofile3.txt", "w")
for i in range(1,r):
    for j in range(1,c):
        print("\033[38;2;%d;%d;%dm "%(im[i,j,0],im[i,j,1],im[i,j,2]) ,end="");
        print("%03d"%im[i,j,1] ,end="")
    print('\n',end="")
#cv.waitKey(0)
