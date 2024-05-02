import sys
bowl,change_num = map(int,sys.stdin.readline().rstrip().split()) #공의 갯수와 바꿀 횟수

bowl_list = [i for i in range(1,bowl+1)] #공의 갯수만큼 리스트 생성

for n in range(change_num):
    a,b = map(int,sys.stdin.readline().rstrip().split())
    bowl_list[a-1],bowl_list[b-1] = bowl_list[b-1],bowl_list[a-1]


print(' '.join(map(str,bowl_list)))