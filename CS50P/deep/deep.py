def main():

    x = input("What is the Answer to Great Question of Life, the Universe, and Everything? ").lower().strip()
    answer(x)


def answer(a):

    if a == "42" or a == "forty-two" or a == "forty two":
        print("Yes")
    else:
        print("No")


main()
