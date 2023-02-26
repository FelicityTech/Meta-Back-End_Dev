import warnings

def some_function(x):

    if x == 0:
        warnings.warn("Divide by zero", RuntimeWarning)
    else:
        return 10 / x
    
    some_function(0)
    # the some_function function raises a RuntimeWarning if the argument x is equal to zero. 
    # The warning message is "Divide by zero". The warning is displayed in the console, but 
    # does not stop the program from executing. 
    # This is useful for indicating potential problems at runtime, such as divide by zero errors.