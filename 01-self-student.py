class Student:
    def __init__(self,name,age):
        # Constructor
        # This method is called when an object is created
        self.name = name
        self.age = age

    def display(self):

        print(f"NAME:{self.name} AGE:{self.age}")
s1 = Student("John", 20)
s1.display()