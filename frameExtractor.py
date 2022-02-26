import cv2
import os

def frameExtractor(PATH, VIDEO_PATH, selectedFrames=None):
    vid= cv2.VideoCapture(VIDEO_PATH)

    if not os.path.exists(PATH):
        os.makedirs(PATH)
    
    if selectedFrames==None:
        selectedFrames= [i for i in range(0, int(vid.get(cv2.CAP_PROP_FRAME_COUNT)), int(vid.get(cv2.CAP_PROP_FPS)))]
    
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
    print('\nFrames at interval of 1 second will be extracted...\n')
    path= os.getcwd()
    videoPath= input('Enter absolute path of video file with / as separator\n')
    frameExtractor(path, videoPath, None)