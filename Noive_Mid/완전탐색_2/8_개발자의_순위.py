## 나의 코드 (Runtime: 125ms, Memory: 28MB)
k, n = map(int, input().split())

# 경기별 순위
ranking = [tuple(map(int, input().split())) for _ in range(k)]

# 개발자별 순위
cnt = [[0] * (n + 1) for _ in range(k)]
for i in range(k):
    for j in range(n):
        num = ranking[i][j]
        cnt[i][num] = j + 1

ans = 0
for i in range(1, n + 1):
    for j in range(1, n + 1):

        # 새로운 개발자와 비교하면 현재가 비교보다 높은 경기 수 초기화
        immut = 0

        for m in range(k):
            if j == i:
                continue
            
            # 현재 개발자보다 비교하는 개발자 순위가 더 높을 경우 
            # 다음 경기로
            if cnt[m][i] > cnt[m][j]:
                continue

            immut += 1

        # 현재가 비교하는 개발자 순위보다 높은 경기가 총 경기 수와 같으면
        # 불변의 순위로 정답 1 증가
        if immut == k:
            ans += 1

print(ans)

--------------------------------------------------------------------------
## 정답 코드 (Runtime: 149ms, Memory: 28MB)
# 변수 선업 및 입력
k, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(k)]

ans = 0

# 모든 쌍에 대해서 불변의 순위인 쌍을 찾는다.
for i in range(1, n + 1):
    for j in range(1, n + 1):
        # i번 개발자가 j번 개발자보다 항상 높은 순위인지 여부를 확인한다.

        # i와 j가 같을 경우 넘어간다.
        if i == j:
            continue

        # correct: i번 개발자가 j번 개발자보다 항상 높은 순위일 때 true
        correct = True

        # k번의 모든 경기에 대해서 두 개발자의 위치를 찾고,
        # 하나라도 i번 개발자가 더 뒤에 있으면 correct를 false로 바꾼다.
        for lists in arr:
            index_i = lists.index(i)
            index_j = lists.index(j)

            if index_i > index_j:
                correct = False
        
        if correct:
            ans += 1

print(ans)
            
