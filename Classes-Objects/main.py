class Student:
    rollno = 3
    name = "abc"

    def info(self):
        # self keyword refers to the object on which the function is called
        print(f"{self.name} has roll no {self.rollno}")


a = Student()
a.rollno = 1
a.name = "amaan"
a.info()

b = Student()
b.rollno = 2
b.name = "ali"
b.info()
