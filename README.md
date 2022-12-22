# Video Keyframe Extractor

---

  <p align="center">
    <img alt="OpenCV" width="100px" src="https://img.icons8.com/fluency/144/000000/opencv.png" />
    <img alt="Python" width="100px" src="https://img.icons8.com/color/144/ffffff/python--v1.png" />
    <img alt="ImageHash" width="100px" src="https://img.icons8.com/ios/100/ffffff/hashtag-2.png" />
  </p>
  
---

### Description

> _Kya matlab teacher slides nahi upload karte?_

My personal project for extracting slides/keyframes from a class recording/video and make a pdf with the selected images. </br>
Uses Python, OpenCV, ImageHash and matplotlib.

---

### Features

- Based on Python3 and OpenCV library
- Uses fast Image Difference Hashing algorithm
- Completely modular structure
- Each module can be executed independently
- Image to PDF converter module
- Video analysis progress bar
- Allows to visualise frame differences using `matplotlib`
- Allows to adjust extracting threshold to extract more or less slides accordingly
- Run `frameSelector` module to find that perfect threshold value

---

### How to Run?

- Fork and clone the repository on your local machine.
- Run `pip install -r requirements.txt`
- Edit `VIDEO_PATH` variable in `main.py` according to your video file.
- Run `python main.py`
- Follow the prompts in terminal
- Execute `frameSelector.py` to fine tune threshold value after completion of video analysis once.
- Done

---

<p align="center">
  Made with <3 by DC
</p>
