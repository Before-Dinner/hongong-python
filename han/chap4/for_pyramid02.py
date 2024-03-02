for i in range(1, 15):
    result = ""
    for j in range(14, i, -1):
        result += " "
    for k in range(i * 2 -1):
        result = result + "\033[93m*\033[0m" \
                if i == 1 \
                else result + "*"
    print(result)