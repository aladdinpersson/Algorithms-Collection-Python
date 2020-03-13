# Algorithm for solving sequence alignment
# Input strings x,y of len(x) = m, len(y) = n and find minimum number of
# edit steps and the specific steps to transform x into y.

# Video of algorithm explanation: https://youtu.be/bQ7kRW6zo9Y
# Video of code explanation: https://youtu.be/XmyxiSc3LKg

# Programmed by Aladdin Persson <aladdin dot persson at hotmail dot com>
#   2020-02-15 Initial coding
#   2020-02-16 Improved find_solution and made code cleaner
#   2020-03-13 There was an error in the code in function find_solution,
#              I was working with list indexing as if it was a matrix.
#              Should be working now. Extensive testing would be good.

delta = lambda x,y,i,j: 1 if x[i] != y[j] else 0

def find_solution(OPT, m, n):
    if m == 0 or n == 0:
        return

    insert = OPT[m][n-1] + 1
    align = OPT[m-1][n-1] + delta(x,y,m-1,n-1)
    delete = OPT[m-1][n] + 1

    best_choice = min(insert, align, delete)

    if best_choice == insert:
        solution.append('insert_'+str(y[n-1]))
        return find_solution(OPT, m, n-1)

    elif best_choice == align:
        solution.append('align_' + str(y[n-1]))
        return find_solution(OPT, m-1, n-1)

    elif best_choice == delete:
        solution.append('remove_'+str(x[m-1]))
        return find_solution(OPT, m-1, n)

# alignment takes input strings x,y but also empty list solution to track the specific edits
def alignment(x, y, solution):
    n = len(y)
    m = len(x)
    OPT = [ [j for i in range(n+1)] for j in range(m+1)]
    
    for i in range(1,m+1):
        OPT[i][0] = i

    for j in range(1,n+1):
        OPT[0][j] = j

    for i in range(1,m+1):
        for j in range(1,n+1):
            OPT[i][j] = min(OPT[i-1][j-1] + delta(x,y,i-1,j-1), OPT[i-1][j] + 1, OPT[i][j-1] + 1) #align, delete, insert respectively

    find_solution(OPT, m, n)
    
    return (OPT[m][n], solution[::-1])

if __name__ == '__main__':
    solution = []
    x = 'TGACGTGC'*1
    y = 'TCGACGTCA'*1
    print('We we want to transform: ' + x + ' to: ' + y)
    min_edit, steps = alignment(x, y, solution)
    print('Minimum amount of edit steps are: ' + str(min_edit))
    print('And the way to do it is: ' + str(steps))