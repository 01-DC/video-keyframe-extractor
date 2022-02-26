# Script for analysing the comparison value and to determine threshold
from matplotlib import pyplot as plt

frameHashValue, frameNumber= [], []
with open('frame_hash_data.txt', 'r') as f:
    for line in f:
        x, y= line.strip().split()
        frameHashValue.append(int(x))
        frameNumber.append(float(y))

plt.plot(frameNumber, frameHashValue)
plt.title('Analysed frame difference values')
plt.show()

thresh= int(input("Enter Threshold value (recommended= 400): "))

selectedFrames= []
for i, val in enumerate(frameHashValue):
    if val >= thresh:
        selectedFrames.append(frameNumber[i])

print(selectedFrames)