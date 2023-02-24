class MyFirstClass():
    print("Who wrote this?")
    index = "Author-Book"   

    def hand_list(self, philosopher, book, year):
        print(MyFirstClass.index)
        print(philosopher + " wrote the book: " + book, " in year " + year)


whodunnit = MyFirstClass()


print(whodunnit.hand_list("plato", "Republic", "19th century"))
print(whodunnit.hand_list("Sun Tzu", "The Art of War", "20th century"))
