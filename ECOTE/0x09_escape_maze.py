def dfs(x, y):
    # 주어진 범위 m행, n열을 벗어날 경우 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    # 현재 노드를 방문하지 않은 경우
    if graph[x][y] == 1:
        # 방문 완료 처리
        graph[x][y] = 0
        # 동쪽 노드
        dfs(x + 1, y)
        # 서쪽 노드
        dfs(x - 1, y)
        # 남쪽 노드
        dfs(x, y - 1)
        # 북쪽 노드
        dfs(x, y + 1)
        return True
    return False


graph = []

# NxM 배열 입력
n, m = map(int, input().split(" "))
for i in range(n):
    graph.append(list(map(int, input())))

result = 0
#모든 노드에 대해 순회
for i in range(n):
    for j in range(m):
        if dfs(i, j):
            result += 1
print(result)
