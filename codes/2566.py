import sys
input = sys.stdin.readline

row,col = 9,9


matrix = []
for c in range(col):
    matrix.append(list(map(int,input().strip().split(" "))))

ma = 0
ro = 0
for i,m in enumerate(matrix):
    if ma < max(m):
        ma = max(m)
        ro = i
print(ma)
print(ro+1,matrix[ro].index(ma)+1)