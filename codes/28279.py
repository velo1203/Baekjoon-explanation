from collections import deque
import sys
input = sys.stdin.readline

deq = deque()
length = int(input())

for _ in range(length):
    command = input().strip().split()
    
    if command[0] == "1":
        deq.appendleft(command[1])
    elif command[0] == "2":
        deq.append(command[1])
    elif command[0] == "3":
        if deq:
            print(deq.popleft())
        else:
            print(-1)
    elif command[0] == "4":
        if deq:
            print(deq.pop())
        else:
            print(-1)
    elif command[0] == "5":
        print(len(deq))
    elif command[0] == "6":
        print(0 if deq else 1)
    elif command[0] == "7":
        if deq:
            print(deq[0])
        else:
            print(-1)
    elif command[0] == "8":
        if deq:
            print(deq[-1])
        else:
            print(-1)
