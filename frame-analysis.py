from matplotlib import pyplot as plt

f= open('frame.txt', 'r')

all_data= list(map(int, f.read().strip().split()))

plt.plot(all_data)

plt.show()