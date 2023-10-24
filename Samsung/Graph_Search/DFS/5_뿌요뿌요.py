## 나의 코드 (Runtime: 164ms, Memory: 26MB)
n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]

# 격자 벗어나는지 확인
def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

# 갈 수 있는 위치인지 확인
def can_go(x, y):

    if not in_range(x, y):
        return False

    if visited[x][y]:
        return False

    return True


def dfs(x, y):
    global block_cnt

    # 상, 하, 좌, 우
    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]

    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy

        # 갈 수 있는 위치이고, 다음 숫자가 같은 숫자인 경우 방문
        if can_go(nx, ny) and grid[nx][ny] == grid[x][y]:
            visited[nx][ny] = 1
            block_cnt += 1
            dfs(nx, ny)

boom = 0
max_block_cnt = 0
for i in range(n):
    for j in range(n):
        
        # 새로운 블럭 탐색
        block_cnt = 1

        if can_go(i, j):
            visited[i][j] = 1
            dfs(i, j)

        # 블럭의 수가 4개 이상인 경우 터지는 블럭 수 1 증가
        if block_cnt >= 4:
            boom += 1

        # 현재 블럭의 수가 기존의 최대 블럭의 수보다 클 경우 갱신
        if max_block_cnt < block_cnt:
            max_block_cnt = block_cnt

print(boom, max_block_cnt)

-------------------------------------------------------------------------------
## 정답 코드 (Runtime: 214ms, Memory: 26MB)
# 변수 선언 및 입력
n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[False for _ in range(n)] for _ in range(n)]

max_block, bomb_cnt = 0, 0
curr_block_num = 0

# 탐색하는 위치가 격자 범위 내에 있는지 여부 반환한다.
def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

# 탐색하는 위치로 움직일 수 있는지 여부 반환한다.
def can_go(x, y, color):
    if not in_range(x, y):
        return False

    if visited[x][y] or grid[x][y] != color:
        return False

    return True


def dfs(x, y):
    global curr_block_num

    # 상, 하, 좌, 우
    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]

    # 네 방향 각각에 대하여 DFS 탐색을 한다.
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy

        # 갈 수 있는 위치이고, 다음 숫자가 같은 숫자인 경우 방문
        if can_go(nx, ny, grid[x][y]):
            visited[nx][ny] = True
            curr_block_num += 1
            dfs(nx, ny)

# 격자의 각 위치에서 탐색을 시작할 수 있는 경우
# 한 블럭에 대한 DFS 탐색을 수행한다.
for i in range(n):
    for j in range(n):
        if not visited[i][j] and grid[i][j]:
            # 해당 블럭을 방문할 수 있는 경우 visited 배열을 갱신하고
            # 새로운 블럭을 탐색한다는 의미로 curr_block_num을 1로 갱신한다.
            visited[i][j] = True
            curr_block_num = 1

            dfs(i, j)

            # 한 블럭 묶음에 대한 탐색이 끝난 경우 답을 갱신
            if curr_block_num >= 4:
                bomb_cnt += 1

            max_block = max(max_block, curr_block_num)

print(bomb_cnt, max_block)
