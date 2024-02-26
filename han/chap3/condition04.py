number = input("정수> ")
number = int(number)

if number % 2 == 0: print("짝수")
else: print("홀수")
  
print("짝수" if number % 2 ==0 else "홀수")