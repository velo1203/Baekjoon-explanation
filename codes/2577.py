import sys
input = sys.stdin.readline

a = int(input())
b = int(input())
c = int(input())
num = str(a * b* c)

li = []
for n in range(10):
    li.append(num.count(str(n)))

for l in li:
    print(l)