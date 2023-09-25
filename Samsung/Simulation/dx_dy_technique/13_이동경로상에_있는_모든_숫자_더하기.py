n, t = map(int, input().split())
s = input()
nums = [list(map(int, input().split())) for _ in range(n)]

# 북, 동, 남, 서
dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]

# 가운데 위치에서 북쪽으로 시작
x, y = n // 2, n // 2
dir_num = 0

# 범위 확인
def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

# 가운데 위치 값부터 합
ans = nums[x][y]

for i in s:
    # 왼쪽으로 90' 방향 전환
    if i == 'L':
        dir_num = (dir_num - 1 + 4) % 4
    # 오른쪽으로 90' 방향 전환
    elif i == 'R':
        dir_num = (dir_num + 1) % 4
    else:
        # 다음 위치 계산
        nx, ny = x + dxs[dir_num], y + dys[dir_num]
        # 범위 안에 있으면 합
        if in_range(nx, ny):
            x, y = nx, ny
            ans += nums[x][y]
    
print(ans)
