## 나의 코드 (Runtime: 264ms, Memory: 25MB)
n, b = map(int, input().split())
wishes = [tuple(map(int, input().split())) for _ in range(n)]

ans = 0
for i in range(n):
    # 학생들이 원하는 선물의 가격 리스트
    tmp = [list(wishes[j]) for j in range(n)]

    # 선물 한 개를 반값 할인
    tmp[i][0] /= 2

    # (선물 가격 + 배송비) 리스트
    prices = [(tmp[k][0] + tmp[k][1]) for k in range(n)]
    prices.sort()

    # 선물할 수 있는 학생수, 현재까지 쓴 예산
    student = 0
    cnt = 0

    for x in range(n):
        if cnt + prices[x] > b:
            break
        cnt += prices[x]
        student += 1

    ans = max(ans, student)

print(ans)

-------------------------------------------------------------------
## 정답 코드 (Runtime: 172ms, Memory: 25MB)
# 변수 선언 및 입력
n, b = map(int, input().split())
p_arr, s_arr = [], []
for _ in range(n):
    p, s = map(int, input().split())
    p_arr.append(p)
    s_arr.append(s)

ans = 0
# 한 명의 학생에 선물 쿠폰을 쓸 때 선물 가능한 학생의 최대 명수를 구한다.
for i in range(n):
    # i번째 학생의 선물에 쿠폰을 쓸 때 선물 가능한 학생 수를 구한다.

    # tmp배열을 만들어 i번째 학생의 선물에 쿠폰을 쓸 때
    # 각 학생의 원하는 선물 가격을 저장한다.
    tmp = [0] * n
    for j in range(n):
        tmp[j] = p_arr[j] + s_arr[j]
    tmp[i] = p_arr[i] // 2 + s_arr[i]

    # 학생을 선물 가격 순으로 정렬한다.
    # 선물 가격이 가장 작은 학생부터 선물을 사 줄 때,
    # 반드시 가장 많은 학생에게 선물을 줄 수 있다.
    tmp.sort()

    student = 0
    cnt = 0

    # 가장 많은 학생에게 선물을 줄 때, 그 학생 수를 구한다.
    # student : 선물받은 학생 수 / cnt : 현재까지 쓴 돈
    for j in range(n):
        if cnt + tmp[j] > b:
            continue

        cnt += tmp[j]
        student += 1

    ans = max(ans, student)

print(ans)
