import cv2
import os
from matplotlib import pyplot as plt
import numpy as np
from keyframe import *
cap = cv2.VideoCapture("house_tour.mpg")

cframe = 0

ret, current_frame = cap.read()

while ret:
         prev_frame = current_frame()
         ret, current_frame = cap.read()
    if ret:
        
        diff = cv2.absdiff(current_frame,prev_frame)
        hist = 

        

        for i in diff:
    
            datasubmean = np.sum(mean_deviation - i)
            datasquare = np.square(datasubmean)
            img3 = datasquare
    
            variance = np.sum(img3)/img3.size - 1
            print("variance", variance)
        
            standard_deviation = np.sqrt(variance)
            th = mean_deviation + standard_deviation

            if i.any() > th:
                name = './keyframes/current_frame' + str(cframe) + '.jpg'
                print("creating" +name)
                cv2.imwrite(name,current_frame)