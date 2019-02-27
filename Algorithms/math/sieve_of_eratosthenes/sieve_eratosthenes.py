# Purpose of this is to find primes from [2,n]

# Programmed by Aladdin Persson <aladdin.persson at hotmail dot com>
#   2019-02-27 Initial programming

def eratosthenes(n):
    primes, sieve = [], [True] * (n+1)
    sieve[0], sieve[1] = 'Zero', 'One'

    for num in range(2,n+1):
        if sieve[num]:
            primes.append(num)

            for i in range(num*num, n+1, num):
                sieve[i] = False

    return primes

primes = eratosthenes(10**3)
print(primes)




