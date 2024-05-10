import sys

input = sys.stdin.readline

txt = input().strip()

if txt == txt[::-1]:
    print(1)
else:
    print(0)