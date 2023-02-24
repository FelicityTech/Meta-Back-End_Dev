class A:
    a = 1
    
class B(A):
    a = 2
class C(B):
    pass

c = C() # output: 2 bcos C derives from immediate super class C and that is B
