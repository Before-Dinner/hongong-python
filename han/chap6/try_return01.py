def test():
  print("test")
  try:
    print("try")
    return
    print("no")
  except:
    print("except")
  else:
    print("else")
  finally:
    print("finally")
  print("end")

test()