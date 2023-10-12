# Create a float variable, and then convert it to an integer
# Print both the original variable and the converted integer.

my_float = 5.09
my_integer = int(my_float)
print(my_float)
print(my_integer)
#I made my float and my integer into a variable  


"""
TASK 2:
Write code that takes a number as input and prints whether 
it's positive, negative, or zero using if-elif-else statements.
"""
X = 11
if X > 0:
    print("Positive")
if X < 0:
 print("Negative")


"""
TASK 3:

Write code that takes two numbers as input (an integer and a float), 
performs addition, subtraction, multiplication, and division, and prints the results.
"""
R = int(input("Give me a integer: "))
C = float(input("Give me a float: "))
add = R + C
sub = R - C
mult = R * C
div = R / C
print(add, sub, mult, div)
"""
TASK 4:

Create a dictionary with keys as fruit names and values as their respective quantities. 
Then print out the quantity of one of the fruits.
"""

fruits = {
     'Mango' : 7,
    'Cherry' : 8
}
print(fruits["Mango"])

"""
TASK 5:

Create a string variable with that is a list of numbers and convert that string into a tuple.
Then print out the both the original string and tuple.
"""
X = "1,2,3,4,5,6,7,8"
X_tup = X.split(",")
print(tuple(X_tup))