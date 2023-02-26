try:
    file = open("nonexistent_file.txt", "r")
except:
    print("File not found error!")