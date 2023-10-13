## 나의 코드 (Runtime: 112ms, Memory: 25MB)
n = int(input())
nums = list(map(int, input().split()))

INI_MIN = -10e9

ans = INI_MIN
for i in range(n):
    # 인접하지 않으므로 2칸 떨어진 곳부터 더함
    for j in range(i + 2, n):
        sum_num = 0
        sum_num = nums[i] + nums[j]

        # 최댓값과 현재 값을 비교하여 최댓값 갱신
        ans = max(ans, sum_num)

print(ans)

-------------------------------------------------
## 정답 코드 (Runtime: 106ms, Memory: 25MB)
n = int(input())
nums = list(map(int, input().split()))

INI_MIN = -10e9

ans = INI_MIN
for i in range(n):
    # 인접하지 않으므로 2칸 떨어진 곳부터 더함
    for j in range(i + 2, n):
        # 현재 값이 이전 값보다 크면 갱신
        if ans < nums[i] + nums[j]:
            ans = nums[i] + nums[j]

print(ans)
