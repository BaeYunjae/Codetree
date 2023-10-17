## 나의 코드
n = int(input())

lines = []
for _ in range(n):
    x1, x2 = map(int, input().split())
    lines.append(((x1, 0) , (x2, 1)))

cross = 0
for i in range(n):
    for j in range(n):
        # 자기 자신은 제외
        if j == i:
            continue

        # 첫번째 선분과 두번째 선분
        line1 = lines[i]
        line2 = lines[j]

        # 첫번째 선분의 시작점 x좌표가 두번째 선분의 시작점 x좌표보다 작고
        # 첫번째 선분의 끝점 x좌표가 두번째 선분의 끝점 x좌표보다 크면
        # 교차하므로 교차하는 선분 2개 증가
        if (line1[0][0] < line2[0][0]) and (line1[1][0] > line2[1][0]):
            cross += 2

# 선분의 개수 중 교차하는 선분 뺀 값
ans = n - cross

# 서로 교차하는 선분이 2개 이상이면 뺀 값이 음수가 나올 수 있으므로 
# ans가 음수면 교차하지 않는 선분이 없다는 의미로 0 출력
if ans < 0:
    print(0)
else:
    print(ans)

----------------------------------------------------------------------------------------------------------------------------------------
## 정답 코드
# 변수 선언 및 입력
n = int(input())
lines = [tuple(map(int, input().split())) for _ in range(n)]

ans = 0

# 다른 선분과 겹치지 않는 선분의 수를 구한다.
for i in range(n):
    # i번째 선분이 다른 선분과 겹치지 않는지 확인한다.
    overlap = False

    for j in range(n):
        # 자기 자신은 제외한다.
        if j == i:
            continue
        
        # x1이 큰 쪽이 x2가 더 작다면 겹치게 된다.
        if (lines[i][0] <= lines[j][0] and lines[i][1] >= lines[j][1]) or (lines[i][0] >= lines[j][0] and lines[i][1] <= lines[j][1]):
            overlap = True
            break

    # 겹치지 않았다면 정답의 개수에 하나를 추가한다.
    if not overlap:
        ans += 1

print(ans)
