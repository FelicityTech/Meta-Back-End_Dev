class MyCustomException(Exception):
    def my_function(x):
        if x < 0:
            raise MyCustomException("x must be non-negative")
        

    try:
         my_function(-1)
    except MyCustomException as e:
        print(e)

