## 나의 코드
class Address:
    def __init__(self, name="", street="", region=""):
        self.name = name
        self.street = street
        self.region = region

# 자료 수
n = int(input())

dictionary = [tuple(input().split()) for _ in range(n)]
dictionary.sort()

a, b, c = dictionary[-1]
last = Address(a, b, c)

print(f'name {last.name}')
print(f'addr {last.street}')
print(f'city {last.region}')

--------------------------------------------------------
## 정답 코드
class Address:
    def __init__(self, name, address, region):
        self.name = name
        self.address = address
        self.region = region

# 변수 선언 및 입력
n = int(input())
dictionary = [tuple(input().split()) for _ in range(n)]
people = [Address(name, address, region) for name, address, region in dictionary]

# 사전순으로 이름이 가장 느린 사람 찾기
target_idx = 0
for i, person in enumerate(people):
    if person.name > people[target_idx].name:
        target_idx = i

print(f'name {people[target_idx].name}')
print(f'addr {people[target_idx].address}')
print(f'city {people[target_idx].region}')
