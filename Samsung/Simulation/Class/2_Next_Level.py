class User:
    def __init__(self, id = "codetree", level = "10"):
        self.id = id
        self.lv = level
    
input_id, input_lv = tuple(input().split())

user1 = User()
user2 = User(input_id, input_lv)

print(f'user {user1.id} lv {user1.lv}')
print(f'user {user2.id} lv {user2.lv}')
