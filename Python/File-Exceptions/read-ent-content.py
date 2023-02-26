# with open('sample.txt', 'r') as file:
    # print(file.read())
    # print(file.read(44))
    # print(file.readline())
    # print(file.readlines())
    # data = file.readlines()


    # for x in data:
    #     print(x)

with open('sample.txt', 'r') as file:
    for x in file:
        print(x)