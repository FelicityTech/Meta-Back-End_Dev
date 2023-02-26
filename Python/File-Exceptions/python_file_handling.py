file = open('./test.txt', mode = 'r')

data = file.readlines()

print(data)

file.close()