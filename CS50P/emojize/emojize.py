import emoji


def main():

    print(emojize(input("Input: ")))


def emojize(a):

    return f"Output: {emoji.emojize(a, language='alias')}"


main()
