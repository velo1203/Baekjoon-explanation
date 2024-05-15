import sys
input = sys.stdin.readline

A,B = map(int,input().strip().split())
while True:
    c = A % B
    if c == 0:
        break
    A = B
    B = c

print("1"*B)