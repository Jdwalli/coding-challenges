
def special_pythagorean_triplet(number: int) -> int:
    for a in range(1, number // 3):
        for b in range(a + 1, number // 2):
            c = number - a - b
            if a ** 2 + b ** 2 == c ** 2:
                return a * b * c
    return 0

if __name__ == "__main__":
    print(special_pythagorean_triplet(1000))