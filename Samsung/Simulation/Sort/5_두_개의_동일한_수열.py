## 나의 코드
n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()

if A == B:
    print("Yes")
else:
    print("No")

--------------------------------------------
## 정답 코드
n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

def equal():
    # 정렬 후 원소가 하나라도 다르면 False
    # 전부 같으면 True
    for elem1, elem2 in zip(A, B):
        if elem1 != elem2:
            return False
    return True    

A.sort()
B.sort()

if equal():
    print("Yes")
else:
    print("No")
