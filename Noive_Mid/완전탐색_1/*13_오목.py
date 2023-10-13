import sys

board = [list(map(int, input().split())) for _ in range(19)]

def in_range(x, y):
    return 0 <= x and x < 19 and 0 <= y and y < 19

# 왼아, 왼, 왼위, 위, 오위, 오, 오아, 아
dxs, dys = [1, 0, -1, -1, -1, 0, 1, 1], [-1, -1, -1, 0, 1, 1, 1, 0]

# 모든 좌표에서 다 확인
for i in range(19):
    for j in range(19):

        if board[i][j] == 0:
            continue

        for dx, dy in zip(dxs, dys):
            # 현재 바둑돌 수, 현재 행 위치, 현재 열 위치
            curt = 1
            curx = i
            cury = j
            while True:
                nx = curx + dx
                ny = cury + dy

                # 다음 좌표가 격자를 벗어나면 break
                if not in_range(nx, ny):
                    break

                # 다음 바둑돌이 현재 바둑돌과 다르면 break
                if board[nx][ny] != board[i][j]:
                    break

                # 둘 다 아니면, 즉 격자를 벗어나지 않고 현재 바둑돌과 같으면 바둑돌 증가, 현재 위치 갱신
                curt += 1
                curx = nx
                cury = ny

            # 바둑돌이 5개가 되면 그 바둑돌과 가운데 위치 출력
            if curt == 5:
                print(board[i][j])
                print(i + 2 * dx + 1, j + 2 * dy + 1)
                sys.exit()

print(0)
