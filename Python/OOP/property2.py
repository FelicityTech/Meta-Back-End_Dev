class Circle:
    def __init__(self, radius):
        self._radius = radius


    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value

    @property
    def diameter(self):
        return 2 * self._radius
    
    @diameter.setter
    def diameter(self, value):
        if value < 0:
            raise ValueError("Diameter cannot be negative")
        self._radius = value / 2


    @property
    def area(self):
        return 3.14159 * self._radius ** 2
    

c = Circle(2)
print(c.radius)

print(c.diameter)

print(c.area)

c.radius = 3

print(c.diameter)
print(c.area)
c.diameter = 10
print(c.radius)
print(c.area)