## 나의 코드 (Runtime: 274ms, Memory: 26MB)
n = int(input())
points = [list(map(int, input().split())) for _ in range(n)]

# 세 점 중 두 점이 x축 평행과 y축 평행하는지 확인
def parallel(x1, y1, x2, y2, x3, y3):
    if (x1 == x2 and y2 == y3) or (x1 == x2 and y1 == y3) or (x1 == x3 and y1 == y2) \
        or (x1 == x3 and y3 == y2) or (x2 == x3 and y2 == y1) or (x2 == x3 and y3 == y1):
        return True
    return False

# 삼각형 만들어서 넓이 구하기
def make_triangle(a, b, c):
    s = 0
    for i, (x, y) in enumerate(points):
        if i == a:
            x1, y1 = x, y
        if i == b:
            x2, y2 = x, y
        if i == c:
            x3, y3 = x, y
    
    if parallel(x1, y1, x2, y2, x3, y3):
        s = 0.5 * abs((x1 * y2 + x2 * y3 + x3 * y1) - (x2 * y1 + x3 * y2 + x1 * y3))

    return s

max_area = 0
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            area = make_triangle(i, j, k)
            max_area = max(max_area, area)

print(int(max_area * 2))

-------------------------------------------------------------------------------------------------
## 정답 코드 (Runtime: 216ms, Memory: 73MB)
n = int(input())
points = [list(map(int, input().split())) for _ in range(n)]

# 삼각형의 넓이에 2를 곱한 값을 반환한다.
def area(x1, y1, x2, y2, x3, y3):
    return abs((x1 * y2 + x2 * y3 + x3 * y1) - (x2 * y1 + x3 * y2 + x1 * y3))


# 3개의 점을 모두 골라보면서
# 조건을 만족하는 경우 중
# 최대 넓이를 계산한다.
max_area = 0
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            # x값이 같은 쌍과 y값이 같은 쌍이 있는 경우에만
            # 최대 넓이를 계산한다.
            x1, y1 = points[i]
            x2, y2 = points[j]
            x3, y3 = points[k]
            if (x1 == x2 or x1 == x3 or x2 == x3) and \
                (y1 == y2 or y1 == y3 or y2 == y3):
                max_area = max(max_area, area(x1, y1, x2, y2, x3, y3))

print(max_area)
