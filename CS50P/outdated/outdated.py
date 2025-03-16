def main():

    print(outdated())


def outdated():

    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]

    while True:

        try:

            date = input("Date: ")

            if "/" in date:

                x, y, z = date.split("/")

                if 1 < int(z) < 2024 and 1 < int(y) < 31 and 1 < int(x) < 12:

                    return f"{int(z):02}-{int(x):02}-{int(y):02}"

                else:

                    pass

            elif "," in date:

                a, b, c = date.split(" ")

                a = int(months.index(a)) + 1

                b = int(b.replace(",", ""))

                if 1 < int(c) < 2024 and 1 < int(b) < 31:

                    return f"{c}-{a:02}-{b:02}"

                else:

                    pass

            else:

                pass

        except ValueError:

            continue


main()
