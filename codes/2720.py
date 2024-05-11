import sys
input = sys.stdin.readline

length = int(input())
for n in range(length):
    num = int(input())
    print(num//25,end=" ")
    num -= 25*(num//25)
    print(num//10,end=" ")
    num -= 10*(num//10)
    print(num//5,end=' ')
    num -= 5*(num//5)
    print(num//1)