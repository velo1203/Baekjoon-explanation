import sys
input = sys.stdin.readline

while True:
    li = list(map(int,input().split()))
    if li == [0,0,0]:
        break
    li.sort(reverse=True)
    if li[0] ** 2 == li[1] ** 2 + li[2] **2:
        print("right")
    else:
        print("wrong")