import sys
input = sys.stdin.readline

input()

li = set(map(int,input().strip().split()))
input()

li_next=  list(map(int,input().strip().split()))

for l in li_next:
    if l in li:
        print(1,end=" ")
    else:
        print(0,end=" ")