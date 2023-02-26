try:
    x = 1 / 0
except ZeroDivisionError:
    print("Division by zero error!")
    """The finally block is then executed, which contains code that will always be executed regardless of whether an exception was raised or not. In this case, 
    the finally block prints a message"""
finally:
    print("This will always be executed.")