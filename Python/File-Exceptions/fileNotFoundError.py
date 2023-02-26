try:
    with open('file_does_not_exist.txt', 'r') as file:
        print(file.read())

except:
    print("Unable to locate file")   