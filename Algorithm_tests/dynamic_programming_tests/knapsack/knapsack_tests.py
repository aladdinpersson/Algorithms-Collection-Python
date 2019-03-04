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