# 조건문으로 예외 처리하기

user_input_a = input("정수입력> ")

# 사용자 입력이 숫자로만 구성되어 있을 때
if user_input_a.isdigit():
  number_input_a = int(user_input_a)
  print("원의 반지름:", number_input_a)
  print("원의 둘레:", 2 * 3.14 * number_input_a)
  print("원의 넓이:", 3.14 * number_input_a * number_input_a)
else:
  print("정수를 입력하지 않았습니다.")