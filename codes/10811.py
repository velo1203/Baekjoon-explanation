import sys
input= sys.stdin.readline

n, r = map(int,input().split(" "))
li = list(range(1,n+1))
for a in range(r):
    s,e = map(int,input().split(" "))
    li[s-1:e] = reversed(li[s-1:e])

for x in li:
    print(x, end=" ")