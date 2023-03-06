class Fruit():
    def __init__(self, fruit):
        print('Fruit type: ', fruit)


class FruitFlavour(Fruit):
    def __init__(self, fruit):
        super().__init__(fruit)
        print(f'{fruit} is sweet')

fruit1 = FruitFlavour("Apple")
print(fruit1) 