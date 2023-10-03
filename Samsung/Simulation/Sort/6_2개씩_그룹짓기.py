## 나의 코드
n = int(input())
ls = list(map(int, input().split()))
ls.sort()

MAX = 0
for i in range(n):
    MAX = max(MAX, ls[i] + ls[-1-i])

print(MAX)

----------------------------------------
## 정답 코드
n = int(input())
ls = list(map(int, input().split()))
ls.sort()

group_max = 0
for i in range(n):
    # i번째와 2n - 1 -i번째 원소 매칭
    group_sum = ls[i] + ls[2*n - 1 - i]
    if group_sum > group_max:
        # 최댓값 갱신
        group_max = group_sum

print(group_max)
