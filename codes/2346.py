import sys
from collections import deque

input = sys.stdin.readline
length = int(input().strip())
nums = list(map(int, input().strip().split()))
idx = deque(range(length))

for i in range(length):
    print(idx[0] + 1, end=" ")
    if len(idx) == 1:
        break
    rotate = nums[idx[0]]
    idx.popleft()
    if rotate > 0:
        idx.rotate(-(rotate - 1))
    else:
        idx.rotate(-rotate)
