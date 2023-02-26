file = open("sample.txt", "r")
line_to_print = [2]

for index, line in enumerate(file):
    if (index in line_to_print):
        print(line)