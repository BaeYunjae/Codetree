## 나의 코드
import sys
INI_MAX = sys.maxsize

# 거리 계산 함수
def dist(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

n = int(input())

# 체크포인트 리스트
points = []
for _ in range(n):
    x, y = map(int, input().split())
    points.append((x, y))
    
ans = INI_MAX
for i in range(1, n - 1):
    # 거리의 합
    total = 0
    # 건너 뛸 포인트 좌표와 인덱스 저장 후 삭제
    tmp_point, tmp_index = points[i], points.index(points[i]) 
    points.remove(tmp_point)
    # 모든 포인트들 간의 거리 합 구하기, 포인트를 하나 건너 뛰었으므로 n - 2까지 확인
    for j in range(n - 2):
        total += dist(points[j][0], points[j][1], points[j + 1][0], points[j + 1][1])

    ans = min(ans, total)
    # 건너 뛰었던 포인트 원래대로 놓려놓기
    points.insert(tmp_index, tmp_point)

print(ans)

-----------------------------------------------------------------------------------------
## 정답 코드
import sys
INI_MAX = sys.maxsize

# 변수 선언 및 입력
n = int(input())
points = [list(map(int, input().split())) for _ in range(n)]
    
# 각 i번째 체크포인트를 건너 뛰었을 때의 거리를 구해준다.
ans = INI_MAX
for i in range(1, n - 1):
    # 거리를 구한다.
    dist = 0
    prev_idx = 0
    for j in range(1, n):
        if j == i:
            continue
        dist += abs(points[prev_idx][0]- points[j][0]) + abs(points[prev_idx][1] - points[j][1])
        prev_idx = j

    ans = min(ans, dist)
    
print(ans)
