class Animal:
    def sound(self):
        print("Sound of an animal")

class Dog(Animal):

    # overriding sound function in child class with a new definition
    # if we do not provide below function, then object of this class
    # calls the sound function of Animal class
    def sound(self):
        print("woof woof")

d = Dog()
d.sound()
