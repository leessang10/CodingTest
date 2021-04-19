
def dfs(x, y):
    #범위 초과시 종료
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    #현재 노드를 방문하지 않은 경우
    if graph[x][y] == 0:
        #현재 노드를 방문했다고 표시
        graph[x][y] == 1
        #좌측 노드 방문
        dfs(x-1, y)
        #우측 노드 방문
        dfs(x+1, y)
        #상측 노드 방문
        dfs(x, y+1)
        #하측 노드 방문
        dfs(x, y-1)
        return True
    return False

#공백을 기준으로 N, M 입력받음
n, m = map(int, input().split())
#nxm 인 그래프 graph 입력 받음
graph = []
for i in range(n):
    graph = list(map(int, input()))

#0을 가진 도메인의 갯수를 나타낼 result
result = 0

for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1

print(result)