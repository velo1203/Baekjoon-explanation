def gcd(A,B):
    while True:
        c = A % B
        if c == 0:
            break
        A = B
        B = c
    return B