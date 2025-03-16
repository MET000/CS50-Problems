import validators


def main():
    print(validator(input("What's your email adsress? ")))


def validator(e):
    if validators.email(e):
        return "Valid"
    else:
        return "Invalid"


main()
