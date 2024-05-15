import sys
input = sys.stdin.readline

A,B = map(int,input().strip().split())

poc = {}
na = {}

for i in range(1,A+1):
    po = input().strip()
    poc[i] = po
    na[po] = i

for _ in range(B):
    use = input().strip()
    if use.isdigit() == True:
        print(poc[int(use)])
    else:
        print(na[use])