import sys
input = sys.stdin.readline

length = int(input())
people = list(map(int,input().strip().split()))
seq = sorted(people,reverse=True)
space = []
for idx,n in enumerate(people):
    space.append(n)
    if n == seq[-1]:
        space.pop()
        seq.pop()
    if len(space) != 0:
        while space and space[-1] == seq[-1]:
            space.pop()
            seq.pop()

if space == seq:
    print("Nice")
else:
    print("Sad")