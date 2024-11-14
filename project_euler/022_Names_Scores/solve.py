
if __name__ == "__main__":
    with open("../assets/names.txt", "r") as f:
        data = f.readline().replace("\"", "").split(",")
        data.sort()
        solution = 0
        for pos in range(len(data)):
            score = sum((ord(char) - 64) for char in data[pos])
            solution += ((pos + 1) * score)

    print(solution)
