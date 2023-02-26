try:
    x = 55 / 0# some code that may raise an exception
except BaseException as e:
    print(f"an error occurred: {e}")

    # it's generally not recommended to catch BaseException directly,
    #  as this will also catch system exceptions like SystemExit and KeyboardInterrupt that should not be caught in most cases. 
    # Instead, it's better to catch specific exceptions that you expect may be raised by your code.