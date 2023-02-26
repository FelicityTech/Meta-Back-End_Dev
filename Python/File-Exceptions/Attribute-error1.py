try:
    x = 123
    x.foo()
except AttributeError:
    print("Attribute error!")