from collections import deque


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
        print(vertex, end=' ')  # 방문한 정점을 출력합니다.

        # 현재 정점의 모든 인접 정점을 확인합니다.
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                # 인접 정점을 방문한 것으로 표시하고 큐에 추가합니다.
                visited.add(neighbor)
                queue.append(neighbor)


graph = {
    '1': ['2', '3','4'],
    '2': ['4'],
    '3': ['4'],
    '4': [],
}

# 시작 노드 'A'로 DFS 수행
bfs(graph, '1')
