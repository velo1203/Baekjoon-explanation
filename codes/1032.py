import sys
input = sys.stdin.readline

length = int(input())
li = []
for _ in range(length):
    li.append(input().strip())

for i in range(len(li[0])):
    s = set() 
    for l in li:
        s.add(l[i])
    if len(s) == 1:
        print(li[0][i],end="")
    else:
        print("?",end="")