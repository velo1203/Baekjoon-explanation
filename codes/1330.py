a = input()
(a,b) = map(int,a.split())

if a > b:
    print(">")
elif a < b:
    print("<")
else:
    print("==")