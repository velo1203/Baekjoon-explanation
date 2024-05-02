import sys

balls,length = map(int,sys.stdin.readline().rstrip().split())
balls_arrary = [0]*balls
for n in range(length):
    li_start,li_and,num = map(int,sys.stdin.readline().split())
    balls_arrary[li_start-1:li_and] = [num]*(li_and-(li_start-1))

for a in balls_arrary:
    print(a,end=" ")    