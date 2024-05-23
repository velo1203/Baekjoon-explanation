import sys
input = sys.stdin.readline

a,b,c = map(int,input().strip().split())
x = 0
for _ in range(c):
    a = (a%b)*10
    x = a//b
print(x)