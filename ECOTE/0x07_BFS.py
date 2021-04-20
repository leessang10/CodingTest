from collections import deque


def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=" ")
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


graph = [
    [],         # 0 노드는 없기 때문에 공백
    [2, 3, 8],  # 1 노드에 연결된 노드: 2, 3, 8 노드
    [1, 7],     # 2 노드에 연결된 노드: 1, 7 노드
    [1, 4, 5],  # 3 노드에 연결된 노드: 1, 4, 5 노드
    [3, 5],     # 4 노드에 연결된 노드: 3, 5 노드
    [3, 4],     # 5 노드에 연결된 노드: 3, 4 노드
    [7],        # 6 노드에 연결된 노드: 7 노드
    [2, 6, 8],  # 7 노드에 연결된 노드: 2, 6, 8
    [1, 7]      # 8 노드에 연결된 노드: 1, 7
]
# n 노드의 방문 여부를 나타내는 리스트
# visited[n]이 True이면 n 노드는 방문한 노드
# visited[n]이 False이면 n 노드는 방문하지 않은 노드
visited = [False] * 9

bfs(graph, 1, visited)