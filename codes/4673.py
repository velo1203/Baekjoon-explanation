li = [False] + [True]*10000

for num in range(1,10001):
    divid = list(map(int,list(str(num))))
    a = num+sum(divid)
    if a > 10000:
        continue
    li[a] = False

for idx,l in enumerate(li):
    if l == True:
        print(idx)