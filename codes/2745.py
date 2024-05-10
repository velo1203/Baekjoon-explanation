from string import ascii_uppercase
import sys
aList = list(ascii_uppercase)
input = sys.stdin.readline

num, formation = input().strip().split(" ")
formation = int(formation)

nums = []
for i,n in enumerate(reversed(list(num))):
    if n.isdecimal() == True:
        nums.append(int(n) * (formation**i))
    else:
        number = aList.index(n)+ 10
        nums.append(int(number) * (formation**i))

print(sum(nums))