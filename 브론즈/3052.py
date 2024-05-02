import sys
input = sys.stdin.readline

li = []
for n in range(10):
    num = int(input())
    if not num % 42 in li:
        li.append(num%42)

print(len(li))