# 객체 만들기
students = [
  {"name": "윤인성", "korean": 1, "math": 2},
  {"name": "연하진", "korean": 2, "math": 3}
]

print("이름", "총점", "평균", sep="\t")

for student in students:
  score_sum = student["korean"] + student["math"]
  score_average = score_sum / 2
  print(student["name"], score_sum, score_average, sep='\t')