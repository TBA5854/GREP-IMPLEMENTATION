import re

def grep(pattern, file_path):
    with open(file_path, 'r') as file:
        for line in file:
            if re.search(pattern, line):
                print(line, end='')

grep(pattern, file_path)