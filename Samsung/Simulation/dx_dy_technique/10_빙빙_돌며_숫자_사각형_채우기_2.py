## 나의 코드
# 행 길이, 열 길이
n, m = map(int, input().split())

# 시작 위치
x, y = 0, 0
grid = [[0] * m for _ in range(n)]

# (0, 0)에서 1부터 시작
grid[x][y] = 1

# 아래, 오른쪽, 위, 왼쪽
dxs, dys = [1, 0, -1, 0], [0, 1, 0, -1] 
dir_num = 0

# 격자에서 벗어났는지 확인
def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < m

for i in range(2, n * m + 1):
    # 다음 위치 계산
    x, y = x + dxs[dir_num], y + dys[dir_num]
    
    # 범위를 벗어났거나 이미 값이 있는 경우
    if not in_range(x, y) or grid[x][y] != 0:
        # 이전 위치로 돌아왔다가
        x, y = x - dxs[dir_num], y - dys[dir_num]
        # 방향을 바꿔주고
        dir_num = (dir_num + 1) % 4
        # 다시 다음 위치 계산
        x, y = x + dxs[dir_num], y + dys[dir_num]
    
    # 값은 2부터 격자 크기까지
    grid[x][y] = i

# 출력
for i in range(n):
    for j in range(m):
        print(grid[i][j], end=' ')
    print()

---------------------------------------------
## 정답 코드
# 행 길이, 열 길이
n, m = map(int, input().split())

# 시작 위치
x, y = 0, 0
grid = [[0] * m for _ in range(n)]

# (0, 0)에서 1부터 시작
grid[x][y] = 1

# 아래, 오른쪽, 위, 왼쪽
dxs, dys = [1, 0, -1, 0], [0, 1, 0, -1] 
dir_num = 0

# 격자에서 벗어났는지 확인
def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < m

for i in range(2, n * m + 1):
    # 나아갈 수 있을 때까지 방향을 바꿔가며 확인
    while True:
        # 현재 방향 기준 다음 위치 값 계산
        nx, ny = x + dxs[dir_num], y + dys[dir_num]
        
        # 나아갈 수 있으면
        if in_range(nx, ny) and grid[nx][ny] == 0:
            # 위치 갱신, 배열에 값 저장
            x, y = nx, ny
            grid[x][y] = i
            break
        
        # 나아갈 수 없으면
        else:
            # 반시계방향 90` 회전
            dir_num = (dir_num + 1) % 4

# 출력
for i in range(n):
    for j in range(m):
        print(grid[i][j], end=' ')
    print()
