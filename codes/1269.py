import sys
input = sys.stdin.readline

input()

a = set(map(int,input().strip().split()))
b= set(map(int,input().strip().split()))

c = len(a.difference(b)) + len( b.difference(a))

print(c)