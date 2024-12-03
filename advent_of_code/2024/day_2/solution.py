from collections import Counter


def count_safe_reports(lst: list[str]) -> int:
    safe_reports = 0
    for report in lst:
        report = report.strip().split(" ")
        level = []
        is_valid = True
        for i in range(len(report) - 1):
            l, r = int(report[i]), int(report[i + 1])
            # Any two adjacent levels differ by at least one and at most three.
            if abs(l - r) > 3 or abs(l - r) < 1:
                is_valid = False
            if l > r:
                level.append("+")
            if l < r:
                level.append("-")
        
        if is_valid and (all(x == "+" for x in level) or all(x == "-" for x in level)):
            safe_reports += 1
        
    return safe_reports



        
        
       
    
        
    return safe_reports
        



if __name__ == "__main__":
    with open('input.txt', 'r') as file:
        print(count_safe_reports(file.readlines()))
