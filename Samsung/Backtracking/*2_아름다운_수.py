# 변수 선언 및 입력
n = int(input())
ans = 0
seq = []

def is_beautiful():
    # 연달아 같은 숫자가 나오는 시작 위치를 잡는다.
    i = 0
    while i < n:
        # 만약 연속하여 해당 숫자만큼 나올 수 없다면
        # 아름다운 수가 아니다.
        if i + seq[i] - 1 >= n:
            return False

        # 연속하여 해당 숫자만큼 같은 숫자가 있는지 확인한다.
        # 하나라도 다른 숫자가 있다면 
        # 아름다운 수가 아니다.
        for j in range(i, i + seq[i]):
            if seq[j] != seq[i]:
                return False

        # 연속하여 나오는 숫자만큼 위치를 바로 이동하면 된다.
        # 예를 들어 0 위치에 2가 연속으로 2번 나왔다면
        # 다음 시작 위치는 2가 된다.
        i += seq[i]

    return True


def count_beautiful_seq(cnt):
    global ans

    if cnt == n:
        if is_beautiful():
            ans += 1
        return 

    for i in range(1, 5):
        seq.append(i)
        count_beautiful_seq(cnt + 1)
        seq.pop()


count_beautiful_seq(0)
print(ans)
