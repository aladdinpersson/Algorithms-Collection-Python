# Working but not complete

import knapsack as KS
import time

def knapsack(n, C, W, v):

    for i in range(1,n+1):
        w = W[i-1]
        val = v[i-1]

        for x in range(1,C+1):
            A[i][x] = A[i-1][x]

            if x >= w:
                A[i][x] = max(A[i - 1][x], A[i-1][x-w]+val)

    return A[n][C]


with open('p08_c.txt') as f_capacity:
    capacity = int(f_capacity.readline())

with open('p08_p.txt') as f_values:
    values = []

    for line in f_values:
        values.append(int(line))

with open('p08_w.txt') as f_weights:
    weights = []

    for line in f_weights:
        weights.append(int(line))


num_objects = len(weights)
#start1=time.time()

A = [[0 for h in range(capacity+1)] for k in range(num_objects+1)]
import numpy as np
A=np.array(A)
#print(A.shape)
#print(capacity)
#final_val = knapsack(num_objects, capacity, weights, values)
#print(final_val)
#print(KS.knapsack(weights,values).solve(capacity))