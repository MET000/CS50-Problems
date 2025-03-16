import re


def main():
    print(count(input("Text: ")))


def count(s):
    a = re.findall(r"\bum\b", s, re.IGNORECASE)
    return len(a)


if __name__ == "__main__":
    main()
