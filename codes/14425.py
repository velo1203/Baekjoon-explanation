import sys
input = sys.stdin.readline

N,M = map(int,input().strip().split())
s = set()

for _ in range(N):
    n = input().strip()
    s.add(n)

li = []
for _ in range(M):
    a = input().strip()
    li.append(a)

c = 0
for l in li:
    if l in s:
        c += 1

print(c)