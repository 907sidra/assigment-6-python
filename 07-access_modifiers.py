class Employee:
    def __init__(self, name, salary, ssn):

        self.name = name
        self._salary = salary
        self.__ssn = ssn

emp =Employee("John", 50000, "123-45-6789")
print("PUBLIC:", emp.name)
print("PRIVATE:", emp._salary)
#print("PROTECTED:",emp.__ssn)  # This will raise an AttributeError
print("PROTECTED:", emp._Employee__ssn)  # Accessing the private attribute using name mangling

