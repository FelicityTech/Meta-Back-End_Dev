from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print("Woof!")
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        print("Meow!")
        return "Meow!"

dog = Dog()
cat = Cat()

print(dog.make_sound())
print(cat.make_sound())