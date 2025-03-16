import random


def game():
    while True:
        try:
            level = int(input("Level: "))
            if level < 1:
                continue
            else:
                target = random.randint(1, level)
                while True:
                    try:
                        guess = int(input("Guess: "))
                        if 1 < guess < target:
                            print("Too small!")
                        elif guess > target:
                            print("Too large!")
                        elif guess < 1:
                            continue
                        else:
                            print("Just right!")
                            break
                    except ValueError:
                        continue
            break
        except ValueError:
            continue


game()
