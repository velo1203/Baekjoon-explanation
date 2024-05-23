import sys
input = sys.stdin.readline

def eratosthenes_sieve(N):
    is_prime = [True] * (N + 1)
    is_prime[0] = is_prime[1] = False  

    p = 2
    while p * p <= N:
        if is_prime[p]:
            for multiple in range(p * p, N + 1, p):
                is_prime[multiple] = False
        p += 1
    return is_prime



mat = eratosthenes_sieve(123456*2)

while True:
    a = int(input())
    if a==0:
        break

    print(mat[a+1:a*2+1].count(True))