## 나의 코드
k, n = map(int, input().split())

answer = []
def print_answer():
    for elem in answer:
        print(elem, end=" ")
    print()

def choose(curr_num):
    if curr_num == n + 1:
        print_answer()
        return

    for i in range(1, k + 1):
        answer.append(i)
        choose(curr_num + 1)
        answer.pop()

    return

choose(1)

--------------------------------
## 정답 코드
# 변수 선언 및 입력
k, n = map(int, input().split())
selected_nums = []

# 선택된 원소들을 출력해준다.
def print_permutation():
    for num in selected_nums:
        print(num, end=" ")
    print()

def find_permutations(cnt):
    if cnt == n:
        print_permutation()
        return

    # i부터 k까지의 각 숫자가 뽑혔을 때의 경우를 탐색한다.
    for i in range(1, k + 1):
        selected_nums.append(i)
        find_permutations(cnt + 1)
        selected_nums.pop()


find_permutations(0)
