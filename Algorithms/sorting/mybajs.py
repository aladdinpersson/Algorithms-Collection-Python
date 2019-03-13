import random
import time
import numpy as np

import matplotlib.pyplot as plt

from bubblesort import bubblesort
from randomized_quicksort import quicksort_randomized

n = [5*i for i in range(100)]
print(n)
save_times = []

for size in n:
    # print(save_times)
    tot_time = 0

    for i in range(100):
        unsorted_arr = [random.randrange(1, 10) for _ in range(size)]

        start = time.time()
        sorted_arr = quicksort_randomized(unsorted_arr)
        tot_time += (time.time() - start)

    save_times.append(tot_time/100)

plt.plot(n, save_times)
plt.show()



