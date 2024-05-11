import sys
input = sys.stdin.readline

num = int(input())

seq = 0
order = 0

for n in range(num):
    seq += (n+1)
    if num <= seq:
        order = n+1
        break

c = seq-num
if order % 2 == 0:
    idx = order-c-1
    for n in range(order):
        if n == idx:
            print(f"{1+n}/{order-n}")
else:
    for n in range(order):
        if n == c:
            print(f"{1+n}/{order-n}")