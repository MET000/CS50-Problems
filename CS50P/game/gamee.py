import random


def main():
    level = get_level()
    target = get_random_number(level)

    while True:
        try:
            guess = int(input("Guess: "))
            if guess > 0:
                if guess == target:
                    print("Just right!")
                    break
                elif guess > target:
                    print("Too large!")
                else:
                    print("Too small!")
            continue
        except ValueError:
            continue


def get_level():
    while True:
        try:
            a = int(input("Level: "))
            if a < 1:
                pass
            else:
                return a
        except ValueError:
            continue


def get_random_number(n):
    b = random.randint(1, n)
    return b


main()
