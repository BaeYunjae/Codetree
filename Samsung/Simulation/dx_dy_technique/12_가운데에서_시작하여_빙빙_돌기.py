## 나의 코드
n = int(input())
grid = [[0] * n for _ in range(n)]

# 거꾸로 돌리기
# 왼쪽, 위, 오른쪽, 아래
dxs, dys = [0, -1, 0, 1], [-1, 0, 1, 0]
dir_num = 0

# 오른쪽 아래부터 시작
x, y = n - 1, n - 1
grid[x][y] = n * n

# 범위 확인
def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

for i in range(n * n - 1, 0, -1):
    # 다음 위치 확인
    nx, ny = x + dxs[dir_num], y + dys[dir_num]
    
    # 나아갈 수 없으면 시계방향 90' 회전
    if not in_range(nx, ny) or grid[nx][ny] != 0:
        dir_num = (dir_num + 1) % 4
     
    # 나아갈 수 있으면 위치 갱신 및 값 저장
    x, y = x + dxs[dir_num], y + dys[dir_num]
    grid[x][y] = i 


for i in range(n):
    for j in range(n):
        print(grid[i][j], end=' ')
    print()

----------------------------------------------------------------
## 정답 코드
n = int(input())
grid = [[0] * n for _ in range(n)]

# 가운데부터 시작
now_x, now_y = n // 2, n // 2

# 이동 방향, 이동 횟수
move_dir, move_num = 0, 1

# 범위 확인
def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

# 이동
def move():
    global now_x, now_y

    # 오른쪽, 위, 왼쪽, 아래
    dxs, dys = [0, -1, 0, 1], [1, 0, -1, 0]
    now_x, now_y = now_x + dxs[move_dir], now_y + dys[move_dir]

# 끝났는지 확인
def end():
    return not in_range(now_x, now_y)

# 숫자는 1부터 시작
cnt = 1

while not end():
    # 현재 방향으로 move_num만큼 이동
    for _ in range(move_num):
        grid[now_x][now_y] = cnt
        cnt += 1

        move()

        # 격자 벗어나면 종료
        if end():
            break
    
    # 방향 전환, 반시계방향 90' 회전
    move_dir = (move_dir + 1) % 4
    # 만약 현재 방향이 왼쪽이나 오른쪽이 된 경우
    # 특정 방향으로 움직여야 할 횟수 1 증가
    if move_dir == 0 or move_dir == 2:
        move_num += 1

for i in range(n):
    for j in range(n):
        print(grid[i][j], end=' ')
    print()
  
