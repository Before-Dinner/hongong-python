class Student:
  def __init__(self, name, korean, math):
    self.name = name
    self.korean = korean
    self.math = math
  def get_sum(self):
    return self.korean + self.math
  def get_avereage(self):
    return self.get_sum() / 2
  def to_string(self):
     return "{}\t{}\t{}".format(
       self.name,\
       self.get_sum(),\
       self.get_avereage())

students = [
  Student("윤인성", 1, 2),
  Student("연하진", 2, 3),
]

print("이름", "총점", "평균", sep="\t")
for student in students:
  print(student.to_string())