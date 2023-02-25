class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        @property
        def width(self):
            return self._width
        
        @width.setter
        def width(self, value):
            if value < 0:
                raise ValueError("width cannot be negative")
            self._width = value

        @property
        def height(self):
            return self._height


        @height.setter
        def height(self, value):
            if value < 0:
                raise ValueError("Height cannot be negative")
            self._height = value

        def area(self):
            return self._width * self._height        