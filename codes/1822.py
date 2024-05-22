import sys
input = sys.stdin.readline

input()
a = set(map(int,input().split()))
b = set(map(int,input().split()))
c = sorted(list(a-b))
if len(c) != 0:
    print(len(c))
    for i in c:
        print(i,end=" ")
else:
    print(0)