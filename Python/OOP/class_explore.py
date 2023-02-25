class A: #Class definition of A  
    """Constructor for A """
    def __init__(self, c):
        print("______Inside Class A_____")
        self.c = c
    print("Print inside A.")
    """Definition of local method alpha() """
    def alpha(self):
        c = self.c + 1
        return c
    
print(dir(A))
print("Instantiating A..")#Instantiating object a over class A 
a = A(1)
print(a.alpha())#Calling method alpha() over object of class A


class B: #Class definition of B 
    """Constructor for B"""
    def __init__(self, a):
        print("------Inside class B-------")
        self.a = a
    print(a.alpha()) # Calling method alpha() over object of class A  
    d = 5
    print(d)
    print(a)

print("Instantiating B..")
b = B(a)# Instantiating object a over class B *
print(a) # Additional print statements distributed through the code