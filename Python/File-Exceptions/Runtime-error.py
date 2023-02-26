try:
    x = [1, 2, 3]
    x.remove(4)
except RuntimeError:
    print("Runtime error!")