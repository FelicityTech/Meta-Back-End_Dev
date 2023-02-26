import warnings

def old_function():
    warnings.warn("old_function() is depreciated", DeprecationWarning)

# Some code

"""the old_function function raises a DeprecationWarning to indicate that it is deprecated
 and should not be used in new code. The warning message is "old_function() is deprecated". 
The warning is displayed in the console, but does not stop the program from executing."""

