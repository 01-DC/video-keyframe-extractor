# Working code for extracting key frames
# Now looking for improvements

import cv2
import numpy as np

p_frame_thresh= 360000 # modify constant to make more accurate
p_frame_count= 0

vid= cv2.VideoCapture('output2.mkv')

success, prev_frame= vid.read()

while success:
    success, curr_frame= vid.read()
    if success:
        diff= cv2.absdiff(curr_frame, prev_frame)
        non_zero_count= np.count_nonzero(diff)
        if non_zero_count > p_frame_thresh:
            p_frame_count+= 1
            print("Got P-Frame", p_frame_count)
            cv2.imshow('frame', curr_frame)
            if cv2.waitKey(30) & 0xFF == ord('q'):
                break

        prev_frame= curr_frame

vid.release()
cv2.destroyAllWindows()