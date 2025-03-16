def main():

    while True:
        try:
            number = int(input("Number: "))
            break
        except ValueError:
            continue

    validity_identifier = check_sum(number)
    number_of_digits = check_len(number)
    first_digits = check_first_digits(number)

    if (
        (number_of_digits == 15)
        and (first_digits == 34 or first_digits == 37)
        and (validity_identifier == 0)
    ):
        print("AMEX")

    elif (
        (number_of_digits == 16)
        and (
            first_digits == 51
            or first_digits == 52
            or first_digits == 53
            or first_digits == 54
            or first_digits == 55
        )
        and (validity_identifier == 0)
    ):

        print("MASTERCARD")

    elif (
        (number_of_digits == 13 or number_of_digits == 16)
        and (int(first_digits / 10) == 4)
        and (validity_identifier == 0)
    ):

        print("VISA")

    else:
        print("INVALID")


def check_sum(n):

    sum1 = add_digits(n, 10, True)
    sum2 = add_digits(n, 1, False)
    last_digit = int((sum1 + sum2) % 10)

    return last_digit


def add_digits(number, divisor, multiply=True):

    sum = 0
    multiplicator = 100

    while True:

        target = int((number / divisor) % 10)

        if int(number / divisor) > 0:

            if (target * 2) < 10 and multiply:

                sum += target * 2

            elif (target * 2) >= 10 and multiply:

                sum += int((target * 2) / 10) + int((target * 2) % 10)

            else:
                sum += target

            divisor *= multiplicator

        else:
            break

    return sum


def check_len(n):

    len = 0
    divisor = 1

    while True:
        marker = int(n / divisor)

        if marker > 0:
            divisor = divisor * 10
            len += 1

        else:
            break

    return len


def check_first_digits(n):

    divisor = 1
    while True:
        x = int(n / divisor)

        if x > 100:
            divisor *= 10

        elif x < 100:
            return x


main()
