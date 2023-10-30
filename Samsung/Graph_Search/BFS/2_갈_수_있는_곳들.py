## 나의 코드 (289ms)
from collections import deque

n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
start_points = deque([tuple(map(int, input().split())) for _ in range(k)])

visited = [[False] * n for _ in range(n)]

q = deque()
ans = 0

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

def can_go(x, y):
    return in_range(x, y) and grid[x][y]  == 0 and not visited[x][y]

def push(x, y):
    global ans

    # 이미 방문했던 곳이 아니면 ans 증가    
    if not visited[x][y]:
        ans += 1
    visited[x][y] = True
    q.append((x, y))
    

def bfs():
    # 상, 하, 좌, 우
    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]

    while q:
        x, y = q.popleft()

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if can_go(nx, ny):
                push(nx, ny)


# 시작점 위치 큐가 비워질 때까지 bfs 실행
while start_points:
    x, y = start_points.popleft()
    push(x - 1, y - 1)
    bfs()

print(ans)

----------------------------------------------------------------------------
## 정답 코드 (226ms)
from collections import deque

n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# bfs에 필요한 변수
bfs_q = deque()
visited = [[False] * n for _ in range(n)]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

def can_go(x, y):
    return in_range(x, y) and not grid[x][y] and not visited[x][y]    

def bfs():
    # 상, 하, 좌, 우
    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]

    # queue에 남은 것이 없을 때까지 반복
    while bfs_q:
        # queue에서 가장 먼저 들어온 원소를 뺀다.
        x, y = bfs_q.popleft()

        # queue에서 뺀 원소의 위치를 기준으로 4방향을 확인한다.
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy

            # 아직 방문한 적이 없으면서 갈 수 있는 곳이라면
            # 새로 queue에 넣어주고 방문 여부를 표시한다.
            if can_go(nx, ny):
                bfs_q.append((nx, ny))
                visited[nx][ny] = True


# 시작점을 모두 bfs queue에 넣는다.
for _ in range(k):
    x, y = tuple(map(int, input().split()))
    bfs_q.append((x - 1, y - 1))
    visited[x - 1][y - 1] = True

# bfs 진행
bfs()

ans = sum([1 for i in range(n) for j in range(n) if visited[i][j]])
print(ans)
