def main():

    expression = input("Expression: ")

    x, y, z = expression.split(" ")

    print(calculate(x,y,z))


def calculate(a,b,c):

    if b == "+":
        return float(int(a) + int(c))

    elif b == "/":
        return float(int(a) / int(c))

    elif b == "-":
        return float(int(a) - int(c))

    else :
        return float(int(a) * int(c))


main()
