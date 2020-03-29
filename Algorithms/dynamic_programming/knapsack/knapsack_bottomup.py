# Bottom up implementation of Knapsack (using loops)

# Purpose is if having a bunch of items with a weight and corresponding value to each object.
# Which collection of objects should we choose such that we maximize the value restricted to
# a specific capacity of weight

# Programmed by Aladdin Persson <aladdin dot persson at hotmail dot com>
#   2020-02-15 Initial programming

def find_opt(i, c, M, values, items, weights):
    if i <= 0 or c <= 0:
        return items

    if (M[i-1][c] >= (values[i-1] + M[i-1][c - weights[i-1]])) or (c - weights[i-1]) < 0:
        find_opt(i-1, c, M, values, items, weights)
        
    else:
        items.append(i-1)
        find_opt(i-1, c-weights[i-1], M, values, items, weights)
        
def knapsack(n, C, weights, values):
    # Initialization of matrix of size (n*W)
    M = [[None for i in range(C + 1)] for j in range(len(values) + 1)]

    for c in range(C+1):
        M[0][c] = 0

    for i in range(len(weights)+1):
        M[i][0] = 0

    for i in range(1, n+1):
        for c in range(1, C+1):
            # If current weight exceeds capacity then we cannot take it
            if weights[i - 1] > c:
                M[i][c] = M[i-1][c]

            # Else we can take it, then find what gives us the optimal value, either
            # taking it or not taking it and we consider what gives us max value of those
            else:
                M[i][c] = max(M[i-1][c], values[i-1] + M[i-1][c-weights[i-1]])
    items = []

    find_opt(n, C, M, values, items, weights)


    return M[n][C], items[::-1]


if __name__ == '__main__':
   # Run small example
   weights = [1,2,4,2,5]
   values = [5,3,5,3,2]
   n = len(weights)
   capacity = 3
   total_value, items = knapsack(n, capacity, weights, values)
   print('Items at the end: ' + str(items))
   print('With total value: ' + str(total_value))
