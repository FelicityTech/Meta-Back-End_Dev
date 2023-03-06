class A:
    num = 5

class B(A):
    num = 9

class C(B):
    pass

print(help(C))
print(C.mro())