## 나의 코드
import sys
INI_MAX = sys.maxsize

from collections import deque

n = int(input())
personnel = deque([int(input()) for _ in range(n)])

ans = INI_MAX

for i in range(n):
    dist = 0
    for j in range(1, n):
        dist += personnel[j] * j

    personnel.rotate(-1)
    ans = min(ans, dist)

print(ans)

-----------------------------------------------------
## 정답 코드
import sys
INI_MAX = sys.maxsize

# 변수 선언 및 입력
n = int(input())
personnel = [int(input()) for _ in range(n)]

ans = INI_MAX

for i in range(n):
    sum_dist = 0
    for j in range(n):
        dist = (j + n - i) % n
        '''
        3번 방에서 시작, i = 2
        1번 방과의 거리 : j = 0, (0 + 5 - 2) % 5 = 3 
        2번 방과의 거리 : j = 1, (1 + 5 - 2) % 5 = 4
        3번 방과의 거리 : j = 2, (2 + 5 - 2) % 5 = 0
        4번 방과의 거리 : j = 3, (3 + 5 - 2) % 5 = 1
        5번 방과의 거리 : j = 4, (4 + 5 - 2) % 5 = 2
        '''
        sum_dist += personnel[j] * dist

    ans = min(ans, sum_dist)

print(ans)
