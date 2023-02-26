try:
    x = [0] * 1000000000
except MemoryError:
    print("Memory error!")