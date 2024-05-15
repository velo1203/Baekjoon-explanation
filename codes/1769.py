import sys

input = sys.stdin.readline
num = input().strip()

i = 0
while len(num) != 1:
    num = str(sum(list(map(int,list(num)))))
    i += 1

print(i)
if int(num)%3 == 0:
    print("YES")
else:
    print("NO")