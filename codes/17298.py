import sys
from collections import deque
input = sys.stdin.readline

length = int(input())
A = list(map(int,input().strip().split())) #

seq = [-1]*length
stack = deque([])

for idx, a in enumerate(A):
    while stack and A[stack[-1]] < a:
        seq[stack.pop()] = a
    stack.append(idx)

for se in seq:
    print(se,end=" ")
