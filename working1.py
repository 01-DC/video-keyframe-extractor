# Working code for extracting key frames
# Now looking for improvements

import cv2
import numpy as np

p_frame_thresh_max= 800000 # modify constant to make more accurate
p_frame_thresh_min= 700000 # modify constant to make more accurate
p_frame_count= 0

# input3.mkv is SPM sir class
vid= cv2.VideoCapture('input3.mkv')

success, prev_frame= vid.read()
# f= open('frame.txt', 'w')

while success:
    success, curr_frame= vid.read()
    if success:
        diff= cv2.absdiff(curr_frame, prev_frame)
        non_zero_count= np.count_nonzero(diff)
        # f.write(str(non_zero_count)+'\n')
        if p_frame_thresh_min <= non_zero_count <= p_frame_thresh_max:
            p_frame_count+= 1
            print("Got P-Frame", p_frame_count)
            cv2.imwrite('Frame '+str(p_frame_count)+'.jpg', curr_frame)
            # cv2.imshow('frame', curr_frame)
            # if cv2.waitKey(0) & 0xFF == ord('q'):
                # break

        prev_frame= curr_frame

vid.release()
# cv2.destroyAllWindows()