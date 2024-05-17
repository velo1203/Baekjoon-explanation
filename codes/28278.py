import sys

input = sys.stdin.readline
length = int(input())

stack = []

for _ in range(length):
    command = list(map(int,input().strip().split()))

    if command[0] == 1:
        stack.append(command[1])

    elif command[0] == 2:
        if len(stack) >= 1:
            print(stack[-1])
            stack.pop()
        else:
            print(-1)
    elif command[0] == 3:
        print(len(stack))
    elif command[0] == 4:
        if len(stack) >= 1:
            print(0)
        else:
            print(1)
    elif command[0] == 5:
        if len(stack) >= 1:
            print(stack[-1])
        else:
            print(-1)