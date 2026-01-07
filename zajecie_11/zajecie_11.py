import sys
from file_handler import FileHandler

argument = sys.argv[1:]
print(argument)

file_handler = FileHandler(input_file_patch=argument[0], output_file_patch=argument[1], transformations=argument[2:])
file_handler.do_transformations()
file_handler.save_data()
