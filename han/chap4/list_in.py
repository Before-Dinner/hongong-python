array = [pow(i, 2) 
         for i in range(0, 20, 2)]
print(array)

array = ["a", "b", "c", "d", "e"]
result = [v 
          for v in array 
          if v != "e"]
print(result)