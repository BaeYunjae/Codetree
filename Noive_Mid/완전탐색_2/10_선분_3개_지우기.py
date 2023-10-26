## 나의 코드 (Runtime: 124ms, Memory: 25MB)
n = int(input())
lines = [tuple(map(int, input().split())) for _ in range(n)]

def check_overlapped(l1, l2, l3):
    count = [0] * 100

    for i in range(n):
        # 선분이 제거할 선분 중의 하나라면 continue
        if i in [l1, l2, l3]:
            continue

        # 남아있는 선분이라면 count 표시
        x1, x2 = lines[i]
        for j in range(x1, x2 + 1):
            count[j] += 1

    # count 배열을 돌며 1보다 클 경우 겹치는 것으로 보고
    # overlap을 True로 변경
    overlap = False
    for i in range(100):
        if count[i] > 1:
            overlap = True
            break
        
    return overlap


ans = 0
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            # 3개의 선분 제거 후 남은 선분들이 겹치지 않으면
            # 경우의 수 증가
            if not check_overlapped(i, j, k):
                ans += 1

print(ans)

-------------------------------------------------------------
## 정답 코드 (Runtime: 166ms, Memory: 25MB)
MAX_A = 100

# 변수 선언 및 입력
n = int(input())
section = [tuple(map(int, input().split())) for _ in range(n)]

# 3개의 선분을 모두 골라보면서
# 모두 겹쳐지지 않도록 하는 가짓수를 구한다.
ans = 0
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            # i, j, k번 선분을 제외했을 때
            # 모든 선분이 겹치지 않으면 정답을 1 추가한다.

            # overlap : 모든 선분이 겹치지 않으면 False
            overlap = False
            arr = [0] * (MAX_A + 1)

            for x in range(n):
                # 제외한 3개의 선분이면 넘어간다.
                if x == i or x == j or x == k:
                    continue

                for y in range(section[x][0], section[x][1] + 1):
                    arr[y] += 1

            for x in range(MAX_A + 1):
                if arr[x] > 1:
                    overlap = True

            if overlap == False:
                ans += 1

print(ans)            
