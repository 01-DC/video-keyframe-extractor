# Script for analysing the comparison value and to determine threshold

from cv2 import mean
from matplotlib import pyplot as plt
import statistics

# f= open('frame2.txt', 'r')
f= open('frame3.txt', 'r')
# f= open('frame3_dhash.txt', 'r') # for SPM Slides

all_data= list(map(int, f.read().strip().split()))
plt.plot(all_data)
plt.show()
all_data.sort()
upper_all_data= all_data[len(all_data)//2:]
selected_frames= [x for x in all_data if x>0]

print(len(selected_frames))
print(statistics.mean(all_data))
print(statistics.mean(upper_all_data))
print(statistics.median(all_data))