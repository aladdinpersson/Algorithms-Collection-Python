# Interval Scheduling, we have a set of requests R and we wish to choose
# the maximum amount of non-overlapping intervals and output the optimal
# solution as O.

# Programmed by Aladdin Persson <aladdin.persson at hotmail dot com>
#   2020-01-25 Initial programming

def interval_scheduling(R):
    finish = 0

    for r in R:
        # remember r[0] start time of request r, r[1] finish time of request r
        if finish <= r[0]:
            finish = r[1]
            O.append(r)
y
    print(O)

def interval_scheduling_complicated_version(R):
    while R: # keep going while R still has elements
        (si, fi) = R[0]
        O.append((si,fi))
        idx = 0

        while idx < len(R):
            (sj, fj) = R[idx]

            if fi > sj:
                R.remove(R[idx])
                idx -= 1

            idx += 1

if __name__ == '__main__':
    # request is: (start, end)
    r1 = (0, 3)
    r2 = (1, 3)
    r3 = (0, 5)
    r4 = (3, 6)
    r5 = (4, 7)
    r6 = (3, 9)
    r7 = (5, 10)
    r8 = (8, 10)
    R = [r1,r2,r3,r4,r5,r6,r7,r8]
    R.sort(key=lambda x: x[1]) # sort by finish times f1 <= f2 <= ... <= fn
    O = []

    interval_scheduling(R)
    print('The intervals to choose are: ' + str(O))