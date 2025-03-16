import sys
from PIL import Image, ImageOps


def main():

    if checkLen() is True:
        pass
    else:
        sys.exit(checkLen())

    a = sys.argv[1].split(".")[-1]
    b = sys.argv[2].split(".")[-1]

    if checkEx(a, b) is True:
        pass
    else:
        sys.exit(checkEx(a, b))

    try:
        paste(sys.argv[1], sys.argv[2])

    except FileNotFoundError:
        sys.exit("Input does not exist")


def checkLen():

    if len(sys.argv) == 3:
        return True
    elif len(sys.argv) > 3:
        return "Too many command-line arguments"
    elif len(sys.argv) < 3:
        return "Too few command-line arguments"


def checkEx(x, y):

    if (x == "jpg" or x == "jpeg" or x == "png") and (
        y == "jpg" or y == "jpeg" or y == "png"
    ):

        if x == y:
            return True

        else:
            return "Input and output have different extensions"

    elif (x == "jpg" or x == "jpeg" or x == "png") and (
        y != "jpg" and y != "jpeg" and y != "png"
    ):
        return "Invalid output"

    else:
        return "Invalid input"


def paste(i, o):

    shirt = Image.open("shirt.png")
    size = shirt.size

    with Image.open(i) as im:
        im = ImageOps.fit(im, size)
        im.paste(shirt, shirt)
        im.save(o)


main()
