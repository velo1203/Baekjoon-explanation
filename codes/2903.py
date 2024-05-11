import sys
input = sys.stdin.readline

length = int(input())
size = 2
for n in range(length):
    size = size*2 - 1

print(size*size)
