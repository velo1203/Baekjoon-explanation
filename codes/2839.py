import sys
input = sys.stdin.readline

num = int(input())
se = []
for n in range(num//3+1):
    for i in range(num//5+1):
        if 3*n + 5*i == num:
            se.append(n+i)
        elif 3*n + 5*i > num:
            continue    

if len(se) == 0:
    print(-1)
else:
    print(min(se))