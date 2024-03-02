# read() 함수로 텍스트 읽기

# 파일을 엽니다.
with open("basic.txt", "r") as file:
  contents = file.read()

print(contents)