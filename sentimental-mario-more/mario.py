def main():
    while True:
        try:
            height = int(input("Height: "))
            if 0 < height < 9:
                break
            else:
                continue
        except ValueError:
            continue

    for i in range(height):
        for _ in range(height - (i + 1)):

            print(" ", end='')

        print("#" * (i + 1), end='  ')
        print("#" * (i + 1))


main()
