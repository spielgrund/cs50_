expression = input("gimme gimme: ")
x, y, z = expression.split(" ")
x = float(x)
z = float(z)
if y == "+":
    ergebniss = x+z
    print(f"{ergebniss:0.1f}")
elif y == "/":
    ergebniss = x/z
    print(f"{ergebniss:0.1f}")
elif y == "*":
    ergebniss = x*z
    print(f"{ergebniss:0.1f}")
elif y == "-":
    ergebniss = x-z
    print(f"{ergebniss:0.1f}")
else:
    print("falsche eingabe")


