# 첫번째 풀이 (while문)
# 격자 크기, 시간
n, t = map(int, input().split())

# 구슬 정(r행 c열 d방향)
r, c, d = input().split()
r = int(r) - 1
c = int(c) - 1

# 0번과 3번, 1번과 2번 반대방향
dxs, dys = [0, 1, -1, 0], [1, 0, 0, -1]

mapper = {
    'R': 0,
    'D': 1,
    'U': 2,
    'L': 3
}

dir_num = mapper[d]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

while t:
    nx, ny = r + dxs[dir_num], c + dys[dir_num]
    if not in_range(nx, ny):
        dir_num = 3 - dir_num
        t -= 1
    t -= 1
    if t < 0:
        break
    r, c = r + dxs[dir_num], c + dys[dir_num]
    

print(r + 1, c + 1)

--------------------------------------------------------
# 두번째 풀이 (for문)
# 격자 크기, 시간
n, t = map(int, input().split())

# 구슬 정(r행 c열 d방향)
r, c, d = input().split()
r = int(r) - 1
c = int(c) - 1

# 0번과 3번, 1번과 2번 반대방향
dxs, dys = [0, 1, -1, 0], [1, 0, 0, -1]

mapper = {
    'R': 0,
    'D': 1,
    'U': 2,
    'L': 3
}

dir_num = mapper[d]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

for _ in range(t):
    nx, ny = r + dxs[dir_num], c + dys[dir_num]
    if in_range(nx, ny):
        r, c = nx, ny
    else:
        dir_num = 3 - dir_num
    

print(r + 1, c + 1)

