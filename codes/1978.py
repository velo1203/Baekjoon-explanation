import sys
input = sys.stdin.readline

length = int(input())

nums = list(map(int,input().strip().split()))
count = 0
for n in nums:
    li = []
    for a in range(1,n+1):
        if n % a == 0:
            li.append(a)

    if len(li) == 2:
        count += 1


print(count)