import sys
input = sys.stdin.readline

length = []
num = int(input())
for n in range(num):
    length.append(int(input()))

length.sort()
for l in length:
    print(l)