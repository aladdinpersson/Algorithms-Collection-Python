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

maxheap = None
minheap = None

def initialize():
    global maxheap, minheap

    maxheap = []
    minheap = []


def medmain_insert(x):
    global maxheap, minheap

    if (len(maxheap)==0):
        heapq.heappush(maxheap, -x)
    else:
        m = -maxheap[0]
        if x > m:
            heapq.heappush(minheap,x)

            if len(minheap) > len(maxheap):
                y = heapq.heappop(minheap)
                heapq.heappush(maxheap, -y)

        else:
            heapq.heappush(maxheap, -x)

            if len(maxheap) - len(minheap) > 1:
                y = -heapq.heappop(maxheap)
                heapq.heappush(minheap, y)

    return -maxheap[0]


def test():
    data = [1,3,8,5,10]

    initialize()

    for x in data:
        median = medmain_insert(x)

    print(median)

heap_low = None
heap_high = None

test()




