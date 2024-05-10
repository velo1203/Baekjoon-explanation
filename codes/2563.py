import sys
input = sys.stdin.readline

paper = [[0 for j in range(100)] for i in range(100)]

length = int(input())
for i in range(length):
    x,y = map(int,input().strip().split(" "))

    for idx_x in range(x,x+10):
        for idx_y in range(y,y+10):
            paper[idx_x][idx_y] = 1
c = 0
for row in paper:
    c += row.count(1)

print(c)