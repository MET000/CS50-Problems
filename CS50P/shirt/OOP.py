from PIL import Image
from PIL import ImageOps
import sys

shirt = Image.open("shirt.png")
size = shirt.size


if len(sys.argv) == 3:

    if (sys.argv[1].split(".")[-1] and sys.argv[2].split(".")[-1]) == "jpg" or "png" or "jpeg" :

        if sys.argv[1].split(".")[-1] == sys.argv[2].split(".")[-1]:

            try:

                with Image.open(sys.argv[1]) as im:

                    im = ImageOps.fit(im, size)

                    im.paste(shirt, shirt)

                    im.save(sys.argv[2])

            except FileNotFoundError:

                sys.exit("Input does not exist")

        elif sys.argv[1].split(".")[-1] != sys.argv[2].split(".")[-1]:

            sys.exit("Input and output have different extensions")


    elif (sys.argv[1].split(".")[-1] != "jpg" and "png" and "jpeg") or "." not in sys.argv[1] :

        sys.exit("Invalid input")

    elif sys.argv[2].split(".")[-1] != "jpg" and "png" or "." not in sys.argv[2] :

        sys.exit("Invalid output")



elif len(sys.argv) < 3:

    sys.exit("Too few command-line arguments")


else:

    sys.exit("Too many command-line arguments")
