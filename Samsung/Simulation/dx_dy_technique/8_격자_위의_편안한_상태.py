## 나의 코드
n, m = map(int, input().split())
grid = [[0] * n for _ in range(n)]

# 위, 아래, 오른쪽, 왼쪽
dxs, dys = [-1, 1, 0, 0], [0, 0, 1, -1] 

# 계산한 좌표가 범위 내에 있는지 확인
def in_range(x, y):
    if 0 <= x and x < n and 0 <= y and y < n:
        return True
    return False

# 위, 아래, 양옆으로 색칠 확인
def check(x, y):
    color = 0
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if in_range(nx, ny) and grid[nx][ny] == 1:
            color += 1

    # 색칠된 부분이 3개이면 true 반환
    if color == 3:
        return True
    return False

for _ in range(m):
    r, c = map(int, input().split())
    r -= 1
    c -= 1
    grid[r][c] = 1

    # 3개이면 1 출력, 아니면 0 출력
    if check(r, c):
        print(1)
    else:
        print(0)

----------------------------------------------------
## 정답 코드
n, m = map(int, input().split())
grid = [[0] * n for _ in range(n)]

# 위, 아래, 오른쪽, 왼쪽
dxs, dys = [-1, 1, 0, 0], [0, 0, 1, -1] 

# 계산한 좌표가 범위 내에 있는지 확인
def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

# 위, 아래, 양옆으로 색칠 확인
def check(x, y):
    color = 0
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if in_range(nx, ny) and grid[nx][ny] == 1:
            color += 1

    # 색칠된 부분 반환
    return color

for _ in range(m):
    r, c = map(int, input().split())
    r -= 1
    c -= 1
    grid[r][c] = 1

    # 3개이면 1 출력, 아니면 0 출력
    if check(r, c) == 3:
        print(1)
    else:
        print(0)
