## 나의 코드 (Runtime: 130ms, Memory: 25MB)
n, t = map(int, input().split())
top = list(map(int, input().split()))
bottom = list(map(int, input().split()))

for _ in range(t):
    # 위 변 마지막, 아래 변 마지막 저장
    tmp1 = top[n - 1]
    tmp2 = bottom[n - 1]

    # 위 변과 아래 변 오른쪽으로 밀기
    for i in range(n - 1, 0, -1):
        top[i] = top[i - 1]
        bottom[i] = bottom[i - 1]

    # 위 변 마지막이 아래 변 처음으로,
    # 아래 변 마지막이 위 변 처음으로 이동
    top[0] = tmp2
    bottom[0] = tmp1

print(*top)
print(*bottom)

---------------------------------------------------------------------------
## 정답 코드 (Runtime: 123ms, Memory: 24MB)
# 변수 선언 및 입력
n, t = map(int, input().split())
u = list(map(int, input().split()))
d = list(map(int, input().split()))

for _ in range(t):
    # Step 1
    # 위에서 가장 오른쪽에 있는 숫자를 따로 temp값에 저장한다.
    temp = u[n - 1]

    # Step 2
    # 위에 있는 숫자들을 완성한다.
    # 오른쪽에서부터 채워넣어야 하며,
    # 맨 왼쪽 숫자는 아래에서 가져와야함에 유의한다.
    for i in range(n - 1, 0, -1):
        u[i] = u[i - 1]
    u[0] = d[n - 1]

    # Step 3
    # 아래에 있는 숫자들을 완성한다.
    # 마찬가지로 오른쪽에서부터 채워넣어햐 하며,
    # 맨 왼쪽 숫자는 위에서 미리 저장했던 temp값을 가져와야함에 유의한다.
    for i in range(n - 1, 0, -1):
        d[i] = d[i - 1]
    d[0] = temp

# 출력
for elem in u:
    print(elem, end=" ")
print()

for elem in d:
    print(elem, end=" ")
