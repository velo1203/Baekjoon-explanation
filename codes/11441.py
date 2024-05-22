import sys
input = sys.stdin.readline

length = int(input())
mat = list(map(int,input().split()))

temp = 0
li = []
for n in mat:
    temp = temp+n
    li.append(temp)

ren = int(input())
for _ in range(ren):
    M,N = map(int,input().split())
    if M-2 < 0:
        print(li[N-1])
    else:
        print(li[N-1]-li[M-2])