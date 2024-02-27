import sys
import re

def help():
    print("Help")
def basic_search (argv):
    file_path=argv[2]
    pattern=argv[3]
    with open(file_path, 'r') as file:
        for line in file:
            if re.search(pattern, line):
                print(line, end='')

def case_insenstive (argv):
    file_path=argv[2]
    pattern=argv[3]
    with open(file_path, 'r') as file:
        with open(file_path, 'r') as file:
            data = file.readlines()
            for i in data:
                for j in i:
                    if(i.lower==pattern.lower):
                        print(j)

print(sys.argv)
print(sys.argv[1])

if sys.argv[1] == '--help':
    help()
elif sys.argv[1] == '-E' or sys.argv[1] == '--extended-regexp':
    basic_search(sys.argv[2], sys.argv[3])
elif sys.argv[1] == '-i' or sys.argv[1] == '--ignore-case':
    # case_insensitive(sys.argv)
    pass