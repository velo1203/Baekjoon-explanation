import sys
input = sys.stdin.readline

N,M = map(int,input().split())
li = list(map(int,input().split()))

mat = [] #부분합
temp = 0
for l in li:
    temp += l
    mat.append(temp)

remain = [0] * M


for re in mat:
    rem = re % M
    remain[rem] += 1

count = 0
count += remain[0]
for r in remain:
    count += r*(r-1)/2

print(int(count))