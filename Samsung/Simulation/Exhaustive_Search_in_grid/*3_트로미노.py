n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# 가능한 블럭 모양 (총 6개), 좌측 상단 모서리에 대응시킨다.
shapes = [
    [[1, 1, 0],
    [1, 0, 0],
    [0, 0, 0]],

    [[1, 1, 0],
    [0, 1, 0],
    [0, 0, 0]],
    
    [[1, 0, 0],
    [1, 1, 0],
    [0, 0, 0]],
    
    [[0, 1, 0],
    [1, 1, 0],
    [0, 0, 0]],
    
    [[1, 1, 1],
    [0, 0, 0],
    [0, 0, 0]],
    
    [[1, 0, 0],
    [1, 0, 0],
    [1, 0, 0]],
]

# 주어진 위치에 대하여 가능한 모든 모양을 탐색하여 최대 합 반환
def get_max_sum(x, y):
    max_sum = 0
    for i in range(6):
        is_possible = True
        sum_of_nums = 0
        for dx in range(0, 3):
            for dy in range(0, 3):

                # 블록인지 아닌지 확인
                if shapes[i][dx][dy] == 0:
                    continue

                # 격자를 벗어나는지 확인
                # 왼쪽 위에서 시작하므로 오른쪽이나 아래로 벗어나는지만 확인하면 된다.
                if x + dx >= n or y + dy >= m:
                    is_possible = False
                else:
                    sum_of_nums += grid[x + dx][y + dy]

        if is_possible:
            max_sum = max(max_sum, sum_of_nums)

    return max_sum


ans = 0

# 격자의 각 위치 탐색
for i in range(n):
    for j in range(m):
        ans = max(ans, get_max_sum(i, j))

print(ans)
