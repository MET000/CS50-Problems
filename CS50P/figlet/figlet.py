from pyfiglet import Figlet
import sys
import random


def main():

    print(figlet())


def figlet():

    figlet = Figlet()

    if len(sys.argv) < 2:

        figlet.setFont(font=random.choice(figlet.getFonts()))
        a = input("Input: ")
        return figlet.renderText(a)

    elif sys.argv[1] == "-f" or sys.argv[1] == "--font":

        figlet.setFont(font=sys.argv[2])
        a = input("Input: ")
        return figlet.renderText(a)

    else:

        sys.exit("Invalid usage")


main()
