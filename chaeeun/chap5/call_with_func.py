# map() 함수와 filter() 함수

def power(item):
  return item * item
def under_3(item):
  return item < 3

list_input_a = [1, 2, 3, 4, 5]

# map() 함수를 사용합니다.
output_a = map(power, list_input_a)
print("# map() 함수의 실행 결과")
print("map(power, list_input_a):", output_a)
print("map(power, list_input_a):", list(output_a))
print()

# filter() 함수를 사용합니다.
output_b = filter(under_3, list_input_a)
print("# filter() 함수의 실행 결과")
print("filter(power, list_input_a):", output_b)
print("filter(power, list_input_a):", list(output_b))
print()