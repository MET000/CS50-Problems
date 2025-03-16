def main():

    x = input("File name: ").lower().strip()
    extension(x)


def extension(f):

    if ".gif" in f:
        print("image/gif")

    elif ".jpg" in f or ".jpeg" in f:
        print("image/jpeg")

    elif ".pdf" in f:
        print("application/pdf")

    elif ".png" in f:
        print("image/png")

    elif ".txt" in f:
        print("text/plain")

    elif ".zip" in f:
        print("application/zip")

    else:
        print("application/octet-stream")


main()
