import sys
input = sys.stdin.readline

N,M = map(int,input().strip().split())
data = list(map(int,input().strip().split()))
temp = 0
append = [0] # 0을 넣었어야함
for n in data:
    temp += n
    append.append(temp)
    

for a in range(M):
    st,en = map(int,input().strip().split())
    this = append[en]-append[st-1]

    print(this)