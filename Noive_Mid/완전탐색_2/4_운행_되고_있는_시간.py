## 나의 코드
n = int(input())
workers = [tuple(map(int, input().split())) for _ in range(n)]

ans = -10e9
for i in range(n):
    count = [0] * 1001
    time = 0
    for j, (s, e) in enumerate(workers):
  		# i번째는 건너뜀
        if j == i:
            continue
        
        # 일하는 시간에 해당하는 인덱스 증가, 끝나는 시간은 포함되지 않음
        for k in range(s, e):
            count[k] += 1
	
    # 일하는 시간을 모두 더함
    for l in range(1001):
        if count[l] >= 1:
            time += 1
            
    ans = max(ans, time)

print(ans)

---------------------------------------------------------------
## 정답 코드
MAX_NUM = 1000

# 변수 선언 및 입력
n = int(input())
workers = [tuple(map(int, input().split())) for _ in range(n)]

ans = 0

# 빼야하는 직원을 정한다.
for i in range(n):
    # i번 직원의 구간을 제외한 나머지 구간에서
    # 운행되고 있는 시간을 구한다.

    count = [0] * MAX_NUM

    for j, (s, e) in enumerate(workers):
        # i번째 구간은 제외한다.
        if j == i:
            continue
        
        # 모든 구간을 카운팅한다.
        for k in range(s, e):
            count[k] += 1

    
    time = 0

    for l in range(1, MAX_NUM):
        if count[l] >= 1:
            time += 1

    # 운행되고 있는 시간 중 최댓값을 구한다.            
    ans = max(ans, time)

print(ans)
