import warnings


warnings.filterwarnings("ignore", category=ImportWarning)

try:
    import some_module
except:
    pass


# the filterwarnings function is used to ignore ImportWarning warnings. 
# The try block attempts to import a module, and if an exception is raised, the pass statement is executed. If an ImportWarning is raised during the import, it is ignored and the program continues to execute. 
# This is useful for ignoring warnings that may not be important or 
# relevant to a particular piece of code.