import cv2
import numpy as np
from PIL import Image
import imagehash

def videoAnalysis(FRAMES_SKIP, VIDEO_PATH):
    vid= cv2.VideoCapture(VIDEO_PATH)
    f= open('frameHashData.txt', 'w') # For storing and analysing frame hash differences

    success, prevImg= vid.read()
    prevHash= imagehash.dhash(Image.fromarray(np.uint8(prevImg)).convert('RGB'), hash_size=64)

    while success:
        i= 0
        currImg= None
        while i<FRAMES_SKIP and success:
            success, currImg= vid.read()
            i+=1

        if not success:
            print('Video END or Video File corrupted.')
            break

        currHash= imagehash.dhash(Image.fromarray(np.uint8(currImg)).convert('RGB'), hash_size=64)

        f.write(str(currHash-prevHash)+' '+str(vid.get(cv2.CAP_PROP_POS_FRAMES))+'\n')
        
        prevHash= currHash

    f.close()
    vid.release()

if __name__ == '__main__':
    videoPath= input('Enter absolute path of video file with / as separator\n')
    frameSkip= int(input('Number of frames to skip in between slides\n'))
    videoAnalysis(frameSkip, videoPath)