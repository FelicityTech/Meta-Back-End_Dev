import warnings

def my_function(x):
    if x < 0:
        warnings.warn("Value is negative", category=UserWarning)

    return x ** 2

# print(my_function(-5))

try:
    result = my_function(-1)
except UserWarning:
    print("Warning issued")