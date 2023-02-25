# Python program to
# demonstrate private members
 
# Creating a Base class

class Base:
    def __init__(self):
        self.a = "Eniola"
        self.__c = "Solomon"

# Creating a derived class
class Derived(Base):
    def __init__(self):
        print("Calling private member of base class: ")
        print(self.__c)


# Driver code
obj1 = Base()
print(obj1.a)
print(obj1.__c)