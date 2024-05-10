nums = []
for n in range(9):
    nums.append(int(input()))

print(max(nums), nums.index(max(nums))+1)