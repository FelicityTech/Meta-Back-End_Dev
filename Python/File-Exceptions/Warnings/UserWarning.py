import warnings

def some_function():
    warnings.warn("This is a user warning", UserWarning)
    # some code


some_function()

#the some_function function raises a UserWarning 
# to indicate that there is a potential problem with the function, 
# but it is not critical. The warning message is "This is a user warning".
#  The warning is displayed in the console, 
# but does not stop the program from executing.