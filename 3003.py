import sys
input = sys.stdin.readline

txt = list(map(int,list(input().split(" "))))
config = [1,1,2,2,2,8]
for i,t in enumerate(txt):
    print(config[i]-t,end=" ")