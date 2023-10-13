## 나의 코드 (Runtime: 118ms, Memory: 25MB)
n = int(input())
nums = [input() for _ in range(n)]

def extend_num(num):
    return '0' * (max_len - len(num)) + num

not_carry = -10e9
for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            sum_of_digits = ''
            # 숫자의 최대 길이 찾기
            max_num = max(int(nums[i]), int(nums[j]), int(nums[k]))
            max_len = len(str(max_num))
            
            # 숫자 확장하기
            num1, num2, num3 = extend_num(nums[i]), extend_num(nums[j]), extend_num(nums[k])

            # 각 자리수 더하기
            for d in range(max_len):
                each_digit = int(num1[d]) + int(num2[d]) + int(num3[d])
                # 자릿수 합이 10 이상이면 자릿수 합 초기화 후 다음 조합으로
                if each_digit >= 10:
                    sum_of_digits = ''
                    break
                sum_of_digits += str(each_digit)
            
            if sum_of_digits and not_carry < int(sum_of_digits):
                not_carry = int(sum_of_digits)

if not_carry < 0:
    print(-1)
else:
    print(not_carry)

-----------------------------------------------------------------------------------------------
## 정답 코드 (Runtime: 139ms, Memory: 24MB)
n = int(input())
nums = [int(input()) for _ in range(n)]

# 모든 쌍을 다 잡아본다.
ans = -1
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            carry = False

            # 일의 자리에서 carry 발생
            if nums[i] % 10 + nums[j] % 10 + nums[k] % 10 >= 10:
                carry = True
            
            # 십의 자리에서 carry 발생
            if nums[i] % 100 // 10 + nums[j] % 100 // 10 + nums[k] % 100 // 10 >= 10:
                carry = True

            # 백의 자리에서 carry 발생
            if nums[i] % 1000 // 100 + nums[j] % 1000 // 100 + nums[k] % 1000 // 100 >= 10:
                carry = True

            # 천의 자리에서 carry 발생
            if nums[i] % 10000 // 1000 + nums[j] % 10000 // 1000 + nums[k] % 10000 // 1000 >= 10:
                carry = True

            if carry == False:
                ans = max(ans, nums[i] + nums[j] + nums[k])

print(ans)
