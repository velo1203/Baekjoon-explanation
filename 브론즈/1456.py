length = input()
nums = input()

nums = list(map(int, nums.split()))
maxnum = max(nums)
result = 0
for n in nums:
    result += n/maxnum*100

result = result/len(nums)

print(result)