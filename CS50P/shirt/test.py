from PIL import Image
from PIL import ImageOps
import sys

shirt = Image.open("shirt.png")
size = shirt.size


def checkEx(a,b):

    if len(sys.argv) == 3 :

        a = sys.argv[1].split(".")[-1]
        b = sys.argv[2].split(".")[-1]

        print(a, b)

        if (a == ("jpeg" or "png" or "jpg")) and (b == ("jpeg" or "png" or "jpg")) :

            if a == b :

                try:

                    with Image.open(sys.argv[1]) as im:

                        im = ImageOps.fit(im, size)

                        im.paste(shirt, shirt)

                        im.save(sys.argv[2])

                except FileNotFoundError:

                            sys.exit("Input does not exist")

        elif a != b :

            sys.exit("Input and output have different extensions")


    elif  a != ("jpeg" and "png" and "jpg") :

        sys.exit("Invalid input")

    elif  b != ("jpeg" and "png" and "jpg") :

        sys.exit("Invalid output")



elif len(sys.argv) < 3:

    sys.exit("Too few command-line arguments")


else:

    sys.exit("Too many command-line arguments")
