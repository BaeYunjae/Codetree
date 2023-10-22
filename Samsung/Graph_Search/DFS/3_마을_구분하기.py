## 나의 코드
n = int(input())
people = [list(map(int, input().split())) for _ in range(n)]

visited = [[0] * n for _ in range(n)]

# 마을 내 사람 수
cnt = 0

# 사람 수 리스트
residents = []

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

def can_go(x, y):
    if not in_range(x, y):
        return False
    
    if visited[x][y] or people[x][y] == 0:
        return False

    return True

def dfs(x, y):
    global cnt
    # 상, 하, 좌, 우
    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]

    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy

        if can_go(nx, ny):
            visited[nx][ny] = 1
            cnt += 1
            dfs(nx, ny)

for i in range(n):
    for j in range(n):
    	# 위치를 방문할 수 있다면
        if can_go(i, j):
        	# 방문 여부 갱신
            visited[i][j] = 1
           	# 새로운 마을 탐색한다는 의미로 cnt를 1로 갱신
            cnt = 1
            
            dfs(i, j)
            
            # 한 마을 탐색 후 마을 내 사람 수 저장
            residents.append(cnt)

# 마을 수 = 각 마을 내 사람 수 리스트 길이
print(len(residents))

# 각 마을 내 사람 수 오름차순 정렬
residents.sort()
for r in residents:
    print(r)

-------------------------------------------------------------------------------------
## 정답 코드
# 변수 선언 및 입력
n = int(input())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

visited = [
    [False for _ in range(n)]
    for _ in range(n)
]

people_num = 0
people_nums = list()

# 주어진 위치가 격자를 벗어나는지 여부를 반환합니다.
def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n


# 주어진 위치로 이동할 수 있는지 여부를 확인합니다.
def can_go(x, y):
    if not in_range(x, y):
        return False
    
    if visited[x][y] or grid[x][y] == 0:
        return False
    
    return True

def dfs(x, y):
    global people_num
    
    # 0: 오른쪽, 1: 아래쪽, 2: 왼쪽, 3: 위쪽
    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
    
    # 네 방향에 각각에 대하여 DFS 탐색을 합니다.
    for dx, dy in zip(dxs, dys):
        new_x, new_y = x + dx, y + dy
        
        if can_go(new_x, new_y):
            visited[new_x][new_y] = True
            
            #  마을에 존재하는 사람을 한 명 추가해줍니다.
            people_num += 1
            dfs(new_x, new_y)

# 격자의 각 위치에서 탐색을 시작할 수 있는 경우
# 한 마을에 대한 DFS 탐색을 수행합니다.
for i in range(n):
    for j in range(n):
        if can_go(i, j):
            # 해당 위치를 방문할 수 있는 경우 visited 배열을 갱신하고
            # 새로운 마을을 탐색한다는 의미로 people_num을 1으로 갱신합니다.
            visited[i][j] = True
            people_num = 1
            
            dfs(i, j)
            
            # 한 마을에 대한 탐색이 끝난 경우 마을 내의 사람 수를 저장합니다.
            people_nums.append(people_num)

# 각 마을 내 사람의 수를 오름차순으로 정렬합니다.
people_nums.sort()

print(len(people_nums))

for i in range(len(people_nums)):
    print(people_nums[i])
