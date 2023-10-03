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
