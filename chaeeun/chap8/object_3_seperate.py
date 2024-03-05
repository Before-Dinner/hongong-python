# 객체를 처리하는 함수(2)

def create_student(name, korean, math):
  return{
    "name": name,
    "korean": korean,
    "math": math
  }

def student_get_sum(student):
  return student["korean"] + student["math"]

def student_get_average(student):
  return student_get_sum(student) / 2

def student_to_string(student):
  return "{}\t{}\t{}".format(
    student["name"],
    student_get_sum(student),
    student_get_average(student)
  )

students = [
  create_student("윤인성", 1, 2),
  create_student("연하진", 2, 3)
]

print("이름", "총점", "평균", sep="\t")

for student in students:
  print(student_to_string(student))