def main():
    x = input("File name: ").lower().strip()

    if ".gif" in x:
        exetension("image/gif")

    elif ".jpg" in x or ".jpeg" in x :
        extension("image/jpeg")

    elif ".pdf" in x :
        extension("application/pdf")

    elif ".png" in x :
        extension("image/png")

    elif ".txt" in x :
        extension("text/plain")

    elif ".zip" in x :
        extension("application/zip")

    else :
        extension("application/octet-stream")

def extension(x):
    print(x)

main()

