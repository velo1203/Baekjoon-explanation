import sys
num = int(sys.stdin.readline())
totoal = list(map(int, sys.stdin.readline().split()))
find = int(sys.stdin.readline())

print(totoal.count(find))