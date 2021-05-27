import matplotlib.pyplot as plt
import numpy as np
import random
from collections import defaultdict

samples_count = 100
#samples = defaultdict(int)
samples = []

for i in range(samples_count):
    LENGTH_OF_GAME = int(200-40*np.log(1-random.random()))
    samples.append(LENGTH_OF_GAME)

print(sorted(samples))

_ = plt.hist(samples, bins='auto')  # arguments are passed to np.histogram
plt.title("Histogram with 'auto' bins")
plt.show()
