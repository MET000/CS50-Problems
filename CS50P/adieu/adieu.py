import inflect


def main():

    print(get_names_and_format_farewell())


def get_names_and_format_farewell():

    p = inflect.engine()

    names = []

    try:

        while True:

            name = input("Name: ")

            names.append(name)

    except EOFError:

        return f"\nAdieu, adieu, to {p.join(names)}"


main()
