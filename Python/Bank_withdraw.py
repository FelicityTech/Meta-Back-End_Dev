from abc import ABC, abstractmethod
"""Create a class called Bank and pass ABC to it. """
class Bank(ABC):
    def basicinfo():
        """Define a function called basicinfo() and add a print statement inside it saying "This is a generic bank" 
        and returning the string "Generic bank: 0" """
        print("This is a generic bank")
        return "Generic bank: 0"
    """Define a second function called withdraw and keep it empty by adding a pass keyword under it. Make this function abstract 
    by adding '@abstractmethod' right above it. """
    @abstractmethod
    def withdraw():
        pass

""" Create another class called Swiss and pass the class Bank inside it. This means you are inheriting from class Bank. """
class Swiss(Bank):
    def __init__(self, bal=1000): #Create a constructor for this class that initializes a class variable `bal` to 1000
        self.bal = bal
    """Override both functions from the Bank class: basicinfo() and withdraw()."""
    def withdraw(self, amount):
        if (amount > self.bal):
            print("Insufficient funds")
            return self.bal
        else:
            self.bal = self.bal - amount
            print(f"withdraw amount: {amount}")
            print(f"New balance: {self.bal}")
            return self.bal


bank = Swiss()
print(bank.withdraw(30))