# Code using image hashing algorithm

import cv2
import numpy as np
from PIL import Image
import imagehash
from matplotlib import cm

FRAMES_SKIP= 30
# vid= cv2.VideoCapture('input2.mkv')
vid= cv2.VideoCapture('input3.mkv')
# f= open('frame2.txt', 'w')
c= 1

success, prev_img= vid.read()

prev_hash= imagehash.dhash(Image.fromarray(np.uint8(prev_img)).convert('RGB'), hash_size=64)

while success:
    i= 0
    img= None
    while i<FRAMES_SKIP and success:
        success, img= vid.read()
        i+=1

    if not success:
        break
    curr_hash= imagehash.dhash(Image.fromarray(np.uint8(img)).convert('RGB'), hash_size=64)
    # f.write(str(curr_hash-prev_hash)+'\n')
    if(curr_hash-prev_hash > 400):
        print("Selected Frame: ",c)
        cv2.imwrite('Frame '+str(c)+'.jpg', img)
        c+=1
        # cv2.imshow('selected frame', img)
        # cv2.waitKey(1000)
    prev_hash= curr_hash

vid.release()