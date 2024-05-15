import sys
input = sys.stdin.readline
N,k = map(int,input().strip().split())

li = list(map(int,input().strip().split()))
li.sort(reverse=True)

print(li[k-1])
