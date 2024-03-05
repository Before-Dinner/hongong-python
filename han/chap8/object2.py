def create_student(name: str, age: int) -> dict:
    return {
        "name": name,
        "age": age
    }
    
list_students = [
    create_student("Han", 28),
    create_student("Seong", 27),
    create_student("Deok", 26)
]

def get_only_name(student: dict) -> str:
    return student["name"]
        
def get_only_age(student: dict) -> int:
    return student["age"]

def get_name_with_age(studnet: dict) -> str:
    return "name: {}, age: {}".format(
        get_only_name(studnet),
        get_only_age(studnet)
    )

for s in list_students:
    print(get_name_with_age(s))