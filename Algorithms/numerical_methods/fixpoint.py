"""
# Purpose of the fixpoint method is to solve equations of the form x = g(x)
# Note that many equations can be rewritten in this form, to solve for example for roots.

# Programmed by Aladdin Persson
#   2019-10-07 Initial programming

"""
# Rewrite x^2 = 2
def function(x):
    return (x + (2 / x)) / 2


def fixpoint(x0, tol):
    x = x0
    y = function(x)

    while abs(x - y) > tol:
        x = y
        y = function(x)

    return y


def main():
    x0 = 2
    val = fixpoint(x0, tol=1e-8)
    print(val)


main()
