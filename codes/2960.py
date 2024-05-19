import sys
input = sys.stdin.readline

N,K = map(int,input().split())

mat = [True for i in range(N+1)]
mat[0] = mat[1] = False

remove = []

for i in range(2,N+1):
    if mat[i] == True:
        j = 1
        while i * j <= N:
            if mat[i*j] == True:
                remove.append(i*j)
            mat[i*j] = False

            j +=1


print(remove[K-1])