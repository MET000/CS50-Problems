def main():

    grocery()


def grocery():

    a = {}

    try:

        while True:

            item = input("")

            if item in a:

                a[item] += 1

            else:

                a[item] = 1

    except EOFError:

        print()

        for i in sorted(a):

            print(a[i], i.upper())


main()
