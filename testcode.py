def print_pattern(n):
    for i in range(n):
        print(' ' * i, end='')
        
        for j in range(n - i):
            print(chr(65 + j), end='')
        
        for j in range(n - i - 2, -1, -1):
            print(chr(65 + j), end='')
        
        print()
floors = int(input("층수를 입력하세요: "))
print_pattern(floors)
