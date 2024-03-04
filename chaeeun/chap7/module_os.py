# os 모듈

# os를 읽어 들임
import os

print("현재 운영체제:", os.name)
print("현재 폴더:", os.getcwd())
print("현재 폴더 내부의 요소:", os.listdir())

# 폴더를 만들고 제거
os.mkdir("hello")
os.rmdir("hello")

# 파일을 생성 + 파일 이름 변경
with open("original.txt", "w") as file:
  file.write("hello")
os.rename("original.txt", "new.txt")

# 파일 제거
os.remove("new.txt")

# 시스템 명령어 실행
os.system("dir")