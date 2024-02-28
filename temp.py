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
def op_formatting (argv):
    file_path=argv[2]
    pattern=argv[3]
    with open(file_path, 'r') as file:
        data = file.readlines()
        for i in range(len(data)):
            print(i+1, data[i], end='')
def context (argv):
    file_path=argv[2]
    pattern=argv[3]
    with open(file_path, 'r') as file:
        data = file.readlines()
        for i in range(len(data)):
            print(i+1, data[i], end='')
            if re.search(pattern, data[i]):
                for j in range(i-1, i+2):
                    print(j+1, data[j], end='')

def word_match (argv):
    file_path=argv[2]
    pattern=argv[3]
    with open(file_path, 'r') as file:
        for line in file:
            if re.search(r'\b' + pattern + r'\b', line):
                print(line, end='')


if sys.argv[1] == '--help':
    help()
elif sys.argv[1] == '-E' or sys.argv[1] == '--extended-regexp':
    basic_search(sys.argv)
elif sys.argv[1] == '-i' or sys.argv[1] == '--ignore-case':
    case_insenstive(sys.argv)
elif sys.argv[1] == '-v' or sys.argv[1] == '--invert-match':
    invert_match(sys.argv)
elif sys.argv[1] == '-n' or sys.argv[1] == '--line-number':
    op_formatting(sys.argv)
elif sys.argv[1] == '-x' or sys.argv[1] == '--context':
    context(sys.argv)
elif sys.argv[1] == '-w' or sys.argv[1] == '--word':
    word_match(sys.argv)