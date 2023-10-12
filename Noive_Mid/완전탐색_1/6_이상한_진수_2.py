## 나의 코드
a = list(input())
n = len(a)

# 0이 있을 때 
if '0' in a:
    for i in range(n):
        if a[i] == '0':
            a[i] = '1'
            break

# 0이 없을 때
else:
    a[-1] = '0'

answer = 0
for i in range(n):
    answer += int(a[i]) * (2 ** ((n - 1) - i))

print(answer)

------------------------------------------------
## 정답 코드
import sys
MIN = -sys.maxsize

# 변수 선언 및 입력
binary = list(map(int, input()))
length = len(binary)

# 각 i번째 자릿수를 바꾸었을 때의 십진수 값을 구해준다.
ans = MIN
for i in range(length):
    # i번째 자릿수를 바꾼다.
    binary[i] = 1 - binary[i]

    # 십진수로 변환한다.
    num = 0
    for j in range(length):
        num = num * 2 + binary[j]
        '''  
        (binary, j, num)
        [1, 1, 1, 0] 0 1
        [1, 1, 1, 0] 1 3
        [1, 1, 1, 0] 2 7
        [1, 1, 1, 0] 3 14
        '''
    
    ans = max(ans, num)

    # i번째 자릿수를 원래대로 돌려놓는다.
    binary[i] = 1 - binary[i]

print(ans)
