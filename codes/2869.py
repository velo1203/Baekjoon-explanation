import sys
input = sys.stdin.readline
A,B,V = map(int,input().strip().split(" "))

oneday = (A-B)
target = (V-B)
if target%oneday != 0:
    print(target//oneday +1)
else:
    print(target//oneday)