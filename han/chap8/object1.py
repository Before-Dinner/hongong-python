class student:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
    
    def get_name_with_age(self) -> str:
        return "name: {}, age: {}".format(
            self.get_only_name(),
            self.get_only_age()
        )
    def get_only_name(self) -> str:
        return self.name
        
    def get_only_age(self) -> int:
        return self.age
        
list_student = [
    student("Han", 28),
    student("Seong", 27),
    student("Deok", 26)
]

for s in list_student:
    print(s.get_name_with_age())