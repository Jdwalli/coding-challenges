
def calculate_similarity_score(r: list, l: list) -> int:
    return sum(int(item) * l.count(item) for item in r)


def calculate_total_distance(r: list, l: list) -> int:
    return sum(abs(int(r[i]) - int(l[i])) for i in range(len(r)))


if __name__ == "__main__":
    r = []
    l = []
    with open('input.txt', 'r') as file:
        for line in file:
            values = line.strip().split("   ")
            r.append(values[0])
            l.append(values[1])
        r.sort()
        l.sort()
        print(calculate_total_distance(r, l))
        print(calculate_similarity_score(r, l))
