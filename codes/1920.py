import sys
input = sys.stdin.readline

length = int(input())
mat= set(map(int,input().split()))
length2 = int(input())
answer = list(map(int,input().split()))


for a in answer:
    if a in mat:
        print(1)
    else:
        print(0)