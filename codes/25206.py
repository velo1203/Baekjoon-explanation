import sys

input = sys.stdin.readline

lev = {
    "A+":4.5,
    "A0":4.0,
    "B+":3.5,
    "B0":3.0,
    "C+":2.5,
    "C0":2.0,
    "D+":1.5,
    "D0":1.0,
    "F":0.0,
}

total_num = 0
total_point = 0
for n in range(20):
    t = input().strip().split(" ")
    num = float(t[1])
    level = t[2]
    if level == "P":
        continue

    point = lev[level]
    total_num += num
    total_point += num*point

print(round(total_point/total_num,6))