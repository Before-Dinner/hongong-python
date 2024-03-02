test = (
    "a"
    "b"
    "c"
    )
print(test)
print(type(test))

test = (
    "a",
    "b",
    "c",
    )
print(test)
print(type(test))

## clean code !

num = input("input number> ")
def print_odd_even(num) -> None:
    if num % 2 == 0:
        print(
            ("input number is {}\n"
            "{} is Even").format(num, num)
            )
    else:
        print(
            ("input number is {}\n"
            "{} is Odd").format(num, num)
            )

print_odd_even(int(num))

