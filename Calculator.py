a = int (input("Enter a number: "))

print()

b = float(input("Give me another number: "))

print()

print('''select operation:
Add
Sub
Mult
Div
Exponent
Floor_div
Remainder''')
c = int(input)
print()

if c == 1:
    y = a + b
    print(y)
elif c == 2:
    y = a - b
    print(y)
elif c == 3:
    y = a * b
elif c == 4:
    if a or b == 0:
        print("Print number higher than zero")
    else:
        y = a / b
        print(y)
    elif c == 5:
y = a // b
print(y)
elif c == 6:
y = a ** b
print(y)
elif c == 7:
y = a % b
print(y)
print("Print a number on the list of operations.")