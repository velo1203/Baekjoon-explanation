import sys
from collections import deque
input = sys.stdin.readline
N,K = map(int,input().strip().split())

que = deque(list(range(1,N+1)))

seq = []
while len(que) != 0:
    for idx in range(K-1):
        que.append(que[0])
        que.popleft()
    seq.append(que[0])
    que.popleft()

print("<",end="")
for i,s in enumerate(seq):
    if i == len(seq) -1:
        print(s,end="")
    else:
        print(f"{s}, ",end="")
print(">",end="")