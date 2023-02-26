import warnings

def some_function():
    warnings.warn("This feature will change in the future", FutureWarning)

    # Some code


some_function()

# the some_function function raises a FutureWarning to indicate that the behavior of 
# the function may change in the future. The warning message is "This feature will change 
# in the future". The warning is displayed in the console, but does not stop the program from executing. 
# This is useful for indicating changes in behavior that developers should be aware of