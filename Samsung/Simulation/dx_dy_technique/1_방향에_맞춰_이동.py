n = int(input())
dx, dy = [-1, 0, 0, 1], [0, -1, 1, 0]  # 서, 남, 북, 동

x, y = 0, 0

for _ in range(n):
    direction, distance = input().split()
    distance = int(distance)

    if direction == 'W':
        move_dir = 0
    elif direction == 'S':
        move_dir = 1
    elif direction == 'N':
        move_dir = 2
    elif direction == 'E':
        move_dir = 3

    x += dx[move_dir] * distance
    y += dy[move_dir] * distance

print(x, y)
