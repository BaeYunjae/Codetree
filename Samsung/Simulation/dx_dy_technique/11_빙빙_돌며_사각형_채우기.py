## 나의 코드
n, m = map(int, input().split())
grid = [[0] * m for _ in range(n)]

# 오른쪽, 아래쪽, 왼쪽, 위쪽
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
dir_num = 0  # 오른쪽 시작

# 시작 위치
x, y = 0, 0
grid[x][y] = 'A'
now = ord('A')

# 범위 확인
def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < m

for _ in range(1, n * m):
    # 가능할 때까지 확인
    while True:
        # 현재 방향으로 다음 위치 계산
        nx, ny = x + dxs[dir_num], y + dys[dir_num]

        # 나아갈 수 있으면
        if in_range(nx, ny) and grid[nx][ny] == 0:
            # 위치 갱신
            x, y = nx, ny

            # 현재 알파벳이 Z 이전이면
            if now < ord('Z'):
                # 다음 알파벳으로
                now += 1
            # Z 이후이면
            else:
                # A로 돌아간다
                now = ord('A')

            grid[x][y] = chr(now)
            break
        
        # 나아갈 수 없다면
        else:
            # 시계방향 90` 회전
            dir_num = (dir_num + 1) % 4

for i in range(n):
    for j in range(m):
        print(grid[i][j], end=' ')
    print()

------------------------------------
## 정답 코드
n, m = map(int, input().split())
grid = [[0] * m for _ in range(n)]

# 오른쪽, 아래쪽, 왼쪽, 위쪽
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
dir_num = 0  # 오른쪽 시작

# 시작 위치
x, y = 0, 0
grid[x][y] = 'A'

# 범위 확인
def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < m

for i in range(1, n * m):
    # 가능할 때까지 확인
    while True:
        # 현재 방향으로 다음 위치 계산
        nx, ny = x + dxs[dir_num], y + dys[dir_num]

        # 나아갈 수 있으면
        if in_range(nx, ny) and grid[nx][ny] == 0:
            # 위치 갱신
            x, y = nx, ny
            grid[x][y] = chr((i % 26) + ord('A'))
            break
        
        # 나아갈 수 없다면
        else:
            # 시계방향 90` 회전
            dir_num = (dir_num + 1) % 4

for i in range(n):
    for j in range(m):
        print(grid[i][j], end=' ')
    print()
