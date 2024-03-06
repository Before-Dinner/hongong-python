# 사용자 정의 예외 클래스 만들기

class CustomException(Exception):
  def __init__(self):
    super().__init__()

raise CustomException