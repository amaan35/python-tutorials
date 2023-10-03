class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    def show_details(self):
        print(f"{self.name} has id {self.id}")

class Programmer(Employee):
    def __init__(self, name, id, lang):
        super().__init__(name, id)
        self.lang = lang

    # before adding the third parameter namely lang in above constructor,
    # I was calling this below function to input lang at object creation
    # super() keyword was used to access the constructor of superclass
    # and the parameters that were required by the superclass were passed
    # into that constructor : name, id
    # def set_lang(self, lang):
    #    self.lang = lang

    def show(self):
        print(f"{self.name} {self.id} {self.lang}")


e = Employee("Amaan", 1)
e.show_details()
p = Programmer("Ali", 2, "Java")
p.show()
