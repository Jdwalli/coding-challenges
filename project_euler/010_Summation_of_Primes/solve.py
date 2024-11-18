import math


def primes_to_n(n):
    """
    Implemented using the Sieve of Eratosthenes

    Start with an array (or list) of n where all elements are set to true. 

    Set the values at index 0 and 1 to `false` since 0 and 1 are not prime.

    Begin at the first prime number 2 and mark all multiples of 2 (greater than 2) as false 
    since they are composite.

    Move to the next number that is still marked true the next prime number then 
    mark all its multiples as false.
    """

    if (n <= 2):
        return []

    primes = [True] * n
    primes[0] = False
    primes[1] = False

    for i in range(2, math.isqrt(n)):
        if primes[i]:
            for j in range(i**2, n, i):
                primes[j] = False

    return [i for i in range(n) if primes[i]]


if __name__ == "__main__":
    n = 2000000 - 1
    print(sum(primes_to_n(n)))
