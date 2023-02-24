class A:
    pass
class B(A):
    pass

b = B()
print(isinstance(b, B)) # b is an instance of B
