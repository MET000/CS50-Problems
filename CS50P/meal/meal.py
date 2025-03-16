def main():

    meal_time = convert(input("What time is it? "))

    if 7 <= meal_time <= 8:
        print("breakfast time")

    elif 12 <= meal_time <= 13:
        print("lunch time")

    elif 18 <= meal_time <= 19:
        print("dinner time")

    else:
        return


def convert(time):

    hours, minutes = time.split(":")

    return int(hours) + (int(minutes) / 60)


if __name__ == "__main__":
    main()
