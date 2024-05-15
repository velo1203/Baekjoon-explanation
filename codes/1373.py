import sys

input = sys.stdin.readline

num = list(input().strip())
num.reverse()

result = []

for n in range(0,len(num),3):
    section = num[n:n+3]
    res = 0
    for i,sec in enumerate(section):
        res += int(sec) * (2**i)

    result.append(str(res))

result.reverse()

print("".join(result))