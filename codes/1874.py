import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
target = deque() # 유저 입력
seq = deque() # delete stack

for _ in range(N):
    num = int(input())
    seq.append(num)

log = []
for nm in range(1,N+1):
    target.append(nm)
    log.append("+")
    while True:
        if target and target[-1] == seq[0]:
            seq.popleft()
            target.pop()
            log.append("-")
        else:
            break

if not seq:
    for l in log:
        print(l)
else:
    print("NO")