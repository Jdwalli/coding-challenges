def calculate_sum_of_squares():
    return sum(i ** 2 for i in range(101))


def calculate_square_of_sums():
    return sum(range(101))**2

if __name__ == "__main__":
    print(calculate_square_of_sums() - calculate_sum_of_squares())