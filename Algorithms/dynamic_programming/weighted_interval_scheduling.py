'''
Weighted Interval Scheduling
Explained YouTube video: https://www.youtube.com/watch?v=iIX1YvbLbvc
Implementation walkthrough video: https://www.youtube.com/watch?v=dU-coYsd7zw

Programmed by Aladdin Persson <aladdin.persson at hotmail dot com>
  2020-02-13 Initial programming
  2020-03-28 Cleaned up code by making WeightedIntervalScheduling class

Time complexity: O(nlogn)
'''

import bisect

class WeightedIntervalScheduling(object):
    def __init__(self, I):
        self.I = sorted(I, key = lambda tup : tup[1]) #(key = lambda tup : tup[1])
        self.OPT = []
        self.solution = []

    def previous_intervals(self):
        start = [task[0] for task in self.I]
        finish = [task[1] for task in self.I]
        p = []

        for i in range(len(self.I)):
            # finds idx for which to input start[i] in finish times to still be sorted
            idx = bisect.bisect(finish, start[i]) - 1
            p.append(idx)

        return p

    def find_solution(self, j):
        if j == -1:
            return

        else:
            if (self.I[j][2] + self.compute_opt(self.p[j])) > self.compute_opt(j - 1):
                self.solution.append(self.I[j])
                self.find_solution(self.p[j])

            else:
                self.find_solution(j - 1)

    def compute_opt(self, j):
        if j == -1:
            return 0

        elif (0 <= j) and (j < len(self.OPT)):
            return self.OPT[j]

        else:
            return max(self.I[j][2] + self.compute_opt(self.p[j]), self.compute_opt(j - 1))

    def weighted_interval(self):
        if len(self.I) == 0:
            return 0, self.solution

        self.p = self.previous_intervals()

        for j in range(len(self.I)):
            opt_j = self.compute_opt(j)
            self.OPT.append(opt_j)

        self.find_solution(len(self.I) - 1)

        return self.OPT[-1], self.solution[::-1]

# Small Example
# if __name__ == '__main__':
#     # They are labeled as:  (start, end, weight)
#     t1 = (0,3,3)
#     t2 = (1,4,2)
#     t3 = (0,5,4)
#     t4 = (3,6,1)
#     t5 = (4,7,2)
#     t6 = (3,9,5)
#     t7 = (5,10,2)
#     t8 = (8,10,1)
#     I = [t1,t2,t3,t4,t5,t6,t7,t8]
#     weightedinterval = WeightedIntervalScheduling(I)
#     max_weight, best_intervals = weightedinterval.weighted_interval()
#     print('Maximum weight: ' + str(max_weight))
#     print('The best items to take are: ' + str(best_intervals))