import sys
input = sys.stdin.readline

A = []
num = int(input())
for n in range(num):
    A.append(int(input()))



for l in range(num-1):
    for i in range(num-1-l):
        if A[i] > A[i+1]:
            A[i],A[i+1] = A[i+1],A[i]

print(A)