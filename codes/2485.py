import sys
input = sys.stdin.readline
def gcd(A,B):
    while True:
        if A % B == 0:
            break
        A,B=B,A%B
    return B



length = int(input())
li = []
for _ in range(length):
    n = int(input())
    li.append(n)

seq = []
for idx,l in enumerate(li):
    if idx == 0:
        continue
    seq.append(l-li[idx-1])

gc = seq[0]
for idx,se in enumerate(seq):
    if idx == 0:
        continue
    gc = gcd(gc,se)

c = 0
for s in seq:
    c += s //gc -1
print(c)