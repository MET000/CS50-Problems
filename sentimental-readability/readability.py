def main():

    text = input("Input: ")
    index = index_calculator(text)

    if index < 1:

        print("Before Grade 1")

    elif index >= 16:

        print("Grade 16+")

    else:

        print(f"Grade {index}")


def index_calculator(text):

    numbers = counter(text)
    letters = numbers[0]
    words = numbers[1]
    sentences = numbers[2]

    L = (letters * 100.0) / words
    S = (sentences * 100.0) / words
    index = 0.0588 * L - 0.296 * S - 15.8

    return round(index)


def counter(text):

    a = [0, 1, 0]

    for i in range(len(text)):

        if text[i].isalpha():

            a[0] += 1

        elif text[i].isspace():

            a[1] += 1

        elif text[i] == "!" or text[i] == "." or text[i] == "?":

            a[2] += 1

    return a


main()
