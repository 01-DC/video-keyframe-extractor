import cv2
import os

def frameExtractor(PATH, VIDEO_PATH, selectedFrames):
    vid= cv2.VideoCapture(VIDEO_PATH)

    if not os.path.exists(PATH):
        os.makedirs(PATH)
        
    for i, framePos in enumerate(selectedFrames):
        vid.set(cv2.CAP_PROP_POS_FRAMES, framePos-1)
        success, frame= vid.read()

        if not success:
            print('Video END or Video File corrupted.')
            break
        
        print('Selected Frame: {} @ {} seconds'.format(i+1, vid.get(cv2.CAP_PROP_POS_MSEC)/1000))
        
        cv2.imwrite(os.path.join(PATH, 'Frame{}.jpg'.format(i+1)), frame)

    vid.release()

if __name__ == '__main__':
    pass