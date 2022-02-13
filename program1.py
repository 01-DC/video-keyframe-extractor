import cv2
import os
from matplotlib import pyplot as plt
import numpy as np
cap = cv2.VideoCapture("s06.mp4")
frame_list = []
try:
	if not os.path.exists('data'):
		os.makedirs('data')
except OSError:
	print("Error cant make directories")

	
cframe = 0
while(True):
        if os.path.exists('data'):
                break

        
        ret, frame= cap.read()
        name = './data/' + str(cframe) + '.jpg'
        print("creating" +name)
        cv2.imwrite(name,frame)

        frame_list.append(frame)
        cframe += 1
 
        if not ret:
                break


images = {}
index = {}


import glob

for imagePath in glob.glob('./data/*.jpg'):
    filename = imagePath[imagePath.rfind("/") + 1:]
                  
    image = cv2.imread(imagePath,1)
    images[filename] = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    hist = cv2.calcHist([image],[0,1,2],None,[8,8,8],[0,256,0,256,0,256])
    hist = cv2.normalize(hist,None).flatten()
    index[filename] = hist


OPENCV_METHODS = (
	(cv2.HISTCMP_CORREL ),
	(cv2.HISTCMP_CHISQR),
	(cv2.HISTCMP_INTERSECT), 
	(cv2.HISTCMP_BHATTACHARYYA))
 

for method in OPENCV_METHODS:

	
	results = {}
	reverse = False
 
	
	
	if method in (cv2.HISTCMP_CORREL, cv2.HISTCMP_INTERSECT ):
		reverse = True




for (k, hist) in index.items():
		
		d = cv2.compareHist(index[k], hist, cv2.HISTCMP_INTERSECT)
		results[k] = d
		print(d)

        
	
for (k,hist) in index.items():
	mean__ = np.mean(index[k], dtype=np.float64)

	

for (k,hist) in index.items():
	variance = np.var(index[k], dtype=np.float64)
        

print("variance", variance)
        
standard_deviation = np.sqrt(variance)
th = mean__ + standard_deviation + 3
print("threshold value", th)

try:
	if not os.path.exists('keyframes'):
		os.makedirs('keyframes')
except OSError:
	print("Error cant make directories")


cframe1=0
for (k,hist) in index.items():
        d = cv2.compareHist(index[k], hist, cv2.HISTCMP_INTERSECT)
        ret, keyframe = cap.read()

        if not ret:
                break
        
        if (d > th):
                name = './keyframes/' + str(cframe1) + '.jpg'
                print("creating" +name)
                cv2.imwrite(name, keyframe )
                cframe1+=1