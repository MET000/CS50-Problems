import sys
from tabulate import tabulate
import csv


def main():
    pizza_table(sys.argv)


def pizza_table(n):
    a = []

    if len(n) == 2:
        try:
            if n[1][-4:] == ".csv":

                with open(n[1]) as file:
                    reader = csv.reader(file)

                    for row in reader:
                        a.append(row)

                    headers = a[0]

                print(tabulate(a[1:], headers, tablefmt="grid"))

            else:
                sys.exit("Not a python file")

        except FileNotFoundError:
            sys.exit("File does not exist")

    elif len(n) > 2:
        sys.exit("Too many command-line arguments")

    else:
        sys.exit("Too few command-line arguments")


main()
