class A:
    def __init__(self, a):
        self.a = a

class B(A):
    def __init__(self, b):
        self.b = b

class C(B):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def show(self):
        print(f"{self.a} {self.b} {self.c}")


objc = C(10, 20, 30)
objc.show()
