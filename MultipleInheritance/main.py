class Father:
    def __init__(self, eye_color):
        self.eye_color = eye_color

class Mother:
    def __init__(self, hair_color):
        self.hair_color = hair_color

class Child(Father, Mother):
    def __init__(self, eye_color, hair_color):
        # Entering values in the inherited attributes directly
        # self.eye_color = eye_color
        # self.hair_color = hair_color
        
        # Entering values in super constructors
        Father.__init__(self, eye_color)
        Mother.__init__(self, hair_color)

    def child_info(self):
        print(f"this child has {self.eye_color} eye color and {self.hair_color} hair color")

c = Child("Blue", "Black")
c.child_info()
