import sys
input = sys.stdin.readline

num,seq = map(int,input().strip().split())
li = []
for n in range(1,num+1):
    if num % n == 0:
        li.append(n)

if len(li) < seq:
    print(0)
else:
    print(li[seq-1])