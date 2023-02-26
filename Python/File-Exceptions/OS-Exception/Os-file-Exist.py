import os

def create_directory(path):
    try:
        os.mkdir(path)
    except FileExistsError:
        raise FileExistsError("Directory already exists")