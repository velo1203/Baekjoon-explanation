import sys

# 표준 입력 재정의
input = sys.stdin.readline

# 입력 받기
input_string = input().strip()  # 입력 끝의 개행 문자 제거

# 공백으로 문자열 분리 후 각 부분을 뒤집기
a, b = map(lambda x: ''.join(reversed(x)), input_string.split())

# 결과 출력
if int(a) > int(b):
    print(a)
elif int(b) > int(a):
    print(b)