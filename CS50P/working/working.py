import re

def main():
    print(convert(input("Hours: ")))


def convert(s):
    if matches := re.search(r"^(.+) (AM|PM) to (.+) (AM|PM)$", s):
        if matches.group(2) == "AM" and matches.group(4) == "PM":
            return f"{am(matches.group(1))} to {pm(matches.group(3))}"

        if matches.group(2) == "PM" and matches.group(4) == "AM":
            return f"{pm(matches.group(1))} to {am(matches.group(3))}"

    else:
        raise ValueError


def am(hour):

    if ":" in hour:
        h, m = hour.split(":")

        if 1 <= int(h) <= 11 and 0 <= int(m) <= 59:
            return f"{int(h):02}:{m}"

        elif int(h) == 12 and 0 <= int(m) <= 59:
            return f"00:{m}"

        else:
            raise ValueError

    elif hour == "12":
        return f"00:00"

    elif 1 <= int(hour) <= 11:
        return f"{int(hour):02}:00"

    else:
        raise ValueError


def pm(hour):

    if ":" in hour:
        h, m = hour.split(":")

        if 1 <= int(h) <= 11 and 0 <= int(m) <= 59:
            return f"{int(h) + 12}:{m}"

        elif int(h) == 12 and 0 <= int(m) <= 59:
            return f"{h}:{m}"

        else:
            raise ValueError

    elif hour == "12":
        return f"{hour}:00"

    elif 1 <= int(hour) <= 11:
        return f"{int(hour) + 12}:00"

    else:
        raise ValueError


if __name__ == "__main__":
    main()
