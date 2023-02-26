def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return a / b

# x = divide(10,5)
# y = divide(7, 0)
# print(x)
# print(y)
try:
    result = divide(10, 0)
except ZeroDivisionError as e:
    print("An error occurred:", e)