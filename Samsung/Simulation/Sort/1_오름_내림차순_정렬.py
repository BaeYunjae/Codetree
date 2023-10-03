## sorted()
n = int(input())
nums = list(map(int, input().split()))
print(*sorted(nums))
print(*sorted(nums)[::-1])

----------------------------------------
## sort()
n = int(input())
nums = list(map(int, input().split()))
nums.sort()
print(*nums)
nums.sort(reverse=True)
print(*nums)
