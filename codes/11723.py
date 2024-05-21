import sys
input = sys.stdin.readline

se = set()

length =int(input())
for n in range(length):
    command = input().strip().split()
    if command[0] == "add":
        se.add(command[1])
    elif command[0] == "remove":
        if command[1] in se:
            se.remove(command[1])
    elif command[0] == "check":
        if command[1] in se:
            print(1)
        else:
            print(0)
    elif command[0] == "toggle":
        if command[1] in se:
            se.remove(command[1])
        else:
            se.add(command[1])
    elif command[0] == "all":
        se = set(range(1,21))
    elif command[0] == "empty":
        se = set()