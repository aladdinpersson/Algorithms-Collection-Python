'''

'''
def function(x):
    return (x**2 - 2)


def bisection(a0, b0, eps, delta, maxit):
    # Initialize search bracket s.t a <= b
    alpha = min(a0,b0)
    beta = max(a0,b0)
    a = []
    b = []
    fa = function(alpha)
    fb = function(beta)

    if function(alpha)*function(beta) > 0:
        print("Needs to have one f(a) > 0 and f(b) < 0")

    for j in range(maxit):
        a.append(alpha)
        b.append(beta)

        # Carefully compute the midpoint in an effort to avoid numerical roundoff errors
        midpoint = alpha + (beta - alpha)/2
        fc = function(midpoint)

        # Check for small residual
        if abs(fc) <= eps:
            print("Very small function value -> we're close enough to a root")
            return alpha,beta

        # check for small bracket
        if abs(beta - alpha) <= delta:
            print("Interval is good enough --> We're close to root")
            return alpha, beta

        # Now we know we need to run more iterations
        if fa*fc < 0:
            beta = midpoint
            fb = fc
        else:
            alpha = midpoint
            fa = fc

    return alpha,beta

def main():
    a = 1
    b = 2
    #print(function(a))
    #print(function(b))
    alpha, beta = bisection(a,b,eps=1e-8,delta=1e-8, maxit=1000)
    print("Bracket is (" + str(alpha)+ ', ' + str(beta) + ')')

main()

