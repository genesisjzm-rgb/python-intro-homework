#Handle a Missing File with try and except FileNotFoundError
#trys to open "../data/missing.txt"

import os

def read_file(filename):
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        base_name = os.path.basename(filename)
        print(f"Error: {base_name} was not found. Please check the file path and try again.")
        return ""

file_content = read_file("../data/missing.txt")  # This will print an empty string if the file is not found