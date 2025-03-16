def main():

    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(a):

    if (
        first_characters(a)
        and minimum_characters(a)
        and conditions(a)
        and allowed_characters(a) is True
    ):
        return True

    else:

        return False


def first_characters(a):

    if a[0:2].isalpha():
        return True
    else:
        return False


def minimum_characters(a):

    if 2 <= len(a) <= 6:
        return True
    else:
        return False


def conditions(a):

    for i in range(len(a)):

        if a[i].isalpha():

            continue

        elif a[i].isdecimal() and a[i:].isdecimal() and a[i] != "0":

            continue

        elif a[i] == "0" and a[i - 1].isdecimal():

            continue

        else:
            return False

    return True


def allowed_characters(a):

    for i in a:
        if i.isdecimal() or i.isalpha():
            continue
        else:
            return False

    return True


main()
