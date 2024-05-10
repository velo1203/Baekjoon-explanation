import sys
nums = int(sys.stdin.readline())

users = []
for n in range(nums):
    age,name = sys.stdin.readline().split()
    users.append([age,name])

for usr in sorted(users,key=lambda x: int(x[0])):
    print(usr[0],usr[1])