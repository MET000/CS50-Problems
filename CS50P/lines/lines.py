import sys


def main():
    count_lines(sys.argv)


def count_lines(a):
    n = 0

    if len(a) == 2:

        if a[1][-3:] == ".py":
            try:

                with open(a[1]) as file:
                    for line in file:
                        if len(line.lstrip()) == 0 or line.lstrip().startswith("#"):
                            continue

                        else:
                            n += 1

                print(n)

            except FileNotFoundError:
                sys.exit("File does not exist")

        else:
            sys.exit("Not a python file")

    elif len(a) > 2:
        sys.exit("Too many command-line arguments")
    else:
        sys.exit("Too few command-line arguments")


main()
