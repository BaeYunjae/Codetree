## 나의 코드 (Runtime: 119ms, Memory: 25MB)
n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

ans = 10e9

for i in range(n):
    for j in range(i + 1, n):
        for k, (x, y) in enumerate(points):
        	# 첫번째 점
            if k == i:
                x1, y1 = x, y
            # 두번째 점
            if k == j:
                x2, y2 = x, y
    
        # print((x1, y1), (x2, y2))
        dist_square = (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)
        ans = min(ans, dist_square)

print(ans)

----------------------------------------------------------------------
## 정답 코드 (Runtime: 162ms, Memory: 72MB)
n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

# 두 점 사이의 거리의 제곱 값을 반환한다.
def dist(i, j):
    x1, y1 = points[i]
    x2, y2 = points[j]
    return (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)

# 모든 쌍에 대해서 거리 제곱값을 계산하여
# 그 중 최솟값을 찾는다.
min_dist = 10e9
for i in range(n):
    for j in range(i + 1, n):
        min_dist = min(min_dist, dist(i, j))

print(min_dist)

        
