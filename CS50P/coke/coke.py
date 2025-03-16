def main():
    coke()


def coke():
    i = 0
    while i in range(50):

        a = int(input("Insert Coin: "))

        if a == 25 or a == 5 or a == 10:

            i += a

            if i < 50:
                print(f"Amount Due: {50 - i}")

            else:
                print(f"Change Owed: {i - 50}")

        else:

            print("Amount Due: 50")

            continue


main()
