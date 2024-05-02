import sys
input = sys.stdin.readline

li = list(range(1,31))
for n in range(28):
    num = int(input())
    li.remove(num)

for a in li:
    print(a)