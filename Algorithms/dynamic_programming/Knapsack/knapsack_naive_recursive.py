# "Naive" Implementation of the knapsack problem

# Purpose is if having a bunch of items with a weight and corresponding value to each object.
# Which collection of objects should we choose such that we maximize the value restricted to
# a specific capacity of weight?

# Programmed by Aladdin Persson <aladdin dot persson at hotmail dot com>
#   2019-02-28 Initial programming
#   2019-03-04 Cleaned up code and included a tracking of which items to choose

def knapsack(n, C, W, v, items):
    # if n == 0 we cannot index further (since we look at n-1), further if we have no more capacity
    # then we cannot obtain more objects
    if n == 0 or C == 0:
        return 0, []

    # If the weight is higher than our capacity then we can't pick it
    elif W[n-1] > C:
        result, items = knapsack(n-1,C, W, v, items)

    # Recursively search through all choices
    else:
        tmp1, items1 = knapsack(n-1, C, W, v, items) # exclude item
        tmp2, items2 = knapsack(n - 1, C - W[n - 1], W, v, items) # include item

        items=items2+[n-1] if (tmp2+v[n-1] > tmp1) else items1

        result=max(tmp1,tmp2+v[n-1])

    return result, items


# Small example
weight = [1,2,4,2,5]
value = [5,3,5,3,2]
num_objects = len(weight)
capacity = 3

arr = [[None for i in range(capacity)] for j in range(num_objects)]

total_val_and_items = knapsack(num_objects, capacity, weight, value, [])
print(total_val_and_items)

# items = []
#
# with open('p01_c.txt') as f_capacity:
#     capacity = int(f_capacity.readline())
#
# with open('p01_p.txt') as f_values:
#     values = []
#
#     for line in f_values:
#         values.append(int(line))
#
# with open('p01_w.txt') as f_weights:
#     weights = []
#
#     for line in f_weights:
#         weights.append(int(line))
#
# num_objects = len(weights)
# start1=time.time()
# total_val, items = knapsack(num_objects, capacity, weights, values, [])
# print(items)
#
# print(total_val)
#
# print(time.time()-start1)
# print(KS.knapsack(weights,values).solve(capacity))