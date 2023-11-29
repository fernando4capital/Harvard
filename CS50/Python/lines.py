import sys

def main():
    checkargs()
    readpythonfile()

def checkargs():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")

    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    if ".py" not in sys.argv[1][-3:].lower():
        sys.exit("Not a Python file")


def ignorelines(fileline):
    if fileline.isspace():
        return True

    if fileline.lstrip().startswith('#'):
        return True

    return False

def countlines(lines):
    totallines = 0
    for line in lines:
        if ignorelines(line) == False:
            totallines +=1

    print(totallines)
    sys.exit()

def readpythonfile():
    try:
        pythonfile = open(sys.argv[1],"r")
        filelines = pythonfile.readlines()
        countlines(filelines)
    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()