import math


if __name__ == "__main__":
    with open("../assets/base_exp.txt", "r") as f:
        data = f.readlines()
        values = []
        for entry in data:
            a, b = entry.strip().split(",")
            values.append(int(b) * math.log(int(a)))
    print(values.index(max(values)) + 1)