n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Step 1 #
# 첫번째 격자를 놓는다. (i, j)
max_cnt = 0
for i in range(n):
    # 격자를 벗어나지 않을 범위로만 잡는다.
    for j in range(n - 2):
        # 두 번째 격자를 놓는다. (k, l)
        for k in range(n):
            for l in range(n - 2):
                # Step 2 #  <------------------------------------------------------------ 이 부분을 놓침
                # 두 격자가 겹치는 경우에는 패스
                # 격자가 같은 줄에 있을 수 있으니 j와 l의 차가 3보다 작으면 겹치는 것
                if i == k and abs(j - l) <= 2:
                    continue
                
                # Step 3 #
                # 두 격자가 겹치지 않는 경우 동전 수 세어 갱신
                cnt1 = grid[i][j] + grid[i][j + 1] + grid[i][j + 2]
                cnt2 = grid[k][l] + grid[k][l + 1] + grid[k][l + 2]
                max_cnt = max(max_cnt, cnt1 + cnt2)

print(max_cnt)
