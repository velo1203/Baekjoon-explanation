num = int(input())


def factorial(n):
    # 기본 조건: n이 0이거나 1일 때
    if n == 0 or n == 1:
        return 1
    # 재귀 호출: n * (n-1)의 팩토리얼
    else:
        return n * factorial(n - 1)

# 함수 호출 예시
print(factorial(num))  # 출력: 120
