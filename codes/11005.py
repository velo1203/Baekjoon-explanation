import sys
input = sys.stdin.readline

num,formation = map(int,input().strip().split(" "))
nums = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
txt = []

while num:
    txt.append(nums[num % formation])
    num = num//formation

print("".join(reversed(txt)))