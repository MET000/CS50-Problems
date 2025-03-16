def main():

    print(fuel(input("Fraction: ")))


def fuel(a):

    while True:

        try:

            x, y = a.split("/")

            if 0.01 < int(x) / int(y) < 0.99:

                return f"{int(round((int(x) / int(y)) * 100))}%"

            elif 0.99 <= int(x) / int(y) <= 1:

                return "F"

            elif int(x) / int(y) <= 0.01:

                return "E"

            else:

                pass

        except (ValueError, ZeroDivisionError):

            pass


main()
