import sys

input = sys.stdin.readline

num = int(input())
li = []
for n in range(num):
    li.append(input().strip())
li = list(set(li))
li = sorted(li, key=lambda x: (len(x), x.lower()))
for a in li:
    print(a)