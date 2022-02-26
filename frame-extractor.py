import cv2
import numpy as np
from PIL import Image
import imagehash
import os
import img2pdf
import frameSelector

# Important constants and variables
PATH= 'C:/Users/Lenovo/Documents/opencv-project/ExtractedSlides' #Folder to store all slides and merged pdf
FRAMES_SKIP= 30
HASH_DIFF_THRESH= 380
vid= cv2.VideoCapture('F:/Class Recordings/2022-01-21 11-32-21.mkv') # Video file name that will be analysed
keyframe_count= 1
# f= open('frame_hash_data.txt', 'r')

# success, prev_img= vid.read()
# prev_hash= imagehash.dhash(Image.fromarray(np.uint8(prev_img)).convert('RGB'), hash_size=64)

# while success:
#     i= 0
#     img= None
#     while i<FRAMES_SKIP and success:
#         success, img= vid.read()
#         i+=1

#     if not success:
#         print('Video END or Video File corrupted.')
#         break

#     curr_hash= imagehash.dhash(Image.fromarray(np.uint8(img)).convert('RGB'), hash_size=64)

    # f.write(str(curr_hash-prev_hash)+' '+str(vid.get(cv2.CAP_PROP_POS_FRAMES))+'\n')

    # if(curr_hash-prev_hash > HASH_DIFF_THRESH):
    #     print("Selected Frame:", keyframe_count, ' @ ', vid.get(cv2.CAP_PROP_POS_MSEC)/1000, 'seconds')
    #     cv2.imwrite(os.path.join(PATH, 'Frame{}.jpg'.format(keyframe_count)), img)
    #     keyframe_count+=1
    
    # prev_hash= curr_hash

# f.close()
selectedFrames= frameSelector.frameSelector()

if not os.path.exists(PATH):
    os.makedirs(PATH)
    
for framePos in selectedFrames:
    vid.set(cv2.CAP_PROP_POS_FRAMES, framePos-1)
    success, frame= vid.read()

    if not success:
        print('Video END or Video File corrupted.')
        break
    
    print("Selected Frame:", keyframe_count, ' @ ', vid.get(cv2.CAP_PROP_POS_MSEC)/1000, 'seconds')
    cv2.imwrite(os.path.join(PATH, 'Frame{}.jpg'.format(keyframe_count)), frame)
    keyframe_count+=1


vid.release()