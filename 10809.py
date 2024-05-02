import sys
input = sys.stdin.readline
string = input().strip()
aList = [chr(i) for i in range(ord('a'),ord('z')+1)]

res = []
for n in aList:
    res.append(string.find(n))

for rs in res:
    print(rs,end=" ")