import os
import videoAnalysis
import frameSelector
import frameExtractor
import makePdf

FRAMES_SKIP= 30 # Increase value for faster processing but may lead to skipped slides
FOLDER_PATH= os.path.join(os.getcwd(), 'ExtractedSlides') # Folder where slide images and merged pdf will be stored
## EDIT THIS BEFORE RUNNING
VIDEO_PATH= "F:/Class Recordings/2022-01-24 14-37-41.mkv" # Absolute path of video for running script

videoAnalysis.videoAnalysis(FRAMES_SKIP, VIDEO_PATH)
selectedFrames= frameSelector.frameSelector()
frameExtractor.frameExtractor(FOLDER_PATH, VIDEO_PATH, selectedFrames)
print('Review extracted slides and delete duplicates or wrong selections.')
ch= input('Press any key to create PDF... ')
makePdf.makePdf(FOLDER_PATH)