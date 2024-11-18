
def is_palindrome(number):
    return str(number) == str(number)[::-1]

if __name__ == "__main__":
    largest = 0
    for x in range(1, 1000):
        for y in range(1, 1000):
            product = x * y
            if is_palindrome(x * y) and x * y > largest:
                largest = x * y

    print(largest)
