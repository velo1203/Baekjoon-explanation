import sys

input = sys.stdin.readline

A,B = input().strip().split()

C = int(A[::-1]) + int(B[::-1])
print(int(str(C)[::-1]))