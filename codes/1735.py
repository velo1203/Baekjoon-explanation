import sys
input = sys.stdin.readline


def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

A, B = map(int, input().strip().split())
C, D = map(int, input().strip().split())


lcm = B * D // gcd(B, D)

tA = lcm // B
tC = lcm // D
numerator = A * tA + C * tC
denominator = lcm
common_divisor = gcd(numerator, denominator)
print(numerator // common_divisor, denominator // common_divisor)
