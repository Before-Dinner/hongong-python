# 파일 처리 중간에 예외 발생

try:
  # 파일을 엽니다.
  file = open("info.txt", "w")
  예외.발생해라()
  file.close()
except:
  print("오류가 발생했습니다.")

print("# 파일이 제대로 닫혔는지 확인하기")
print("file.closed:", file.closed)