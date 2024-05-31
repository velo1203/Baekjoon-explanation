import sys
input = sys.stdin.readline

length = int(input().strip())
for n in range(length): #테스트 케이스

    num = int(input().strip())
    if num == 0 or num ==1:
        print(2)
        continue
    while True:
        isprime = True
        for number in range(2, int(num**0.5) + 1):
            if num % number == 0:
                isprime = False
                break
            
        if isprime:
            print(num)
            break
        
        num += 1
