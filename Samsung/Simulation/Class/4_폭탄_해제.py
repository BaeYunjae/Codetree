class Bomb:
    def __init__(self, code, color, second):
        self.code = code
        self.color = color
        self.second = second

i_code, i_color, i_second = tuple(input().split())
ans = Bomb(i_code, i_color, i_second)

print(f'code : {ans.code}')
print(f'color : {ans.color}')
print(f'second : {ans.second}')
