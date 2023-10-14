## 나의 코드 (Runtime: 122ms, Memory: 25MB)
n, m = map(int, input().split())
strings = [input() for _ in range(n)]

# 왼아, 왼, 왼위, 위, 오위, 오, 오아, 아
dxs, dys = [1, 0, -1, -1, -1, 0, 1, 1], [-1, -1, -1, 0, 1, 1, 1, 0]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < m

# LEE 개수
num_of_LEE = 0
for i in range(n):
    for j in range(m):

        # L부터 시작이므로 L이 아니면 다음 위치로
        if strings[i][j] != 'L':
            continue
        
        for dx, dy in zip(dxs, dys):
            # 문자열 LEE 확인 리스트
            check_LEE = []

            # 현재 위치
            curx = i
            cury = j

            # 확인 리스트에 L 추가, (i, j)는 확인용
            # check_LEE.append(((i, j), 'L'))
            check_LEE.append('L')

            while True:
                nx = curx + dx 
                ny = cury + dy 

                # 다음 위치가 격자를 벗어나면 break
                if not in_range(nx, ny):
                    break

                # 다음 문자가 E일 때 확인 리스트에 E 추가
                if strings[nx][ny] == 'E':
                    # check_LEE.append(((nx, ny), 'E'))
                    check_LEE.append('E')
                    # print(check_LEE)
                    # 확인 리스트 길이가 3이면 LEE로 판단, LEE 개수 증가
                    if len(check_LEE) == 3:
                        num_of_LEE += 1
                        break

                # 다음 문자가 E가 아니면 break
                else:
                    break

                # 현재 위치 갱신
                curx = nx
                cury = ny

print(num_of_LEE)

-------------------------------------------------------------------------
## 정답 코드 (Runtime: 111ms, Memory: 24MB)
n, m = map(int, input().split())
strings = [input() for _ in range(n)]

# 왼아, 왼, 왼위, 위, 오위, 오, 오아, 아
dxs, dys = [1, 0, -1, -1, -1, 0, 1, 1], [-1, -1, -1, 0, 1, 1, 1, 0]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < m

# LEE 개수
cnt = 0
for i in range(n):
    for j in range(m):

        # L부터 시작이므로 L이 아니면 다음 위치로
        if strings[i][j] != 'L':
            continue
        
        for dx, dy in zip(dxs, dys):
            curt = 1
            curx = i
            cury = j
            while True:
                nx = curx + dx
                ny = cury + dy
                if not in_range(nx, ny):
                    break
                if strings[nx][ny] != 'E':
                    break
                curt += 1
                curx = nx
                cury = ny

            if curt >= 3:
                cnt += 1

print(cnt)
        
        
