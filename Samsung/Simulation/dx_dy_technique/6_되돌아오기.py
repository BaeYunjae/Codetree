## 나의 코드
dxs, dys = [-1, 0, 0, 1], [0, -1, 1, 0]  # W, S, N, E

# 서, 남, 북, 동 
mapper = {
    'W': 0,
    'S': 1,
    'N': 2,
    'E': 3
}

n = int(input())
x, y = 0, 0       # 시작 위치
cnt = 0           # 걸린 시간 count

for _ in range(n):
    _dir, move_dis = input().split()
    move_dis = int(move_dis)
    dir_num = mapper[_dir]
    for _ in range(move_dis):                      # 이동 거리만큼
        x, y = x + dxs[dir_num], y + dys[dir_num]  # 이동 방향으로 이동
        cnt += 1                                   # 이동하면 count 1 증가
        if x == 0 and y == 0:                      # 시작 위치에 오면
            break                                  # 나가기
    if x == 0 and y == 0:                          
        break                                      # 나가기
    
if x == 0 and y == 0:  # 시작 위치면 
    print(cnt)         # 시간 출력
else:                  # 아니면
    print(-1)          # -1 출력
  
--------------------------------------------------------------------------
## 정답 코드
dxs, dys = [-1, 0, 0, 1], [0, -1, 1, 0]  # W, S, N, E

n = int(input())
x, y = 0, 0       # 시작 위치
ans = -1          # 답 저장
now_time = 0      # 현재까지 걸린 시간

# dir 방향으로 dist 만큼 이동하는 함수
# 시작 위치에 도달하면 True 반환
def move(dir_num, dist):
    global x, y
    global ans, now_time

    for _ in range(dist):
        x, y = x + dxs[dir_num], y + dys[dir_num]
        
        # 이동 시간 저장
        now_time += 1

        # 시작 위치로 다시 돌아오면, 답 갱신
        if x == 0 and y == 0:
            ans = now_time
            return True
        
    return False


for _ in range(n):
    move_dir, dist = input().split()
    dist = int(dist)

    if move_dir == 'W':
        dir_num = 0
    elif move_dir == 'S':
        dir_num = 1
    elif move_dir == 'N':
        dir_num = 2
    else:
        dir_num = 3

    # 주어진 방향대로 dist 만큼 위치 이동
    done = move(dir_num, dist)

    # 시작 위치 도달했다면 종료
    if done:
        break

print(ans)
