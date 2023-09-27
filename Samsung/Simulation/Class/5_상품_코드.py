# 첫번째 코드
class Product:
    def __init__(self, name="", code=0):
        self.name = name
        self.code = code

i_name, i_code = tuple(input().split())
i_code = int(i_code)

p1 = Product()
p1.name = "codetree"
p1.code = 50

p2 = Product(i_name, i_code)

print(f'product {p1.code} is {p1.name}')
print(f'product {p2.code} is {p2.name}')

-------------------------------------------
# 두번째 코드
class Product:
    def __init__(self, name="", code=0):
        self.name = name
        self.code = code

i_name, i_code = tuple(input().split())

p1 = Product("codetree", 50)
p2 = Product(i_name, int(i_code))

print(f'product {p1.code} is {p1.name}')
print(f'product {p2.code} is {p2.name}')
