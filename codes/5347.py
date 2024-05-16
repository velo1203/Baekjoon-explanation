import sys
input = sys.stdin.readline

def gcd(A,B):
    while True:
        c = A % B
        if c == 0:
            break
        A = B
        B = c
    return B


num = int(input())
for n in range(num):
    A,B = map(int,input().strip().split())
    print(A*B//gcd(A,B))