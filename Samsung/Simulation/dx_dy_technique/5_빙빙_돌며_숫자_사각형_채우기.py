n, m = map(int, input().split())
answer = [[0] * m for _ in range(n)]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < m

# 우, 하, 좌, 상
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]  
x, y = 0, 0                  # 시작 위치
dir_num = 0                  # 0: 우, 1: 하, 2: 좌, 3: 상

# 초기값
answer[x][y] = 1

for i in range(2, n * m + 1):
    nx, ny = x + dxs[dir_num], y + dys[dir_num]

    if not in_range(nx, ny) or answer[nx][ny] != 0:
        dir_num = (dir_num + 1) % 4

    x, y = x + dxs[dir_num], y + dys[dir_num]
    answer[x][y] = i

for i in range(n):
    for j in range(m):
        print(answer[i][j], end=' ')
    print()
