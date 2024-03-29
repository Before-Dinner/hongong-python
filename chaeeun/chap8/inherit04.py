# 자식 클래스로써 부모에 없는 새로운 함수 정의하기
class CustomException(Exception):
  def __init__(self, message, value):
    super().__init__()
    self.message = message
    self.value = value
  def __str__(self):
    return self.message
  def print(self):
    print("## 오류 정보 ##")
    print("메시지:", self.message)
    print("값:", self.value)

try:
  raise CustomException("딱히 이유 없음", 2)
except CustomException as e:
  e.print()