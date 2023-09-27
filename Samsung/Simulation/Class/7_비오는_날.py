## 나의 코드
class Data:
    def __init__(self, date, day, weather):
        self.date = date
        self.day = day
        self.weather = weather

# 데이터 수
n = int(input())
predict = [tuple(input().split()) for _ in range(n)]
rains = [Data(date, day, weather) for date, day, weather in predict if weather == "Rain"]

target_idx = 0
for i, rain in enumerate(rains):
    if rain.date < rains[target_idx].date:
        target_idx = i

print(rains[target_idx].date, rains[target_idx].day, rains[target_idx].weather)

-----------------------------------------------------------------
## 정답 코드
class Forecast:
    def __init__(self, date, day, weather):
        self.date, self.day, self.weather = date, day, weather

# 데이터 수
n = int(input())

ans = Forecast("9999-99-99", "", "")
for _ in range(n):
    date, day, weather = tuple(input().split())

    # Forecast 객체
    f = Forecast(date, day, weather)
    if weather == "Rain":
        # 비가 오는 경우 가장 최근인지 확인
        # 가장 최근일 경우 정답 업데이트
        if ans.date >= f.date:
            ans = f

print(ans.date, ans.day, ans.weather)
