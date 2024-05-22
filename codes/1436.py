N = int(input())
c = 0
res = 666
while True:
    if "666" in str(res):
        c +=1
    if c == N:
        print(res)
        break

    res +=1 