num = int(input())
def factorial(n):
    # 기저 조건: n이 0 또는 1일 때 팩토리얼은 1이다.
    if n == 0 or n == 1:
        return 1
    # 재귀 조건: n * factorial(n-1)
    else:
        return n * factorial(n - 1)

print(factorial(num))