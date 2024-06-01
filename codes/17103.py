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
    return [i for i in range(N + 1) if is_prime[i]]

def goldbach_partitions_count(num, primes, prime_set):
    count = 0
    for prime in primes:
        if prime > num // 2:
            break
        if (num - prime) in prime_set:
            count += 1
    return count

# 소수를 1000000까지 구합니다.
max_limit = 1000000
primes = eratosthenes_sieve(max_limit)
prime_set = set(primes)

T = int(input().strip())

for _ in range(T):
    num = int(input().strip())
    count = goldbach_partitions_count(num, primes, prime_set)
    print(count)
