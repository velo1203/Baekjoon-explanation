import sys

testcase = int(sys.stdin.readline().rstrip())
for _ in range(testcase):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    print(x + y)