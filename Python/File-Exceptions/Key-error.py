try:
    d = {"a": 1, "b" : 2}
    print(d["c"])
except KeyError:
    print("Key error!")