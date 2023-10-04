# hierarchical inheritance
class A:
    def __init__(self, a):
        self.a = a
    def showA(self):
        print(f"In class A and value of a is {self.a}")

class B(A):
    def __init__(self, a, b):
        A.__init__(self, a)
        self.b = b
    def showB(self):
        print(f"In class B and value of b is {self.b}")

class C(A):
    def __init__(self, a, c):
        A.__init__(self, a)
        self.c = c
    def showC(self):
        print(f"In class C and value of c is {self.c}")

objb = B(10, 20)
objb.showA()
objb.showB()
objc = C(30, 40)
objc.showA()
objc.showC()

# Hybrid Inheritance
class D(B, C):
    def __init__(self, a, b, c, d):
        B.__init__(self, a, b)
        C.__init__(self, a, c)
        self.d = d
    def showD(self):
        print(f"Value of a = {self.a}, b = {self.b}, c = {self.c}, and d = {self.d}")

objd = D(50, 60, 70, 80)
objd.showD()
