from math import gcd

if __name__ == "__main__":
    n = 20
    result = 1
    for i in range(2, n + 1):
        result = result * i // gcd(result, i)
    print(result)