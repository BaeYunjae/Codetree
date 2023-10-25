## 나의 코드 (Runtime: 146ms, Memory: 25MB)
# 사람 수, 치즈 수, 치즈 먹은 기록 수, 아픈 기록 수
n, m, d, s = map(int, input().split())

# (몇 번째 사람, 몇 번째 치즈, 몇 초)
ate = [tuple(map(int, input().split())) for _ in range(d)]

# (몇 번째 사람, 몇 초)
sick = [tuple(map(int, input().split())) for _ in range(s)]

# 시간 포함한 치즈 먹은 사람 리스트와 시간을 제외한 치즈 먹은 사람 리스트
cheese = [[] for _ in range(m + 1)]
non_time_cheese = [[] for _ in range(m + 1)]
for p, c, t in ate:
    cheese[c].append((p, t))
    non_time_cheese[c].append(p)

# 각 치즈별 사람 확인 리스트
cheese_check = [True for _ in range(m + 1)]

spoil = []
for i in range(1, m + 1):

    # 치즈 먹은 사람이 아픈 사람보다 적으면 continue
    if len(cheese[i]) < s:
        continue

    for k in range(s):
        # print(i, sick[k][0])
        # 아픈 사람이 치즈 먹은 사람 리스트에 없으면 치즈별 사람 확인 리스트 False
        if sick[k][0] not in non_time_cheese[i]:
            cheese_check[i] = False
            break
        
    for j in range(len(cheese[i])):
        for k in range(s):
            # 치즈 먹은 사람이 아픈 사람과 같을 때 
            # 치즈 먹은 시간이 아픈 시간보다 늦다면 break
            if cheese[i][j][0] == sick[k][0]:
                if cheese[i][j][1] >= sick[k][1]:
                    cheese_check[i] = False
                    break

    # 각 치즈별 사람 확인 리스트가 True이면 상한 치즈에 차즈 리스트 넣기 
    if cheese_check[i]:
        spoil.append(cheese[i])

# print(spoil)

# 시간을 제외한 상한 치즈를 먹었을 사람 리스트
person = [[] for _ in range(len(spoil))]
for i in range(len(spoil)):
    for j in range(len(spoil[i])):
        # 한 치즈를 여러 번 먹은 사람이 있으므로
        # 사람 리스트에 없는 사람일 경우 추가
        if spoil[i][j][0] not in person[i]:
            person[i].append(spoil[i][j][0])

# print(person)


ans = 0

# 상한 치즈별 사람 리스트 중 최대 길이가 
# 아플 수 있는 최대 사람의 수
for p in person:
    if ans <= len(p):
        ans = len(p)

print(ans)

---------------------------------------------------------------------------
## 정답 코드 (Runtime: 138ms, Memory: 73MB)
# 클래스 선언
class Info1:
    def __init__(self, p, m, t):
        self.p, self.m, self.t = p, m, t

class Info2:
    def __init__(self, p, t):
        self.p, self.t = p, t

# 변수 선언 및 입력
n, m, d, s = map(int, input().split())

# 치즈를 먹은 기록
info1 = []
for _ in range(d):
    p, x, t = map(int, input().split())
    info1.append(Info1(p, x, t))

# 아픈 사람 기록
info2 = []
for _ in range(s):
    p, t = map(int, input().split())
    info2.append(Info2(p, t))

ans = 0

# 하나의 치즈가 상했을 때 필요한 약의 수의 최댓값을 구한다.
for i in range(1, m + 1):
    # i번째 치즈가 상했을 때 필요한 약의 수를 구한다.

    # 우선 i번째 치즈가 상했다고 가정할 때 모순이 발생하지 않는지 확인한다.
    # time 배열을 만들어 각 사람이 언제 치즈를 먹었는지 저장한다.
    time = [0] * (n + 1)
    for info in info1:
        # i번째 치즈에 대한 정보가 아닌 경우 넘어간다.
        if info.m != i:
            continue

        # person이 i번째 치즈를 처음 먹었거나
        # 이전보다 더 빨리 먹게 된 경우 time배열을 갱신한다.
        person = info.p
        if time[person] == 0:
            time[person] = info.t
        elif time[person] > info.t:
            time[person] = info.t

    # possible : i번째 치즈가 상했을 수 있으면 true, 아니면 false
    possible = True

    for info in info2:
        # person이 i번째 치즈를 먹지 않았거나
        # i번째 치즈를 먹은 시간보다 먼저 아픈 경우 모순이 생긴다.
        person = info.p
        if time[person] == 0:
            possible = False
        if time[person] >= info.t:
            possible = False

    # 만약 i번째 치즈가 상했을 가능성이 있다면, 몇 개의 약이 필요한지 확인한다.
    pill = 0
    if possible:
        # 한번이라도 i번째 치즈를 먹은 적이 있다면, 약이 필요하다.
        for j in range(1, n + 1):
            if time[j] != 0:
                pill += 1
                
    # 약의 최댓값
    ans = max(ans, pill)

print(ans)
