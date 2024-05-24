from collections import deque
import sys
input = sys.stdin.readline

A,B=  map(int,input().split())
que = deque(range(1,A+1))
res = []

while que:
    for i in range(B-1):
        que.append(que[0])
        que.popleft()
    res.append(que[0])
    que.popleft()

print('<',end="")
for idx, r in enumerate(res):
    if idx + 1 ==len(res):
        print(r,end=">")
    else:
        print(r,end=", ")