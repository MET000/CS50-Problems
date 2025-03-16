def main():

    x = input("Greeting: ")

    print("$", value(x), sep="")


def value(greeting):

    a = greeting.lower().strip()

    if a[0] == "h":
        if a.split()[0] == "hello" or a.split()[0] == "hello,":
            return 0
        else:
            return 20

    else:
        return 100


if __name__ == "__main__":
    main()
