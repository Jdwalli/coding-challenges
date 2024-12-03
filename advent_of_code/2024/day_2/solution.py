
def is_safe(xs) -> bool:
    increase_or_decrease = xs in [sorted(xs), sorted(xs, reverse=True)]
    is_valid = True
    for i in range(len(xs) - 1):
        diff = abs(xs[i] - xs[i + 1])
        if not 1 <= diff <= 3:
            is_valid = False
    return is_valid and increase_or_decrease


def count_safe_reports(lst: list[str]) -> int:
    safe = 0
    for report in lst:
        report = list(map(int, report.split()))
        if is_safe(report) == True:
            safe += 1

    return safe


def problem_dampener(lst: list[str]) -> int:
    safe = 0
    for report in lst:
        reports = list(map(int, report.split()))
        if (any(is_safe(reports[:index] + reports[index + 1:]) for index in range(len(reports)))):
            safe += 1
    return safe


if __name__ == "__main__":
    with open('input.txt', 'r') as file:
        print(count_safe_reports(file.readlines()))
        file.seek(0)
        print(problem_dampener(file.readlines()))
