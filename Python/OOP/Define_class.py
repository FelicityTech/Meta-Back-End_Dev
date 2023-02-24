class House:
    """
    THis is a stub for a class representing a house that can be used
    to create objects and evaluate different metrics that we may require in constructing it.
    """
    num_rooms = 5
    bathrooms = 2
    def cost_evaluation(self): # self as instance method
        print(self.num_rooms)
        pass

house = House()  # instantiating of class
print(house.num_rooms)  
print(House.num_rooms) # calling class direct

house.num_rooms = 7 # Modification of  attribute
print(house.num_rooms)
print(House.num_rooms)

House.num_rooms = 7 # modification of class instance attribute
print(house.num_rooms)
print(House.num_rooms)
    