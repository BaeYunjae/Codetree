# 북쪽 시작
dir_num = 3
x, y = 0, 0

# 동, 남, 서, 북
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]

n = input()

for i in n:
    if i == 'L':
        dir_num = (dir_num - 1 + 4) % 4
    elif i == 'R':
        dir_num = (dir_num + 1) % 4
    else:
        x, y = x + dx[dir_num], y + dy[dir_num]

print(x, y)
