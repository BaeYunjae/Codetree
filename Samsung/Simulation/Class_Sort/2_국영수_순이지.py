# Class
class Student:
    def __init__(self, name, kor, eng, math):
        self.name, self.kor, self.eng, self.math = name, kor, eng, math


n = int(input())
students = []
for _ in range(n):
    name, k, e, m = input().split()
    students.append(Student(name, int(k), int(e), int(m)))

# 점수가 높은 학생부터 출력하므로 내림차순 정렬
students.sort(key = lambda x : (-x.kor, -x.eng, -x.math))

for student in students:
    print(student.name, student.kor, student.eng, student.math)

---------------------------------------------------------------------------
# Tuple
n = int(input())
students = []
for _ in range(n):
    name, kor, eng, math = input().split()
    students.append((name, int(kor), int(eng), int(math)))

# 점수가 높은 학생부터 출력하므로 내림차순 정렬
# tuple 0: 이름, 1: 국어, 2: 영어, 3: 수학
students.sort(key = lambda x : (-x[1], -x[2], -x[3]))

for name, kor, eng, math in students:
    print(name, kor, eng, math)
