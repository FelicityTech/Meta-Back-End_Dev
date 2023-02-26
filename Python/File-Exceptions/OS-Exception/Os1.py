import os

try:
    with open("nonexistent.txt") as f:
        contents = f.read()
except FileExistsError:
    print("File not found")