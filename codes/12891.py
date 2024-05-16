import sys
input = sys.stdin.readline

# 입력 읽기
S, M = map(int, input().strip().split())
txt = input().strip()
checklist = list(map(int, input().strip().split()))

# 변수 초기화
txtlist = [0] * 4
count = 0

# 첫 번째 윈도우의 문자 개수 계산
for i in range(M):
    if txt[i] == 'A':
        txtlist[0] += 1
    elif txt[i] == 'C':
        txtlist[1] += 1
    elif txt[i] == 'G':
        txtlist[2] += 1
    elif txt[i] == 'T':
        txtlist[3] += 1

# 첫 번째 윈도우가 조건을 만족하는지 확인
if (txtlist[0] >= checklist[0] and txtlist[1] >= checklist[1] and 
    txtlist[2] >= checklist[2] and txtlist[3] >= checklist[3]):
    count += 1

# 나머지 문자열에 대해 윈도우 슬라이딩
for n in range(1, S - M + 1):
    # 윈도우에서 벗어나는 문자 처리
    end_char = txt[n - 1]
    if end_char == 'A':
        txtlist[0] -= 1
    elif end_char == 'C':
        txtlist[1] -= 1
    elif end_char == 'G':
        txtlist[2] -= 1
    elif end_char == 'T':
        txtlist[3] -= 1

    # 윈도우에 새로 들어오는 문자 처리
    start_char = txt[n + M - 1]
    if start_char == 'A':
        txtlist[0] += 1
    elif start_char == 'C':
        txtlist[1] += 1
    elif start_char == 'G':
        txtlist[2] += 1
    elif start_char == 'T':
        txtlist[3] += 1

    # 현재 윈도우가 조건을 만족하는지 확인
    if (txtlist[0] >= checklist[0] and txtlist[1] >= checklist[1] and 
        txtlist[2] >= checklist[2] and txtlist[3] >= checklist[3]):
        count += 1

# 결과 출력
print(count)
