import sys
x,y = map(int,sys.stdin.readline().rstrip().split())
li = list(map(int,sys.stdin.readline().rstrip().split()))
mapped = list(filter(lambda a: a < y, li))
print(' '.join(map(str,mapped)))