def dec(func):
    def mod_func(*args, **kwargs):
        print("Inside modifying function")
        func(*args, **kwargs)
    return mod_func


@dec
def add(a, b):
    print(a+b)


def sub(a, b):
    print(a-b)


add(10, 20)
dec(sub)(20, 10)
