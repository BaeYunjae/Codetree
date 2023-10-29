n = int(input())
lines = [tuple(map(int, input().split())) for _ in range(n)]

ans = 0
selected_lines = []

def overlapped(l1, l2):
    (ax1, ax2), (bx1, bx2) = l1, l2

    # 두 선분이 겹치는지 여부는
    # 한 점이 다른 선분에 포함되는 경우로 판단 가능하다.
    # ------       ------      ------   ------  
    #   ------   ------      ------        ------
    return (ax1 <= bx1 and bx1 <= ax2) or (ax1 <= bx2 and bx2 <= ax2) or \
           (bx1 <= ax1 and ax1 <= bx2) or (bx1 <= ax2 and ax2 <= bx2)

def possible():
    # 단 한쌍이라도 선분끼지 겹치면 안된다.
    for i, l1 in enumerate(selected_lines):
        for j, l2 in enumerate(selected_lines):
            if i < j and overlapped(l1, l2):
                return False

    return True

def find_max_lines(cnt):
    global ans
    
    # print(cnt, selected_lines, ans)

    if cnt == n:
        if possible():
            ans = max(ans, len(selected_lines))
        return

    # 해당 선분을 선택한 경우
    selected_lines.append(lines[cnt])
    find_max_lines(cnt + 1)
    selected_lines.pop()

    # 해당 선분을 선택하지 않은 경우
    find_max_lines(cnt + 1)

find_max_lines(0)
print(ans)
        

