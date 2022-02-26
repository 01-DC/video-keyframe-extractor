import cv2
import numpy as np
from PIL import Image
import imagehash

def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█'):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = '\r')
    if iteration == total: 
        print()

def videoAnalysis(FRAMES_SKIP, VIDEO_PATH):
    vid= cv2.VideoCapture(VIDEO_PATH)
    f= open('frameHashData.txt', 'w', buffering=1) # For storing and analysing frame hash differences
    printProgressBar(vid.get(cv2.CAP_PROP_POS_FRAMES), vid.get(cv2.CAP_PROP_FRAME_COUNT), prefix = 'Progress:', suffix = 'Complete', length = 50)

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
        printProgressBar(vid.get(cv2.CAP_PROP_POS_FRAMES), vid.get(cv2.CAP_PROP_FRAME_COUNT), prefix = 'Progress:', suffix = 'Complete', length = 50)

    f.close()
    vid.release()

if __name__ == '__main__':
    videoPath= input('Enter absolute path of video file with / as separator\n')
    frameSkip= int(input('Number of frames to skip in between slides\n'))
    videoAnalysis(frameSkip, videoPath)