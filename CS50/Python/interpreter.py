askExpression = input("Expression:")
elements = askExpression.split(" ")
x = float(elements[0])
y = elements[1]
z = float(elements[2])

if y == "+":
    print (x+z)
if y == "-":
    print (x-z)
if y == "*":
    print (x*z)
if y == "/":
    print (x/z)
