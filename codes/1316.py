import sys,re

input = sys.stdin.readline

num = int(input())

nums = 0
for n in range(num):
    txt = input().strip()
    segments = re.findall(r'(.)\1*', txt)
    isOkay = True
    for s in segments:
        if segments.count(s) > 1:
            isOkay = False
            break

    if isOkay == True:
        nums += 1

print(nums)