exp = input()

x, y, z = exp.split(" ")
x = float(x)
z = float(z)
out = 0
if y == "+":
    out = x+z
elif y == "-":
    out = x-z
elif y == "*":
    out = x*z
elif y == "/":
    out = x/z

print(f"{out:.1f}")
