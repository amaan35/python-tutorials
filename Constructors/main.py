class Employee:
    def __init__(self, namepassed, occpassed):
        self.name = namepassed
        self.occupation = occpassed

    def info(self):
        print(f"{self.name} is a/an {self.occupation}")


a = Employee("ali", "python dev")
a.info()
