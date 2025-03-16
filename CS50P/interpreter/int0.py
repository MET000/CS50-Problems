expression = input("Expression: ")

x, y, z = expression.split(" ")

if y == "+":
    print ("%.1f" % float(int(x) + int(z)))

elif y == "/":
    print ("%.1f" % float(int(x) / int(z)))

elif y == "-":
    print ("%.1f" % float(int(x) - int(z)))

else :
    print ("%.1f" % float(int(x) * int(z)))
