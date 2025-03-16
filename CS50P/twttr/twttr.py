def main():

    a = input("Input: ")
    twttr(a)


def twttr(x):

    b = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]

    print("Output: ", end="")

    for i in x:

        if i not in b:

            print(i, end="")

        else:

            continue


main()
