## 나의 코드
# 시작
x, y = 0, 0

# 동, 남, 서, 북
dxs, dys = [1, 0, -1, 0], [0, -1, 0, 1]

# 시작은 북쪽
dir_num = 3

ans = -1
time = 0

# 시작점으로 돌아왔는지 확인
def check(x, y):
    if x == 0 and y == 0:
        return True
    return False

for n in input():
	# 직진
    if n == 'F':
        x, y = x + dxs[dir_num], y + dys[dir_num]  # 이동하면서
        time += 1                                  # 시간 1 증가
    # 왼쪽으로 90' 회전    
    elif n == 'L':
        dir_num = (dir_num - 1 + 4) % 4            # 회전하면서
        time += 1                                  # 시간 1 증가
    # 오른쪽으로 90' 회전
    elif n == 'R':                 
        dir_num = (dir_num + 1) % 4                # 회전하면서
        time += 1                                  # 시간 1 증가

	# 시작점으로 돌아왔으면
    if check(x, y):
        ans = time      # 답에 시간 저장
        break
    
# 시작점으로 안 돌아왔으면 그대로 -1 출력
# 시작점으로 돌아왔으면 시간 출력
print(ans)

-----------------------------------------------------------------
## 정답 코드
# 시작
x, y = 0, 0

# 동, 남, 서, 북
dxs, dys = [1, 0, -1, 0], [0, -1, 0, 1]

# 시작은 북쪽
dir_num = 3

# 입력
dirs = input()
n = len(dirs)

# 시작점으로 돌아왔는지 여부
flag = False

for i in range(n):
    c_dir = dirs[i]
    # 직진
    if c_dir == 'F':
        x, y = x + dxs[dir_num], y + dys[dir_num]
    # 왼쪽으로 90' 회전
    elif c_dir == 'L':
        dir_num = (dir_num - 1 + 4) % 4
    # 오른쪽으로 90' 회전
    elif c_dir == 'R':
        dir_num = (dir_num + 1) % 4

    # 시작점으로 되돌아왔을 때
    if x == 0 and y == 0:
        print(i + 1)
        flag = True
        break

# 시작점으로 되돌아오지 못했을 때
if not flag:
    print(-1)
