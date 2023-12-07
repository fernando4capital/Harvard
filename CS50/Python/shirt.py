import sys
from PIL import Image, ImageOps

def main():
    checkargs()
    processimagefile(sys.argv[1], sys.argv[2])

def checkargs():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")

    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    extensionfile1 =  sys.argv[1][-4:].lower()
    extensionfile2 =  sys.argv[2][-4:].lower()

    if extensionfile1 not in [".jpg", ".jpeg", ".png"]  or  extensionfile2 not in [".jpg", ".jpeg", ".png"]:
        sys.exit("Invalid output")

    if extensionfile1 != extensionfile2:
        sys.exit("Input and output have different extensions")


def processimagefile(muppet_without_shirt_image, new_muppet_with_shirt_image ):
    try:
        shirtfile = Image.open("shirt.png")
        sizeshirtfile = shirtfile.size

        first_imagesourcefile = Image.open(muppet_without_shirt_image)

        muppetfile = ImageOps.fit(first_imagesourcefile, sizeshirtfile)

        muppetfile.paste(shirtfile, shirtfile)

        muppetfile.save(new_muppet_with_shirt_image)


    except FileNotFoundError:
        sys.exit("Input does not exist.")


if __name__ == "__main__":
    main()