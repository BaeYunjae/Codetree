# Class
class Student:
    def __init__(self, name, height, weight):
        self.n = name
        self.h = height
        self.w = weight

n = int(input())
students = []
for _ in range(n):
    name, height, weight = input().split()
    students.append(Student(name, int(height), int(weight)))

students.sort(key = lambda x: x.h)

for student in students:
    print(student.n, student.h, student.w)

-------------------------------------------------------------
# Tuple
n = int(input())

# 이름, 키, 몸무게
ls = [tuple(input().split()) for _ in range(n)]

ls.sort(key = lambda x: x[1])

for name, height, weight in ls:
    print(name, height, weight)
  
