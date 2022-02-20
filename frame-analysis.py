from cv2 import mean
from matplotlib import pyplot as plt
import statistics

f= open('frame2.txt', 'r')

all_data= list(map(int, f.read().strip().split()))

plt.plot(all_data)

plt.show()

print(statistics.mean(all_data))
print(statistics.median(all_data))