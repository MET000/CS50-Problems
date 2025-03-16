def main():

    name = input("camelCase: ")
    print("snake_case: ", end="")
    snake_case(name)


def snake_case(n):

    for i in n:
        if i == i.lower():
            print(i, end="")
        else:
            print(f"_{i.lower()}", end="")


main()
