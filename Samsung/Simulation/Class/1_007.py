## class
# 클래스 선언
class meet:
    def __init__(self, code, location, time):
        self.code = code
        self.location = location
        self.time = time

# 변수 선언 및 입력
c, l, t = tuple(input().split())

# 객체 생성
ans = meet(c, l, t)

# Runtime: 72ms, Memory: 29MB
print(f"secret code : {ans.code}")
print(f"meeting point : {ans.location}")
print(f"time : {ans.time}")

''' Runtime: 102ms, Memory: 29MB
print("secret code :", ans.code)         
print("meeting point :", ans.location)
print("time :", ans.time)
'''

---------------------------------------------
## tuple
# 변수 선언 및 입력
c, l, t = tuple(input().split())

# 튜플 생성
s = (c, l, t)

# 튜플 원소들을 각 변수에 대입
secret_code, meeting_point, time = s

print(f"secret code : {secret_code}")
print(f"meeting point : {meeting_point}")
print(f"time : {time}")
