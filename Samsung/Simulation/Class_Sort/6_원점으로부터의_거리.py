## 나의 코드
# 점의 개수
n = int(input())

spots = []
for i in range(1, n + 1):
    x, y = map(int, input().split())
    spots.append((x, y, i))

# 원점과 (x, y) 사이가 가까운 순으로 정렬
spots.sort(key = lambda x: abs(x[0]) + abs(x[1]))

for _, _, num in spots:
    print(num)

-----------------------------------------------------------
## 정답 코드
# 변수 선언 및 입력
n = int(input())
distances = []

# 원점과의 거리 계산 함수
def get_dist_from_origin(x, y):
    return abs(x) + abs(y)

for i in range(n):
    x, y = map(int, input().split())
    # 원점과의 거리와 index 저장
    distances.append((get_dist_from_origin(x, y), i + 1))

distances.sort()

for _, idx in distances:
    print(idx)
