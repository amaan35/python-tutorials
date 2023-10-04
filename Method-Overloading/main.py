# It is actually not method overloading in my opinion as
# we are not creating multiple functions with same name
class MethodOverloading:
    def sum(self, a=None, b=None, c=None):
        if(a!=None and b!=None and c!=None):
            sum = a+b+c
            return sum
        elif(a!=None and b!=None):
            sum = a+b
            return sum
        else:
            return a

m = MethodOverloading()
print(m.sum(10, 20, 30))
