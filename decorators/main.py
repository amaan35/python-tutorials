def dec1(func1):
    def imp1():
        print("This is first decorator function")
        func1()
    return imp1
def dec2(func2):
    def imp2():
        print("This is second decorator function")
        func2()
    return imp2
@dec1
def function1():
    print("this is first decorated function")

def function2():
    print("This is second decorated function")
function1()
dec2(function2)()
