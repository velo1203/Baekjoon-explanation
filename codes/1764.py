import sys
input = sys.stdin.readline

alen,blen = map(int,input().strip().split())
a = set(); b= set()

for _ in range(alen):
    n = input().strip()
    a.add(n)

for _ in range(blen):
    n = input().strip()
    b.add(n)

c = list(a.intersection(b))
c.sort()
print(len(c))
for human in c:
    print(human)