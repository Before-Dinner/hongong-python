# 클래스 변수

class Student:
  count = 0
  def __init__(self, name, korean, math):
    self.name = name
    self.korean = korean
    self.math = math

    Student.count += 1
    print("{}번째 학생이 생성되었습니다.".format(Student.count))

students = [
  Student("윤인성", 1, 2),
  Student("연하진", 2, 3)
]

print("현재 생성된 총 학생수는 {}명입니다.".format(Student.count))