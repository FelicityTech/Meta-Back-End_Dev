import warnings


def new_function():
    warnings.warn("new_function() will be deprecated in the future",PendingDeprecationWarning )
    # Some code

new_function()

# the new_function function raises a PendingDeprecationWarning
#  to indicate that it will be deprecated in the future, but is 
# still supported for now. The warning message is "new_function() 
# will be deprecated in the future". The warning is displayed in the console, 
# but does not stop the program from executing.