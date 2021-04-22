import sys

INFINITE = int(1e9) # 무한을 의미하는 값

# 노드의 개수 n, 간선의 개수 m 입력
n, m = map(int, input().split())
# 시작 노드 번호 start 입력
start = int(input())
# 노드 정보 리스트 graph 생성
graph = [[] for i in range(n+1)]
# 방문 여부 리스트 visited 생성
visited = [False] * (n + 1)
# 최단 거리 테이블 생성
distance = [INFINITE] * (n + 1)

# graph 입력
for _ in range(m):
    # 출발 노드 a, 목적 노드 b, a~b의 비용 cost
    a, b, cost = map(int, input().split())
    graph[a].append((b, cost))


# 방문하지 않는 노드 중, 최단 거리가 가장 짧은 노드의 번호를 구함
def get_smallest_node():
    # 최단 거리의 최초 값 = 무한
    min_value = INFINITE
    # 최단 거리가 가장 짧은 노드의 인덱스
    index = 0
    for i in range(1, n + 1):
        # 최단 거리 테이블의 값이 현재 최소값보다 작고, 방문한 적이 없는 경우
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    # 시작 노드 초기화
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]
    # 시작 노드를 제회한 전체 n-1개의 노드에 대해 반복
    for i in range(n-1):
        # 현재 최단 거리가 가장 짧은 노드를 꺼내서 방문처리
        now = get_smallest_node()
        visited[now] = True
        # 현재 노드와 연결된 다른 노드를 확인
        for j in graph[now]:
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost

dijkstra(start)

for i in range(1, n + 1):
    if distance[i] == INFINITE:
        print("x")
    else:
        print(distance[i])

