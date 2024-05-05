import sys
input = sys.stdin.readline

config = [
    ["A","B","C"],
    ["D","E","F"],
    ["G","H","I"],
    ["J","K","L"],
    ["M","N","O"],
    ["P","Q","R","S"],
    ["T","U","V"],
    ["W","X","Y","Z"]
]

time = 0
txt = list(input().strip())
for t in txt:
    i = 2
    for con in config:
        if t in con:
            time += 2 + (i - 1)
        i += 1

print(time)