class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age


    def get_name(self):
        return self._name
    
    def get_age(self):
        return self._age
    

p = Person("Sola", 26)
print(p.get_name())

print(p.get_age())