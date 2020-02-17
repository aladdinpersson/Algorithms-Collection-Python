# Weighted Interval Scheduling
# Explained YouTube video: https://www.youtube.com/watch?v=iIX1YvbLbvc
# Implementation walkthrough video: https://www.youtube.com/watch?v=dU-coYsd7zw

# Programmed by Aladdin Persson
#   2020-02-13 <aladdin.persson at hotmail dot com>

# Time complexity: O(nlogn)

import bisect

def previous_intervals(I):
    start = [task[0] for task in I]
    finish = [task[1] for task in I]
    p = []

    for i in range(len(I)):
        # finds idx for which to input start[i] in finish times to still be sorted
        idx = bisect.bisect(finish, start[i]) - 1
        p.append(idx)

    return p

def find_solution(j):
    if j == -1:
        return
    else:
        if (I[j][2] + OPT[p[j]]) >= OPT[j-1]:
            O.append(I[j])
            find_solution(p[j])
            
        else:
            find_solution(j-1)

def compute_opt(j):
    if j == -1:
        return 0

    elif (0 <= j) and (j < len(OPT)):
        return OPT[j]

    else:
        return max(I[j][2] + compute_opt(p[j]), compute_opt(j - 1))

def weighted_interval(I):
    # Weighted Interval takes as input items sorted by finish times
    for j in range(len(I)):
        opt_j = compute_opt(j)
        OPT.append(opt_j)
    
    find_solution(len(I) - 1)

    return OPT[-1]
    

if __name__ == '__main__':
    # OPT for optimal weight, O for best items to pick
    OPT = []
    O   = []

    # They are labeled as:  (start, end, weight)
    t1 = (0,3,3)
    t2 = (1,4,2)
    t3 = (0,5,4)
    t4 = (3,6,1)
    t5 = (4,7,2)
    t6 = (3,9,5)
    t7 = (5,10,2)
    t8 = (8,10,1)
    I = [t1,t2,t3,t4,t5,t6,t7,t8]
    I.sort(key = lambda tup : tup[1])
    p = previous_intervals(I)

    max_weight = weighted_interval(I)
    print('Maximum weight: ' + str(max_weight))
    print('The best items to take are: ' + str(O[::-1]))