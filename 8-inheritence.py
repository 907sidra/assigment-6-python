class Person:
    def __init__(self,name):
        self.name = name
        print(f"Person initialized with name: {self.name}")
class Teacer(Person):
    def __init__(self,name,subject):
        super().__init__(name)
        self.subject = subject
        print(f"Teacher initialized with subject: {self.subject}")

T1 = Teacer("John", "Math")