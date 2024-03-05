# 객체를 만드는 함수(1)
def create_student(name, korean, math):
  return{
    "name": name,
    "korean": korean,
    "math": math
  }

students = [
  create_student("윤인성", 1, 2),
  create_student("연하진", 2, 3)
]

print("이름", "총점", "평균", sep="\t")

for student in students:
  score_sum = student["korean"] + student["math"]
  score_average = score_sum / 2
  print(student["name"], score_sum, score_average, sep='\t')