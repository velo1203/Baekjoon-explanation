import sys
input = sys.stdin.readline

num = int(input().strip())
i = 1
for n in range(1,num+1):
    for a in range(num-n):
        print(" ",end="")
    for u in range(i):
        print("*",end="")
    i += 2
    print()


for n in range(1,num+1):
    for a in range(n):
        print(" ",end="")
    for u in range((num-n-1)*2+1):
        print("*",end="")
    print()