import sys
input = sys.stdin.readline

ma = 10000
isprime = [False] + [True] * (ma+1)
isprime[1] = False
for n in range(2,int(ma**0.5)+1):
    if isprime[n]:
        j = 2
        while j*n <= ma:
            isprime[j*n] = False
            j +=1
primenum = set()
for i,t in enumerate(isprime):
    if t == True:
        primenum.add(i)

T = int(input())
for _ in range(T):
    number = int(input())
    temp = number//2

    while temp > 0:
        if temp in primenum:
            if number-temp in primenum:
                print(temp,number-temp)
                break
        temp -=1