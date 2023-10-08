## 나의 코드 - Tuple
n = int(input())
inputs = list(map(int, input().split()))

# 동일한 원소인 경우 먼저 나오는 원소가 더 앞으로
elems = []
for idx, num in enumerate(inputs, start=1):
    elems.append((num, idx))  # 편의를 위해 (원소, 위치)

# 오름차순 정렬, 동일한 원소일 경우 idx 오름차순
elems.sort(key = lambda x: (x[0], x[1]))

# 정답 리스트
result = [0] * (n + 1)

for idx, (_, i) in enumerate(elems, start=1):
    result[i] = idx 

print(*result[1:])

---------------------------------------------------------
## 정답 노드 - Class
class Number:
    def __init__(self, number, index):
        self.number, self.index = number, index

n = int(input())
inputs = list(map(int, input().split()))

numbers = [Number(num, i) for i, num in enumerate(inputs)]

# 오름차순 정렬, 동일한 원소일 경우 idx 오름차순
numbers.sort(key = lambda x: (x.number, x.index))

# 정답 리스트
result = [0] * n

for i, number in enumerate(numbers, 1):
    result[number.index] = i 

print(*result)

