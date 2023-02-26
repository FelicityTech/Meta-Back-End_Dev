try:
    with open('sample/newfile2.txt', 'a') as file:
        file.writelines(["\nThis is a new file created!", "\nThis is another line to be added."])
except FileNotFoundError as e:
    print("ERROR", e)
