import videoAnalysis
import frameSelector
import frameExtractor

FRAMES_SKIP= 30 # Increase value for faster processing but may lead to skipped slides
VIDEO_PATH= 'F:/Class Recordings/2022-01-21 11-32-21.mkv' # Absolute path of video for running script
FOLDER_PATH= 'C:/Users/Lenovo/Documents/opencv-project/ExtractedSlides' # Folder where slide images and merged pdf will be stored

videoAnalysis.videoAnalysis(FRAMES_SKIP, VIDEO_PATH)
selectedFrames= frameSelector.frameSelector()
