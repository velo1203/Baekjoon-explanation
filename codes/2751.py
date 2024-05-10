import sys

N = int(sys.stdin.readline())
nums = []

for _ in range(N):
    num = int(sys.stdin.readline())
    nums.append(num)

nums = sorted(nums)

for n in nums:
    print(n)