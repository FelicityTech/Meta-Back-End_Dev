try:
    x = 1 / 0

except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    print("This block is always executed")