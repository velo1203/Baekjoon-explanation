import sys
input = sys.stdin.readline

se = set()

length = int(input().strip())
for _ in range(length):
    command = input().strip().split()
    if command[0] == "add":
        se.add(int(command[1]))
    elif command[0] == "remove":
        se.discard(int(command[1]))
    elif command[0] == "check":
        if int(command[1]) in se:
            print(1)
        else:
            print(0)
    elif command[0] == "toggle":
        num = int(command[1])
        if num in se:
            se.remove(num)
        else:
            se.add(num)
    elif command[0] == "all":
        se = set(range(1, 21))
    elif command[0] == "empty":
        se.clear()
