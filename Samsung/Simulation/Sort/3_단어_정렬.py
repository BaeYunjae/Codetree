n = int(input())
ls = [input() for _ in range(n)]
ls.sort()

for i in ls:
    print(i, end='\n')
