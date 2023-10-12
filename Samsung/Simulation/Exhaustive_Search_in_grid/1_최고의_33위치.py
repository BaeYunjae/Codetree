# 격자 크기
n = int(input())

# 격자
grid = [list(map(int, input().split())) for _ in range(n)]

def get_num_of_coin(row_s, row_e, col_s, col_e):
    num_of_coin = 0

    for row in range(row_s, row_e + 1):
        for col in range(col_s, col_e + 1):
            num_of_coin += grid[row][col]

    return num_of_coin

MAX_coin = 0

for row in range(n):
    for col in range(n):
        # 격자를 벗어나는지 확인
        if row + 2 >= n or col + 2 >= n:
            continue
        
        # 동전 개수 확인
        num_of_coin = get_num_of_coin(row, row + 2, col, col + 2)

        # 동전 최대 개수 
        MAX_coin = max(MAX_coin, num_of_coin)

print(MAX_coin)
