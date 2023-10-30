## 나의 코드
from collections import deque

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

visited = [[0] * m for _ in range(n)]

q = deque()

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < m

def can_go(x, y):
    if not in_range(x, y):
        return False
    if visited[x][y] or grid[x][y] == 0:
        return False
    return True

def bfs():
    # 상, 하, 좌, 우
    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]
    
    while q:
        x, y = q.popleft()

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy

            if can_go(nx, ny):
                visited[nx][ny] = 1
                q.append((nx, ny))


q.append((0, 0))
visited[0][0] = 1
bfs()

# 우측 하단까지 도달했으면 탈출 가능
if visited[n - 1][m - 1]:
    print(1)
else:
    print(0)

-------------------------------------------------
## 정답 코드
from collections import deque

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

visited = [[False for _ in range(m)] for _ in range(n)]

q = deque()

# 주어진 위치가 격자를 벗어나는지 여부 반환
def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < m

# 주어진 위치로 이동할 수 있는지 여부 확인
# 격자를 벗어나지 않고, 뱀이 없고, 방문하지 않았으면 된다.
def can_go(x, y):
    return in_range(x, y) and grid[x][y] and not visited[x][y]

def bfs():
    # 상, 하, 좌, 우
    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]
    
    # queue에서 남은 것이 없을 때까지 반복
    while q:
        # queue에서 가장 먼저 들어온 원소를 뺀다.
        x, y = q.popleft()

        # queue에서 뺀 원소의 위치를 기준으로 4방향 확인
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy

            # 아직 방문한 적이 없으면서 갈 수 있는 곳이라면
            # 새로 queue에 넣어주고 방문 여부 표시
            if can_go(nx, ny):
                q.append((nx, ny))
                visited[nx][ny] = True

# bfs를 이용해 최소 이동 횟수를 구한다.
# 시작점을 queue에 넣고 시작
q.append((0, 0))
visited[0][0] = True

bfs()

# 우측 하단을 방문한 적이 있는지 여부 출력
ans = 1 if visited[n - 1][m - 1] else 0
print(ans)
