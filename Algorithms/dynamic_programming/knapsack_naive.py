def knapsack(n, C, W, v):
    # if n == 0 we cannot index further (since we look at n-1), further if we have no more capacity
    # then we cannot obtain more objects
    if n == 0 or C == 0:
        result = 0

    # If the weight is higher than our capacity then we can't pick it
    elif W[n-1] > C:
        result = knapsack(n-1,C, W, v)

    # Recursively search through all choices
    else:
        tmp1 = knapsack(n-1,C,W,v)
        tmp2 = v[n-1] + knapsack(n-1,C - W[n-1], W, v)

        result=max(tmp1,tmp2)

    return result

weight = [1,2,4,2,5]
value = [5,3,5,3,2]
num_objects = len(weight)

total_val = knapsack(num_objects, 3, weight, value)
print(total_val)
