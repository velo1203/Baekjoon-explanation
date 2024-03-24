total = int(input())
length = int(input())
total_price = 0
for n in range(length):
    a = input()
    (price,count) = map(int,a.split())
    total_price += price*count

if total_price==total:
    print("Yes")
else:
    print("No")