import sys

input = sys.stdin.readline
length = int(input())

num = 1
for i in range(length):
    num += 6*i
    if num >= length:
        print(i+1)
        break