
if __name__ == "__main__":
    sol = 0
    a = 1
    b = 2

    while a < 4000000:
        if a % 2 == 0:
            sol += a
        a, b = b, a + b
    
    print(sol)