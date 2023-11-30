import sys
import csv
from tabulate import tabulate

def main():
    checkargs()
    readcsvfile(sys.argv[1])

def checkargs():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")

    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    if ".csv" not in sys.argv[1][-4:].lower():
        sys.exit("Not a CSV file")

def readcsvfile(filename):
    filetable = []
    try:
        with open(filename,"r") as csvfile:
            filereader = csv.reader(csvfile)
            for filerow in filereader:
                filetable.append(filerow)

            print (tabulate(filetable[1:], headers=filetable[0], tablefmt="grid"))

    except FileNotFoundError:
        sys.exit("File does not exist")

if __name__ == "__main__":
    main()
