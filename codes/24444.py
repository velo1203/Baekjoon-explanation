import sys
from collections import deque
input = sys.stdin.readline
N, M, start = map(int, input().split())
mat = [0]*N
def bfs(graph, start):
    # BFS를 위한 큐를 생성하고 시작 정점을 큐에 추가합니다.
    queue = deque([start])
    # 방문한 정점을 추적하기 위한 집합을 생성합니다.
    visited = set()
    # 시작 정점을 방문한 것으로 표시합니다.
    visited.add(start)
    while queue:
        # 큐에서 정점을 하나 꺼냅니다.
        vertex = queue.popleft()

        # 현재 정점의 모든 인접 정점을 확인합니다.
        for neighbor in sorted(graph[vertex]):
            if neighbor not in visited:
                # 인접 정점을 방문한 것으로 표시하고 큐에 추가합니다.
                visited.add(neighbor)
                queue.append(neighbor)

graph = {}

for num in range(1, N + 1):
    graph[num] = []

# 간선 추가
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)  # 양방향 간선이므로 반대 방향도 추가

bfs(graph,start)
print(mat)