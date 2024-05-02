import sys
input = sys.stdin.readline

ran = int(input())
for _ in range(ran):
    r,s = input().strip().split(" ")
    for n in s:
        print(n*int(r),end="")
    print()
