list_a = [52, 42, 3, 2, 15]

try:
    number_input_a = int(input(">"))
except Exception as exception:
    print("type: {}, message: {}".format(type(exception), exception))
    
try:
    number_input_b = int(input('>'))
    print(list_a[number_input_b])
except Exception as e:
    print("type: {}, message: {}".format(type(e), e))
    
try:
    number_input_c = int(input('>'))
    print(list_a[number_input_c])
    #예외.발생해주세요
except ValueError as e:
    print("type: {}, message: {}".format(type(e), e))
except IndexError as e:
    print("type: {}, message: {}".format(type(e), e))
except Exception as e:
    print("type: {}, message: {}".format(type(e), e))
