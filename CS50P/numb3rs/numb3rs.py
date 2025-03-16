import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):

    if matches := re.search(r"^([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})$", ip):
        for i in matches.groups():
            if 0 <= int(i) <= 255:
                continue
            else:
                return False
        return True

    return False


if __name__ == "__main__":
    main()
