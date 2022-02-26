import cv2
import os


def frameExtractor():
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