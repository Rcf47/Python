import os

current_working_dir = os.getcwd()

file_path = os.path.join(current_working_dir, "file_from_python")

open(file_path, "w").write("Hello my friend")
