# import random
# f = open("petnames.txt", "r")
# f_content = f.read()
# f_content_list = f_content.split("\n")
# # print(f_content_list)
# print(random.choice(f_content_list))
f = open("sample.txt", "r")
# old_list = f.readlines()
# for line in reversed(old_list):
#     print(line)

content = f.readlines()

new_list = content[:: -1]
print(new_list)


