import sys
input = sys.stdin.readline

length = int(input())
stack = []
for n in range(length):
    num = int(input())
    if num == 0:
        stack.pop()
    else:
        stack.append(num)

print(sum(stack))