## 나의 코드
n, k = map(int, input().split())
bomb = [int(input()) for _ in range(n)]

# 폭발 폭탄이 없으면 -1
ans = -1
for i in range(n):
    # 현재 폭탄 번호
    a = bomb[i]
    for j in range(i + 1, n):
        # 비교할 폭탄 번호
        b = bomb[j]

        # 현재 폭탄과 같은 번호라면 거리를 구한다.
        if a == b:
            dist = j - i
            # 거리가 k 이내이면서 현재까지 저장된 폭발 폭탄보다 번호가 크면 갱신
            if dist <= k and ans < a:
                ans = a

print(ans)

----------------------------------------------------------------------------------
## 정답 코드
n, k = map(int, input().split())
bomb = [int(input()) for _ in range(n)]

# 폭발 폭탄이 없으면 -1
ans = -1

# 모든 쌍에 대해서 터질 수 있는 폭탄을 찾고
# 그 중 번호가 최대인 값을 찾는다.
for i in range(n):
    for j in range(i + 1, n):
        # 거리가 k를 초과하는 경우 넘어간다.
        if j - i > k:
            break

        # 두 폭탄의 번호가 다른 경우 터지지 않는다.
        if bomb[i] != bomb[j]:
            continue

        ans = max(ans, bomb[i])

print(ans)
