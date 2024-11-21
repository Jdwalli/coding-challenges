

def is_palindrome(n: int) -> bool:
    return str(n) == str(n)[::-1]


if __name__ == "__main__":
    solutions = [
        i
        for i in range(1, 1000000)
        if (is_palindrome(i) and is_palindrome(int(bin(i)[2:])))
    ]
    print(sum(solutions))
