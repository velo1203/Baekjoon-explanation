import sys
input = sys.stdin.readline

nums = list(map(int,list(input().strip())))
nums.sort(reverse=True)
for n in nums:
    print(n,end="")