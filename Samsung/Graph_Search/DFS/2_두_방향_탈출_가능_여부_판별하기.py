## 나의 코드
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < m

# 갈 수 있는 좌표인지 확인
def can_go(x, y):

	# 다음 좌표가 격자 안에 있는지 확인
    if not in_range(x, y):
        return False
    
    # 이미 방문했거나 뱀이 있는지 확인
    if visited[x][y] or grid[x][y] == 0:
        return False

    return True

def dfs(x, y):

    # 아래, 오른쪽
    dxs, dys = [1, 0], [0, 1] 

    for dx, dy in zip(dxs, dys):
    	# 다음 좌표
        new_x, new_y = x + dx, y + dy

		# 갈 수 있는 곳이면 방문 처리 후 재귀함수 실행
        if can_go(new_x, new_y):
            visited[new_x][new_y] = 1
            dfs(new_x, new_y)

dfs(0, 0)

# 끝지점 방문했다면 1 출력, 아니면 0 출력
if visited[n - 1][m - 1]:
    print(1)
else:
    print(0)

-------------------------------------------------------------
## 정답 코드1
# 변수 선언 및 입력
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

visited = [[0 for _ in range(m)] for _ in range(n)]

# 주어진 위치가 격자를 벗어나는지 여부를 반환한다.
def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < m

# 주어진 위치로 이동할 수 있는지 여부를 확인한다.
def can_go(x, y):
    if not in_range(x, y):
        return False

    if visited[x][y] or grid[x][y] == 0:
        return False

    return True


def dfs(x, y):
    dxs, dys = [1, 0], [0, 1]

    for dx, dy in zip(dxs, dys):
        new_x, new_y = x + dx, y + dy

        if can_go(new_x, new_y):
            visited[new_x][new_y] = 1
            dfs(new_x, new_y)

visited[0][0] = 1
dfs(0, 0)

print(visited[n - 1][m - 1])

-------------------------------------------------------------
## 정답 코드2
...
...
def dfs(x, y):
    dxs, dys = [1, 0], [0, 1]

    # 탐색 전에 해당 위치를 방문했음을 표시
    visited[x][y] = 1

    for dx, dy in zip(dxs, dys):
        new_x, new_y = x + dx, y + dy

        if can_go(new_x, new_y):
            dfs(new_x, new_y)


dfs(0, 0)

print(visited[n - 1][m - 1])
