import sys
input = sys.stdin.read

# 여러 줄 입력 처리
data = input().split()
M = int(data[0])
N = int(data[1])

# 에라토스테네스의 체 초기화
array = [True] * (N + 1)
array[0], array[1] = False, False  # 0과 1은 소수가 아님

# 에라토스테네스의 체로 소수 찾기
for i in range(2, int(N**0.5) + 1):
    if array[i]:
        for j in range(i * i, N + 1, i):
            array[j] = False

# M 이상 N 이하의 소수 리스트 생성
primes = [i for i in range(M, N + 1) if array[i]]

# 결과 출력
if primes:
    print(sum(primes))
    print(min(primes))
else:
    print(-1)
