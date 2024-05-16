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

a,b = map(int,input().strip().split())

gcded = gcd(a,b)
print(gcded)
print(a*b//gcded)