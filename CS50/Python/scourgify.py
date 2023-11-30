import sys
import csv

def main():
    checkargs()

    sourcecontent = readcsvfile(sys.argv[1])
    writecsvfile(sys.argv[2], sourcecontent)

def checkargs():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")

    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    if ".csv" not in sys.argv[1][-4:].lower() or ".csv" not in sys.argv[2][-4:].lower():
        sys.exit("Not a CSV file")

def readcsvfile(sourcefilename):
    destinationlist = []

    try:
        with open(sourcefilename,"r") as sourcecsvfile:
            filereader = csv.DictReader(sourcecsvfile)
            for filerow in filereader:
                dictnames = filerow["name"].split(",")
                destinationlist.append({"first": dictnames[1].lstrip(), "last": dictnames[0].lstrip(), "house": filerow["house"]})

            return destinationlist

    except FileNotFoundError:
        sys.exit(f"Could not read {sourcefilename}")

def writecsvfile(destinationfilename, destinationlist):
    try:
        with open(destinationfilename, "w") as destinationcsvfile:
            filewriter = csv.DictWriter(destinationcsvfile, fieldnames=["first","last","house"])

            filewriter.writerow({"first": "first", "last": "last", "house": "house" })

            for listrow in destinationlist:
                filewriter.writerow({"first": listrow["first"], "last": listrow["last"], "house": listrow["house"] })

    except FileNotFoundError:
        sys.exit(f"Could not write {destinationfilename}")

if __name__ == "__main__":
    main()
