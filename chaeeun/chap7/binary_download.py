from urllib import request

# urlopen() 함수로 구글의 메인 페이지 읽기
target = request.urlopen("https://www.hanbit.co.kr/images/common/logo_hanbit.png")
output = target.read()
print(output)

# write binary[바이너리 쓰기] 모드
file = open("output.png", "wb")
file.write(output)
file.close()