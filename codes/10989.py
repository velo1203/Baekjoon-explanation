import sys
input = sys.stdin.readline
arr = [0]*10001


num = int(input())
for _ in range(num):
    num = int(sys.stdin.readline())
    arr[num] += 1 # arr[num]에 num이 들어온 개수 count 
for n in range(10001):
    if arr[n] != 0:
        for j in range(arr[n]):
            print(n)

#카운팅 정렬(Counting Sort)은 정수나 정수로 표현 가능한 데이터를 정렬하는데 유용한 알고리즘입니다.
#  이 알고리즘은 비교 기반 정렬 알고리즘이 아니며, 
# 원소들의 범위가 비교적 좁을 때 효율적으로 동작합니다. 
# 카운팅 정렬의 기본 아이디어는 데이터의 값을 키로 사용하여,
# 해당 키의 발생 빈도를 카운트한 다음 이를 이용해 정렬하는 것입니다.