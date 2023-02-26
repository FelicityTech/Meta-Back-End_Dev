def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero", x, y)
    return x / y


try:
    result = divide(4, 0)
except ValueError as e:
    message, x, y = e.age
    print(message, "(", x, "/",y, ")")