import sys
input = sys.stdin.readline

N,M = map(int,input().split())
list1 = list(map(int,input().split()))
list2 = list(map(int,input().split()))
l = list1+ list2
l.sort()

for li in l:
    print(li,end=" ")