# 크기 비교 함수

class Student:
  def __init__(self, name, korean, math):
    self.name = name
    self.korean = korean
    self.math = math
  def get_sum(self):
    return self.korean + self.math
  def get_avereage(self):
    return self.get_sum() / 2
  def __str__(self):
     return "{}\t{}\t{}".format(
       self.name,\
       self.get_sum(),\
       self.get_avereage())
  def __eq__(self, value):
    return self.get_sum() == value.get_sum()
  def __nq__(self, value):
    return self.get_sum() != value.get_sum()
  def __gt__(self, value):
    return self.get_sum() > value.get_sum()
  def __ge__(self, value):
    return self.get_sum() >= value.get_sum()
  def __lt__(self, value):
    return self.get_sum() < value.get_sum()
  def __le__(self, value):
    return self.get_sum() <= value.get_sum()

students = [
  Student("윤인성", 1, 2),
  Student("연하진", 2, 3),
]

student_a = Student("윤인성", 1, 2)
student_b = Student("연하진", 2, 3)

print("student_a == student_b =", student_a == student_b)
print("student_a != student_b =", student_a != student_b)
print("student_a > student_b =", student_a > student_b)
print("student_a >= student_b =", student_a >= student_b)
print("student_a < student_b =", student_a < student_b)
print("student_a <= student_b =", student_a <= student_b)
