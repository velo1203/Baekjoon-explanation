import sys

input = sys.stdin.readline
N, M, start = map(int, input().split())
graph = {}

for num in range(1, N + 1):
    graph[num] = []

# 간선 추가
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)  # 양방향 간선이므로 반대 방향도 추가
