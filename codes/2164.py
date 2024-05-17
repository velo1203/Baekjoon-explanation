import sys
from collections import deque
input = sys.stdin.readline




num = int(input())
q = deque(sorted(list(range(1,num+1))))

while len(q) != 1:
    q.popleft()
    q.append(q[0])
    q.popleft()

print(q[0])