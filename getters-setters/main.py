class MyClass:
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = new_value


obj = MyClass(10)
print(obj.value)
obj.value = 100
print(obj.value)

# the name of getter and setter functions has to be same
# adding @property decorator on a function makes it the getter
# adding @<function-name>.setter decorator on a function makes it the setter
# As already told, this function-name has to be same for both getter and setter function
# these decorators makes these functions seem like they are an attribute/property of the class
