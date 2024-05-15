import sys
input = sys.stdin.readline
length = int(input())
for n in range(length):
    A,B = map(int,input().strip().split())
    r = A*B
    while True:
        c = A % B
        if c == 0:
            break
        A = B
        B = c
    print(r//B)