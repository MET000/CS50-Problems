
def main():

    while True:

        try:
            a = input("Fraction: ")
            print(gauge(convert(a)))
            break

        except (ValueError, ZeroDivisionError):

            continue


def convert(fraction):

    x, y = fraction.split("/")

    if int(y) >= int(x):

        return round((int(x) / int(y))*100)

    elif int(x) > int(y) and int(y) != 0:

        raise ValueError

    elif int(y) == 0:

        raise ZeroDivisionError

    else:
        return


def gauge(percentage):

    if percentage <= 1:

        return "E"

    elif percentage >= 99:

        return "F"

    else:

        return f"{percentage}%"


if __name__ == "__main__":
    main()
