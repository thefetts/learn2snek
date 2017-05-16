def read_file(filename):
    file_object = open("../files/data.txt", "r")
    return file_object.read().split("\n")

