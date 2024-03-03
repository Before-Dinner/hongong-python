output = []
def flatten(data: list) -> list:
    global output
    for i in data:
        if type(i) == list: flatten(i)
        else: output.append(i)
    return output

check = [[1,2,3],[2,3,4,5],[6,[3,4]],[1,6]]
print(flatten(check))