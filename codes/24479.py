import sys

input = sys.stdin.readline
N, M, start = map(int, input().split())
graph = {}

mat = [0]*N


def dfs(graph,start):
    visited = set()
    stack = [start]
    idx = 0
    while stack:
        num = stack.pop()
        if num not in visited:
            idx+=1
            mat[num-1] = idx
            visited.add(num)
            stack.extend(sorted(graph[num],reverse=True))

for num in range(1, N + 1):
    graph[num] = []

# 간선 추가
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)  # 양방향 간선이므로 반대 방향도 추가

dfs(graph,start)
for m in mat:
    print(m)