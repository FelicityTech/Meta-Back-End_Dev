# Raising exception from methods

class MyClass:
    def __init__(self, value):
        self.value = value


    def do_somethimg(self):
        if self.value < 0:
            raise ValueError("Value must be non-negative")
        

try:
    obj = MyClass(-1)
    obj.do_somethimg()
except ValueError as e:
    print("Caught exception:", e)