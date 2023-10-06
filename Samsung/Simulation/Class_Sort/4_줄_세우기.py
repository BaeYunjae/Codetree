# Class
class Student:
    def __init__(self, height, weight, number):
        self.height, self.weight, self.number = height, weight, number

n = int(input())
students = []
for i in range(1, n + 1):
    h, w = map(int, input().split())
    students.append(Student(h, w, i))

students.sort(key = lambda x : (-x.height, -x.weight, x.number))

for student in students:
    print(student.height, student.weight, student.number)

------------------------------------------------------------------------
# Tuple
n = int(input())
students = []
for i in range(1, n + 1):
    h, w = map(int, input().split())
    students.append((h, w, i))

students.sort(key = lambda x : (-x[0], -x[1], x[2]))

for h, w, num in students:
    print(h, w, num)
  
