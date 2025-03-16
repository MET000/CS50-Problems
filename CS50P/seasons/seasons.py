from datetime import date
import inflect
import sys


def main():

    try:
        m = date_converter(input("Date of Birth: "))
        print(number_to_words(m))

    except ValueError:
        sys.exit("Invalid date")


def date_converter(a):

    try:
        x, y, z = a.split("-")
        age = date.today() - date(int(x), int(y), int(z))
        return round(age.total_seconds() / 60)

    except ValueError:
        raise ValueError


def number_to_words(n):

    p = inflect.engine()
    words = p.number_to_words(n).capitalize().replace(" and ", " ")
    return f"{words} minutes"


if __name__ == "__main__":
    main()
