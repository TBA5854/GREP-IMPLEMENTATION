import sys
import re
import os

def help():
    print("Help")
    print("Usage: python3 temp.py [OPTION]... PATTERN [FILE]...")
    print("Search for PATTERN in each FILE.")
    print("Example: python3 temp.py -i 'hello' file.txt")
    print("Options:")
    print("-E, --extended-regexp: Interpret PATTERN as an extended regular expression.")
    print("-i, --ignore-case: Ignore case distinctions in both PATTERN and the input files.")
    print("-v, --invert-match: Invert the sense of matching, to select non-matching lines.")
    print("-n, --line-number: Prefix each line of output with the 1-based line number within its input file.")
    print("-x, --context: Print 3 lines of context around, each line containing the pattern.")
    print("-w, --word: Match only whole words.")
    print("-r, --recursive: Read all files under each directory, recursively.")
    print("-c, --count: Print a count of matching lines for each input file.")
    print("-C, --colour: Highlight the matching text.")

def usage():
    print("Usage: python3 temp.py [OPTION]... PATTERN [FILE]...")
    print("Try 'python3 temp.py --help' for more information.")
    
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

def recursive_search (argv):
    file_path=argv[2]
    pattern=argv[3]
    for root, dirs, files in os.walk(file_path):
        for file in files:
            if file.endswith('.txt'):
                with open(os.path.join(root, file), 'r') as file:
                    for line in file:
                        if re.search(pattern, line):
                            print(os.path.join(root, file), line, end='')

def count (argv):
    file_path=argv[2]
    pattern=argv[3]
    count = 0
    with open(file_path, 'r') as file:
        for line in file:
            if re.search(pattern, line):
                count += 1
    print(count)

def colourised_output (argv):
    
    file_path=argv[2]
    pattern=argv[3]
    with open(file_path, 'r') as file:
        for line in file:
            if re.search(pattern, line):
                print("\033[1;32;40m", line,"\033[0m", end='')

def no_args(pattern):
    for line in sys.stdin:
        if re.search(pattern, line):
            print(line, end='')

if sys.argv[1] == '--help':
    help()
elif sys.argv[1] == '--version':
    print("Version 1.0")
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
elif sys.argv[1] == '-r' or sys.argv[1] == '--recursive':
    recursive_search(sys.argv)
elif sys.argv[1] == '-c' or sys.argv[1] == '--count':
    count(sys.argv)
elif sys.argv[1] == '-C' or sys.argv[1] == '--colour':
    colourised_output(sys.argv)
else:
    usage()
    sys.exit(1)