import sys
from collections import deque
input = sys.stdin.readline

stack = deque()

txt = input().strip()
txts = []
for idx,t in enumerate(txt):
    if len(txt)-1 > idx and txt[idx+1] == "(":
        stack.append(int(t))
print(txts)