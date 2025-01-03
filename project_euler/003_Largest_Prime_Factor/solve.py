def prime_factors(n):
    i = 2
    factors = []
    while i**2 <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

if __name__ == "__main__":
    print(max(prime_factors(600851475143)))