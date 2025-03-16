def main():

    word = input("Input: ")

    print("Output:", shorten(word))


def shorten(word):

    a = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
    b = []

    for i in word:

        if i not in a:

            b.append(i)

        else:

            continue

    return ''.join(b)


if __name__ == "__main__":

    main()
