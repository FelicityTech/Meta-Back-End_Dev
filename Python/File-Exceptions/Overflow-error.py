try:
    x = 2 ** 10000
except OverflowError:
    print("Overflow error!")