# Code using image difference hashing algorithm
# This code gives much better results
# Using similarity difference hashing
# Using same input and threshold at 400
# Tested using dhash (106) best so far
# Tested using phash (245) not good
# Tested using ahash (14) worst, finds 2/3 of frames as equal

import cv2
import numpy as np
from PIL import Image
import imagehash
import os
import img2pdf

# Important constants and variables
PATH= 'C:/Users/Lenovo/Documents/opencv-project/ExtractedSlides' #Folder to store all slides and merged pdf
FRAMES_SKIP= 30
HASH_DIFF_THRESH= 400
vid= cv2.VideoCapture('input.mkv') # Video file name that will be analysed
keyframe_count= 1
# f= open('frame3.txt', 'w')

success, prev_img= vid.read()
prev_hash= imagehash.dhash(Image.fromarray(np.uint8(prev_img)).convert('RGB'), hash_size=64)

while success:
    i= 0
    img= None
    while i<FRAMES_SKIP and success:
        success, img= vid.read()
        i+=1

    if not success:
        print('Video END or Video File corrupted.')
        break

    curr_hash= imagehash.dhash(Image.fromarray(np.uint8(img)).convert('RGB'), hash_size=64)

    # f.write(str(curr_hash-prev_hash)+'\n')

    if(curr_hash-prev_hash > HASH_DIFF_THRESH):
        print("Selected Frame:", keyframe_count, ' @ ', vid.get(cv2.CAP_PROP_POS_MSEC)/1000, 'seconds')
        cv2.imwrite(os.path.join(PATH, 'Frame{}.jpg'.format(keyframe_count)), img)
        keyframe_count+=1
    
    prev_hash= curr_hash

# f.close()
vid.release()

print('Please remove any duplicate slides from folder before PDF file is created... ')
inp= input('Enter q to exit or any other key to continue...')

if inp=='q':
    exit()

# Using img2pdf library to make merged pdf
images= []
for fname in os.listdir(PATH):
    img_path= os.path.join(PATH, fname)
    images.append(img_path)

with open(os.path.join(PATH, 'merged_slides.pdf'), 'wb') as f:
    f.write(img2pdf.convert(images))