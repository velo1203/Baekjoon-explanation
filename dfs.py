def dfs(graph, start):
    # 방문한 노드를 기록하는 집합
    visited = set()
    # 탐색을 위한 스택
    stack = [start]
    
    while stack:
        # 스택에서 노드를 꺼내옴
        node = stack.pop()
        if node not in visited:
            # 노드를 방문함
            print(node)
            visited.add(node)
            # 인접 노드들을 스택에 추가
            # 역순으로 추가하여 스택의 특성(후입선출, LIFO) 때문에
            # 올바른 순서로 탐색이 됨
            stack.extend(reversed(graph[node]))

# 예제 그래프
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# 시작 노드 'A'로 DFS 수행
dfs(graph, 'A')
