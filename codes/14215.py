li = list(map(int,input().split()))

li.sort(reverse=True)
a,b,c = li

if a >= b + c:
    a = b + c -1


print(a+b+c)