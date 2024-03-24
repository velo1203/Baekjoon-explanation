a = input()
(a,b,c) = map(int,a.split())

if a==b==c:
    print(10000 +(a *1000))
elif a==b or a==c or c==b:
    same_num = a if a==b or a==c else b
    print(1000+same_num*100)
else:
    print(max(a,b,c)*100)