import sys
input = sys.stdin.readline

row,col = map(int,input().strip().split(' '))

mat1 = []
mat2 = []
for n in range(row):
    mat1.append(list(map(int,input().strip().split(' '))))

for n in range(row):
    mat2.append(list(map(int,input().strip().split(' '))))


for r in range(row):
    for c in range(col):
        print(mat1[r][c] + mat2[r][c], end=' ')
    print()