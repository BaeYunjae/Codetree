## 나의 코드 (Runtime: 164ms, Memory: 25MB)
n, s = map(int, input().split())
nums = list(map(int, input().split()))

ans = 10e9
for i in range(n):
    for j in range(i + 1, n):
        # 2개의 숫자 따로 저장 후 0으로 초기화
        a, b = nums[i], nums[j]
        nums[i], nums[j] = 0, 0
        
        # 남은 nums 합과 s의 차이 중 최솟값 찾기
        ans = min(ans, abs(s - sum(nums)))

        # 제외된 숫자 원래대로
        nums[i], nums[j] = a, b

print(ans)

-------------------------------------------
## 정답 코드 (Runtime: 118ms, Memory: 25MB)
n, s = map(int, input().split())
nums = list(map(int, input().split()))

nums_sum = 0
ans = 10e9

# 배열의 값들의 총합을 미리 구해둔다.
for num in nums:
    nums_sum += num

for i in range(n):
    for j in range(i + 1, n):
        # i번과 j번 수를 제외할 경우 남은 숫자들의 총합
        new_sum = nums_sum - nums[i] - nums[j]

        diff = abs(new_sum - s)
        ans = min(ans, diff)

print(ans)
