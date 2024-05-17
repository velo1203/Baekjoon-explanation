import sys
input = sys.stdin.readline

num = int(input())

li = []

for n in range(num):
    li.append(input().strip().split("X"))

filtered_list = []
for l in li:
    filtered_list.append([item for item in l if item != ''])

for f in   filtered_list:
    nm = 0
    for l in f:
        num = 0
        for i,t in enumerate(l):
            num += i+1

        nm+= num
    print(nm)