import sys
input = sys.stdin.readline

n = int(input())
mat = list(map(int,input().split()))
t = int(input())
sumli = [0]
temp = 0

for m in mat:
    temp+=m
    sumli.append(temp)
idx = 0
c =0 
while True:
    if 2 + idx +1> n:
        break

    if sumli[2+idx+1] - sumli[idx] == n:
        c += 1
    idx+=1

print(c)