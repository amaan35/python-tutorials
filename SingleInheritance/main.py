class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def person_info(self):
        print(f"{self.name} has age {self.age}")

class Student(Person):
    def __init__(self, name, age, klass):
        Person.__init__(self, name, age)
        self.klass = klass

    def student_info(self):
        print(f"{self.name} is a student in class {self.klass}")

s = Student("Amaan", 17, 12)
s.person_info()
s.student_info()
