import sys
input = sys.stdin.readline

length = int(input())
for n in range(length): #테스트 케이스

    num = n
    while True:
        isprime = True
        for number in range(2,int(num**0.5) + 1):
            if num%number != 0:
                isprime = False
                break
            
        num+=1
        if isprime == True:
            print(number)
            break
        