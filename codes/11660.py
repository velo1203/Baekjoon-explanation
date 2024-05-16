import sys
input = sys.stdin.readline
N,M = map(int,input().strip().split())

A = [[0]*(N+1)]# 기존 메트릭스
D = [[0]*(N+1) for _ in range(N+1)]#부분합 메트릭스

for _ in range(N):
    ma = list(map(int,input().strip().split()))
    ma.insert(0,0)
    A.append(ma)

for i in range(1,N+1): #row (Y) position
    for j in range(1,N+1): #colume (x) position
        D[i][j] = D[i-1][j] + D[i][j-1] -D[i-1][j-1] + A[i][j]


for _ in range(M):
    y1,x1,y2,x2 = map(int,input().strip().split()) #행렬로 세로 가로순서입니다.


    ran = D[y2][x2] + D[y1-1][x1-1] - D[y1-1][x2] -D[y2][x1-1]
    print(ran)