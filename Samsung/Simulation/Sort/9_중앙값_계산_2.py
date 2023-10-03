## 나의 코드 (Runtime: 69ms)
n = int(input())
nums = list(map(int, input().split()))

ls = []
for i in range(n):
    ls.append(nums[i])
    ls.sort()
    if i % 2 == 0:
        print(ls[i//2], end=' ')

------------------------------------------
## 정답 코드 (Runtime: 75ms)
n = int(input())
nums = list(map(int, input().split()))

# 홀수 번째 수 지날 때마다 정렬 진행한 후 가운데 값 출력
for i in range(n):
    if i % 2 == 0:
        # 오름차순 정렬
        sorted_nums = sorted(nums[:i + 1])
        print(sorted_nums[i//2], end=' ')
