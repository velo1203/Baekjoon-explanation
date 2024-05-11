import sys
input = sys.stdin.readline

length = int(input())
xlist = []
ylist = []
for n in range(length):
    x,y = map(int,input().strip().split())
    xlist.append(x)
    ylist.append(y)


maxx = max(xlist)
maxy = max(ylist)
minx = min(xlist)
miny = min(ylist)
print((maxx-minx)*(maxy-miny))