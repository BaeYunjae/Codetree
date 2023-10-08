# Class & sorted()
class Student:
    def __init__(self, name, height, weight):
        self.name, self.height, self.weight = name, height, weight

students = []
for _ in range(5):
    name, height, weight = input().split()
    students.append(Student(name, int(height), float(weight)))

# 이름순으로 정렬, 오름차순
name_sort = sorted(students, key = lambda x: x.name)
# 키가 큰 순으로 정렬, 내림차순
height_sort = sorted(students, key = lambda x: -x.height)

print('name')
for student in name_sort:
    print(student.name, student.height, student.weight)

print()
print('height')
for student in height_sort:
    print(student.name, student.height, student.weight)

-------------------------------------------------------------------
# Class & sort()
class Student:
    def __init__(self, name, height, weight):
        self.name, self.height, self.weight = name, height, weight

students = []
for _ in range(5):
    name, height, weight = input().split()
    students.append(Student(name, int(height), float(weight)))

# 이름순으로 정렬, 오름차순
students.sort(key = lambda x: x.name)
print('name')
for student in students:
    print(student.name, student.height, student.weight)

print()

# 키가 큰 순으로 정렬, 내림차순
students.sort(key = lambda x: -x.height)
print('height')
for student in students:
    print(student.name, student.height, student.weight)

-------------------------------------------------------------------
# Tuple & sort()
students = []
for _ in range(5):
    name, height, weight = input().split()
    students.append((name, int(height), float(weight)))

# 이름순으로 정렬, 오름차순
students.sort(key = lambda x: x[0])
print('name')
for n, h, w in students:
    print(n, h, w)

print()

# 키가 큰 순으로 정렬, 내림차순
students.sort(key = lambda x: -x[1])
print('height')
for n, h, w in students:
    print(n, h, w)
  
