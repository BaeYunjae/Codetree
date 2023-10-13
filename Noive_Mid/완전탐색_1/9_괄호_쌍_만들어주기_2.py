## 나의 코드 (Runtime: 264ms, Memory: 25MB)
A = input()

ans = 0
for i in range(len(A) - 1):
    for j in range(i + 2, len(A) - 1):
        if A[i : i + 2] == '((':
            if A[j : j + 2] == '))':
                ans += 1

print(ans)

----------------------------------------------------------------------------------
## 정답 코드 (Runtime: 105ms, Memory: 24MB)
A = input() 
n = len(A)

ans = 0
for i in range(n - 1):
    for j in range(i + 1, n - 1):
        if A[i] == '(' and A[i + 1] == '(' and A[j] == ')' and A[j + 1] == ')':
            ans += 1

print(ans)
