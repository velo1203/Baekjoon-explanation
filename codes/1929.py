import sys
input = sys.stdin.readline

M,N = map(int,input().split())

mat = [True for i in range(N+1)]
mat[0] = mat[1] = False

for i in range(2,int(N**0.5)+1):
    if mat[i] == True:
        j = 2
        while i * j <= N:
            mat[i*j] = False
            j +=1

for i in range(M,N+1):
    if mat[i] == True:
        print(i)