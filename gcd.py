def gcd(A,B):
    while True:
        if A % B == 0:
            break
        A,B=B,A%B
    return B