import sys
input = sys.stdin.readline

matrix = []

for n in range(5):
    matrix.append(list(input().strip()))


for a in range(15):
    for i,mat in enumerate(matrix):
        if (len(mat)-1) >= a:
            print(mat[a],end="")