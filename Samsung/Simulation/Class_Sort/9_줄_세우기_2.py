# Class
class Student:
    def __init__(self, height, weight, number):
        self.h, self.w, self.num = height, weight, number

n = int(input())
students = []
for num in range(1, n + 1):
    h, w = map(int, input().split())
    students.append(Student(h, w, num))

# 1순위: 키 오름차순, 2순위: 몸무게 내림차순
students.sort(key = lambda x: (x.h, -x.w))

for student in students:
    print(student.h, student.w, student.num)
  
----------------------------------------------
# Tuple
n = int(input())
students = []
for num in range(1, n + 1):
    h, w = map(int, input().split())
    students.append((h, w, num))

# 1순위: 키 오름차순, 2순위: 몸무게 내림차순
students.sort(key = lambda x: (x[0], -x[1]))

for h, w, num in students:
    print(h, w, num)
