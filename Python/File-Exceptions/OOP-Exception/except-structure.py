def divide(x, y):
    assert y != 0, "Cannot divide by zero"
    return x / y

try:
    # some code that may raise an exception
except Exception as e:
    # handle the exception
else:
    # code that is executed if no exception is raised
