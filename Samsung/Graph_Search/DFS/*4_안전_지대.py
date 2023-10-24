## 나의 코드 (Runtime: 1150ms, Memory: 118MB)
import sys
sys.setrecursionlimit(2500)

n, m = map(int, input().split())
houses = [list(map(int, input().split())) for _ in range(n)]

# k의 최댓값 = 집 높이의 최댓값
max_k = max(max(houses))

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < m

def can_go(x, y, k):
    # 격자를 벗어나면 False
    if not in_range(x, y):
        return False
    
    # 집 높이가 k보다 작거나 같으면 또는 이미 방문한 위치면 False
    if houses[x][y] <= k or visited[x][y]:
        return False 

    return True

def dfs(x, y, k):

    # 상, 하, 좌, 우
    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]

    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy

        if can_go(nx, ny, k):
            visited[nx][ny] = 1
            dfs(nx, ny, k)


max_area = 0
ans_k = 1
for k in range(1, max_k + 1):
    num_of_area = 0
    visited = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):

            # 갈 수 있는 좌표면 방문 표시
            if can_go(i, j, k):
                visited[i][j] = 1
                num_of_area += 1
                dfs(i, j, k)
				
                # 현재 최대 영역의 수보다 큰 경우 갱신
                if max_area < num_of_area:
                    max_area, ans_k = num_of_area, k


print(ans_k, max_area)
-----------------------------------------------------------
## 정답 코드 (Runtime: 2033ms, Memory: 166MB)
import sys
sys.setrecursionlimit(2500)

# 변수 선언 및 입력
n, m = map(int, input().split())
houses = [list(map(int, input().split())) for _ in range(n)]

# 방문 리스트
visited = [[False for _ in range(m)] for _ in range(n)]

# 안전 영역의 수
zone_num = 0


# visited 배열을 초기화해준다.
def initialize_visited():
    for i in range(n):
        for j in range(m):
            visited[i][j] = False


# 주어진 위치가 격자를 벗어나는지 여부 반환한다.
def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < m


# 주어진 위치로 이동할 수 있는지 여부 확인한다.
def can_go(x, y, k):
    if not in_range(x, y):
        return False
    
    if visited[x][y] or houses[x][y] <= k:
        return False

    return True


def dfs(x, y, k):
    # 상, 하, 좌, 우
    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]

    # 네 방향 각각에 대하여 DFS 탐색
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy

        if can_go(nx, ny, k):
            visited[nx][ny] = True
            dfs(nx, ny, k)


def get_zone_num(k):
    global zone_num

    # 새로운 탐색을 시작한다는 의미로 zone_num를 0으로 갱신하고
    # visited 배열을 초기화해준다.
    zone_num = 0
    initialize_visited()

    # 격자의 각 위치에 대하여 탐색을 시작할 수 있는 경우
    # 해당 위치로부터 시작한 DFS 탐색 수행
    for i in range(n):
        for j in range(m):
            if can_go(i, j, k):
                # 해당 위치를 탐색할 수 있는 경우 visited 배열을 갱신하고
                # 안전 영역을 하나 추가해준다.
                visited[i][j] = True
                zone_num += 1

                dfs(i, j, k)

# 가능한 안전 영역의 최솟값이 0이므로 다음과 같이 초기화할 수 있다.
max_zone_num = -1
ans_k = 0
max_height = 100

# 각 가능한 비의 높이에 대하여 안전 영역의 수를 탐색한다.
for k in range(1, max_height + 1):
    get_zone_num(k)

    # 기존의 최대 영역의 수보다 클 경우 이를 갱신하고 인덱스를 저장한다.
    if zone_num > max_zone_num:
        max_zone_num, ans_k = zone_num, k

print(ans_k, max_zone_num)
