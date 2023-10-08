# Class
class Student:
    def __init__(self, name, height, weight):
        self.name, self.height, self.weight = name, height, weight

n = int(input())
students = []
for _ in range(n):
    name, height, weight = input().split()
    students.append(Student(name, int(height), int(weight)))

# 키 오름차순, 키가 동일한 경우 몸무게 내림차순
students.sort(key = lambda x: (x.height, -x.weight))

for student in students:
    print(student.name, student.height, student.weight)
  
--------------------------------------------------------
# Tuple
n = int(input())
students = []
for _ in range(n):
    name, height, weight = input().split()
    students.append((name, int(height), int(weight)))
    
# 키 오름차순, 키가 동일한 경우 몸무게 내림차순
students.sort(key = lambda x: (x[1], -x[2]))

for name, height, weight in students:
    print(name, height, weight)
  
