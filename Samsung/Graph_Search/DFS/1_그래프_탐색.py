## 나의 코드 
# 노드 수, 간선 수
n, m = map(int, input().split())  

# 인접 리스트
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    x, y = map(int, input().split())

    # 양방향이므로 서로 넣어준다.
    graph[x].append(y)
    graph[y].append(x)

# 방문 리스트
visited = [False for _ in range(n + 1)]

def dfs(v):
    global cnt
    for i in graph[v]:
        if not visited[i]:
            # 1번 정점은 제외
            if i != 1:
                cnt += 1
            visited[i] = True
            dfs(i)

cnt = 0
dfs(1)
print(cnt)

----------------------------------------------------------------------------
# 노드 수, 간선 수
n, m = map(int, input().split())  

# 인접 리스트, index를 1번부터 사용하기 위해 n + 1만큼 할당한다.
graph = [[] for _ in range(n + 1)]


# 방문 리스트
visited = [False for _ in range(n + 1)]
cnt = 0

def dfs(v):
    global cnt

    # 해당 정점에서 이어져있는 모든 정점을 탐색한다.
    for i in graph[v]:
        # 아직 간선이 존재하고 방문한 적이 없는 정점에 대해서만 탐색을 진행
        if not visited[i]:
            visited[i] = True
            cnt += 1
            dfs(i)

for _ in range(m):
    x, y = map(int, input().split())

    # 각 정점이 서로 이동이 가능한 양방향 그래프이기 때문에
    # 각 정점에 대한 간선을 각각 저장해준다.
    graph[x].append(y)
    graph[y].append(x)

visited[1] = True
dfs(1)
print(cnt)
