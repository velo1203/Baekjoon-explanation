import sys
input = sys.stdin.readline
N,M = map(int,input().split())
cards = list(map(int,input().strip().split()))

res = []

for l in range(N):
    for i in range(l+1,N):
        for a in range(i+1,N):
            summ = cards[l] + cards[i] + cards[a]
            if summ <= M:
                res.append(summ)

res.sort(reverse=True)
print(res[0])