def eratosthenes_sieve(N):
    is_prime = [True] * (N + 1)
    is_prime[0] = is_prime[1] = False  

    p = 2
    while p * p <= N:
        if is_prime[p]:
            for multiple in range(p * p, N + 1, p):
                is_prime[multiple] = False
        p += 1
    primes = [number for number, prime in enumerate(is_prime) if prime]
    return primes

N = 30
print(f"{N}까지의 소수: {eratosthenes_sieve(N)}")
