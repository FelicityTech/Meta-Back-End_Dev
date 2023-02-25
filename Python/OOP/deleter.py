class Person:
    def __init__(self, name):
        self._name = name


    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value

    @name.deleter
    def name(self):
        del self._name


p = Person("Sola")
# print(p.name)
d =(p.name)
del d
print(p.name)