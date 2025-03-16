def main():

    item = input("Item: ").title()
    calories(item)


def calories(fruit):

    fruits = {
        "Banana": "110",
        "Avocado": "50",
        "Apple": "130",
        "Cantaloupe": "50",
        "Grapefruit": "60",
        "Grapes": "90",
        "Honeydew Melon": "50",
        "Kiwifruit": "90",
        "Lemon": "15",
        "Lime": "20",
        "Nectarine": "60",
        "Orange": "80",
        "Peach": "60",
        "Pear": "100",
        "Pineapple": "50",
        "Plums": "70",
        "Strawberries": "70",
        "Sweet Cherries": "100",
        "Tangerine": "50",
        "Watermelon": "80",
    }

    for _ in fruits:

        if fruit in fruits:

            print(f"{fruits[fruit]} calories")

            break

        else:

            break


main()
