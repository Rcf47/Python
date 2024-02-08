import os

text = input()

file_path = os.path.join(os.path.abspath("/tmp"), "my_file")


def write_and_read(text):
    open(file_path, "w").write(text)
    return open(file_path, "r").read()


print(write_and_read(text))
