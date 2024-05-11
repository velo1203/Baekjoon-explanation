while True:
    a,b,c = map(int,input().split())
    if a == 0 and b == 0 and c == 0:
        break
    li = [a,b,c]
    ma = max(li)
    li.remove(ma)
    if sum((a, b, c)) - max((a, b, c)) <= max((a, b, c)) :
        print("Invalid")
    elif a == b ==c:
        print("Equilateral")
    elif a ==b or b ==c or c == a:
        print("Isosceles")
    elif a != b and b != c and c != a:
        print("Scalene")
