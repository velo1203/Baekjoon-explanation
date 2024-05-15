import sys
input = sys.stdin.readline

num = int(input())
li =  list(map(int,input().strip().split()))

sorted_unique_X = sorted(set(li))

rank_dict = {value: rank for rank, value in enumerate(sorted_unique_X)}

for n in li:
    print(rank_dict[n],end=" ")