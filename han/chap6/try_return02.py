checked = False

def write_text_file(filename, text):
  global checked
  try:
    file = open(filename, "w")
    return
    file.write(text)
  except:
    print("except")
  finally:
    file.close()
    checked = file.closed 

write_text_file("test.txt", "HI")
print("close?", checked)