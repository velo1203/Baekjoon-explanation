import sys
input = sys.stdin.readline
r = int(input())

for n in range(r):
    a = input()
    print(a[0] + a[-2])