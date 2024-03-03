def test():
  print("call")
  yield "test"

print("A")
test()

print("B")
test()
print(test())

def test():
  print("A")
  yield 1
  print("B")
  yield 2
  print("C")

output = test()
print("D")
print(next(output))
print("E")
print(next(output))
print("F")
print(next(output))

next(test())