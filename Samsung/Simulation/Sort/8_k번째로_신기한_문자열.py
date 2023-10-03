## 나의 코드
n, k, T = input().split()
n = int(n)
k = int(k)

ls = []
for _ in range(n):
    s = input()
    if s[:len(T)] == T:
        ls.append(s)

ls.sort()

print(ls[k - 1])

------------------------------------------------------
## 정답 코드
n, k, T = input().split()
n, k = int(n), int(k)

# a가 b로 시작하는지 확인
def starts_with(a, b):
    # b의 길이가 더 길 수 없다.
    if len(a) < len(b):
        return False

    # b의 길이까지 봤을 때 a와 문자열이 동일한지 확인
    return a[:len(b)] == b

ls = []
for _ in range(n):
    s = input()
    if starts_with(s, T):
        ls.append(s)

ls.sort()

print(ls[k - 1])
