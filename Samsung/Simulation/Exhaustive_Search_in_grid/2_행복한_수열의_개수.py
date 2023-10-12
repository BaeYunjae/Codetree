## 나의 코드
# 격자 크기, 연속 숫자의 수
n, m = map(int, input().split())

grid  = [list(map(int, input().split())) for _ in range(n)]

ans = 0

# 행에서 행복한 수열의 수
for row in range(n):
    # 동일 원소에 자기 자신도 포함
    cnt = 1
    prev_col = 0
    for col in range(n):
        # 이전 열의 값이 현재 값과 같다면
        if prev_col == grid[row][col]:
            cnt += 1
        else:
            cnt = 1

        # 이전 열의 값 갱신
        prev_col = grid[row][col]    

        if cnt >= m:
            ans += 1
            break

# 열에서 행복한 수열의 수
for col in range(n):
    # 동일 원소에 자기 자신도 포함
    cnt = 1
    prev_row = 0
    for row in range(n):
        # 이전 행의 값이 현재 값과 같다면
        if prev_row == grid[row][col]:
            cnt += 1
        else:
            cnt = 1
        
        # 이전 행의 값 갱신
        prev_row = grid[row][col]

        if cnt >= m:
            ans += 1
            break

print(ans)

-----------------------------------------------------------------
## 정답 코드
# 격자 크기, 연속 숫자의 수
n, m = map(int, input().split())

# 격자
grid  = [list(map(int, input().split())) for _ in range(n)]

# 연속 숫자 확인 리스트
seq = [0 for _ in range(n)]


# 주어진 seq가 행복한 수열인지 판단하는 함수
def is_happy_sequence():
    # 연속 횟수, 최대 연속 횟수
    consecutive_count, max_ccnt = 1, 1  
    for i in range(1, n):

        # 수열 리스트 이전 값이 현재 값과 같다면
        if seq[i - 1] == seq[i]:
            # 연속 횟수 증가
            consecutive_count += 1

        # 아니면 연속 횟수 초기화
        else:
            consecutive_count = 1

        max_ccnt = max(max_ccnt, consecutive_count)

    # 최대로 연속한 횟수가 m이상이면 True 반환
    return max_ccnt >= m

# 행복한 수열 개수
num_happy = 0

# 먼저 가로로 행복한 수열의 수를 센다.
for i in range(n):
    seq = grid[i][:]

    if is_happy_sequence():
        num_happy += 1

# 세로로 행복한 수열의 수를 센다.
for j in range(n):
    # 세로로 숫자들을 모아 새로운 수열을 만든다.
    for i in range(n):
        # 같은 열, 다른 행
        seq[i] = grid[i][j]
        
    if is_happy_sequence():
        num_happy += 1

print(num_happy)
