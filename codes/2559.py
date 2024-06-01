import sys
input = sys.stdin.readline

N,K = map(int,input().split())

mat = list(map(int,input().split()))

sumli = [0]
temp = 0

for m in mat:
    temp += m
    sumli.append(temp)


al = set()

dx = 0
while K + dx <= N:
    al.add(sumli[K+dx]-sumli[dx])
    dx+=1

print(max(al))