import sys
input = sys.stdin.readline

length = int(input())
li =[]

for _ in range(length):
    num = int(input())
    li.append(num)


li.sort(reverse=True)
for l in li:
    print(l)