import sys
input = sys.stdin.readline
A = int(input())
B = list(map(int,input().strip().split()))

if A == 1:
    print(B[0]**2)

else:
    B.sort() 
    print(B[0]*B[-1])