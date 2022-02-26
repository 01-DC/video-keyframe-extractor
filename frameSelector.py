# Script for analysing the comparison value and to determine threshold
from matplotlib import pyplot as plt

def frameSelector() -> list[float]:
    frameHashValue, frameNumber= [], []
    with open('frame_hash_data.txt', 'r') as f:
        for line in f:
            x, y= line.strip().split()
            frameHashValue.append(int(x))
            frameNumber.append(float(y))

    ch= input('Plot of analysed values? (Y/N): ')
    if ch == 'Y':
        plt.plot(frameNumber, frameHashValue)
        plt.title('Analysed frame difference values')
        plt.show()

    thresh= int(input("Enter Threshold value (recommended between 350 to 400): "))

    selectedFrames= []
    for i, val in enumerate(frameHashValue):
        if val >= thresh:
            selectedFrames.append(frameNumber[i])

    return selectedFrames

if __name__ == '__main__':
    l= frameSelector()
    print(l)
    print(len(l))