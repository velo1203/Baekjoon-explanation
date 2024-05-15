import sys
input = sys.stdin.readline

A,B = map(int,input().strip().split())
li= []
for n in range(1,B+1):
    li.extend([n]*n)

a = li[A-1:B]

print(sum(a))