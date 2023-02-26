class MyException1(Exception):
    pass
class MyException2(Exception):
    pass


try:
    raise MyException1("Exception 1")
except (MyException1, MyException2) as e:
    print("Caught exception:", e)
