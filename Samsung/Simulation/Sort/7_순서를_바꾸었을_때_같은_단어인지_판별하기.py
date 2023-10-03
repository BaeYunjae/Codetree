## 나의 코드
A = list(input())
B = list(input())
 
A.sort()
B.sort()

A = ''.join(A)
B = ''.join(B)

if A == B:
    print("Yes")
else:
    print("No")

-------------------------------------------------
## 정답 코드
A = input()
B = input()

print("Yes" if sorted(A) == sorted(B) else "No")
