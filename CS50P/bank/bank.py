def main():

    x = input("Greeting: ").strip().lower()
    if x[0] == "h":
        if x.split()[0] == "hello" or x.split()[0] == "hello,":
            dollars(0)
        else:
            dollars(20)

    else:
        dollars(100)


def dollars(x):
    print(f"${x}")


main()
