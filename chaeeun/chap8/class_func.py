# 클래스 함수

class Student:
  count = 0
  students = []

  # 클래스 함수
  @classmethod
  def print(cls):
    print("---학생 목록---")
    print("이름", "총점", "평균", sep="\t")
    for student in cls.students:
      print(str(student))
    print("------------")

  def __init__(self, name, korean, math):
    self.name = name
    self.korean = korean
    self.math = math
    Student.count += 1
    Student.students.append(self)

  def get_sum(self):
    return self.korean + self.math
  def get_average(self):
    return self.get_sum() / 2
  def __str__(self):
    return "{}\t{}\t{}".format(\
      self.name,\
        self.get_sum(),\
          self.get_average())

Student("윤인성", 1, 2),
Student("연하진", 2, 3)

Student.print()