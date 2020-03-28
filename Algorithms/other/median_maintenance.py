# Purpose of median_maintenance is given numbers, x then y, w, etc, maintain the median.

# Programmed by Aladdin Persson
#   2019-02-16 <aladdin.persson at hotmail dot com>

# This is an optimized version using heap

# note: heapq is a min-heap that is why we do -x, also we want all small values in the maxheap
# and all large values in the minheap so that we can take the value on the top as our median

# Improvements to be made:
#   * Do it without the use of globals
#   * Comment code

import heapq

class Maintain_Median(object):
    def __init__(self):
        self.maxheap = []
        self.minheap = []

    def medmain_insert(self, x):
        if (len(self.maxheap) == 0):
            heapq.heappush(self.maxheap, -x)

        else:
            m = -self.maxheap[0]
            if x > m:
                heapq.heappush(self.minheap, x)

                if len(self.minheap) > len(self.maxheap):
                    y = heapq.heappop(self.minheap)
                    heapq.heappush(self.maxheap, -y)

            else:
                heapq.heappush(self.maxheap, -x)

                if len(self.maxheap) - len(self.minheap) > 1:
                    y = -heapq.heappop(self.maxheap)
                    heapq.heappush(self.minheap, y)

        return (-self.maxheap[0] + self.minheap[0])/2 if len(self.maxheap) == len(self.minheap) else -self.maxheap[0]


    def main(self, data):
        if len(data) < 1:
            return data

        for x in data:
            median = self.medmain_insert(x)

        return median

if __name__ == '__main__':
    data = [1, 3, 8, 5, 10]
    maintain_median = Maintain_Median()
    median = maintain_median.main(data)
    print(median)