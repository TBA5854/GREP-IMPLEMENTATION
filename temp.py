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
def invert_match (argv):
    file_path=argv[2]
    pattern=argv[3]
    with open(file_path, 'r') as file:
        for line in file:
            if not re.search(pattern, line):
                print(line, end='')



if sys.argv[1] == '--help':
    help()
elif sys.argv[1] == '-E' or sys.argv[1] == '--extended-regexp':
    basic_search(sys.argv)
elif sys.argv[1] == '-i' or sys.argv[1] == '--ignore-case':
    case_insenstive(sys.argv)
elif sys.argv[1] == '-v' or sys.argv[1] == '--invert-match':
    invert_match(sys.argv)