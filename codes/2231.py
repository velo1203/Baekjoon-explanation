import sys
input =sys.stdin.readline

num = int(input())

t = 1
while True:
    decomposeSum = sum(map(int,list(str(t))))
    if t + decomposeSum == num:
        print(t)
        break
    elif t == num:
        print(0)
        break
    else:
        t+=1