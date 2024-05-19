import sys
input = sys.stdin.readline

length = int(input())
A = []
for _ in range(length):
    n = int(input())
    A.append(n)

B = A #A의 정렬 전 리스트
A.sort()