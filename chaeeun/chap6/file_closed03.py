# finally 구문 사용해 파일 닫기

try:
  # 파일을 엽니다.
  file = open("info.txt", "w")
  예외.발생해라()
  file.close()
except:
  print("오류가 발생했습니다.")
finally:
  # 파일을 닫습니다.
  file.close()

print("# 파일이 제대로 닫혔는지 확인하기")
print("file.closed:", file.closed)