import random


def main():

    a = get_level()
    n = 0

    for _ in range(10):

        b = generate_integer(a)
        z = generate_integer(a)

        for _ in range(3):

            x = int(input(f"{b} + {z} = "))

            if x == b + z:

                break

            else:

                print("EEE")

        if x != b + z:
            print(f"{b} + {z} = {b+z}")
            n += 1

        else:
            continue

    print(f"Score: {10 - n}")


def get_level():

    while True:

        try:

            level = int(input("Level: "))

            if level == 1 or level == 2 or level == 3:

                return level

            else:

                continue

        except ValueError:

            pass


def generate_integer(level):

    if level == 1:

        return random.randint(0, 9)

    elif level == 2:

        return random.randint(10, 99)

    else:

        return random.randint(100, 999)


if __name__ == "__main__":
    main()
