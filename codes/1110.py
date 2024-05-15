import sys
input = sys.stdin.readline

num = input().strip()
original  = int(num)
if len(num) == 1:
    num =  "0"+ num

cycle = 0
while True:
    new = str(int(num[0]) + int(num[-1])) 
    num = num[-1] + new[-1]
    cycle += 1 
    if int(num) == original:
        print(cycle)
        break