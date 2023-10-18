"""
Task 1: Calculate the Square of a Number
Write a function that takes an integer as an argument and returns its square.
"""
def square(int):
    return  int**2
est=square(5)
print(est)
"""
Task 2: Calculate the Area of a Rectangle:
Write a function that takes the length and width of a rectangle and returns its area.
"""
def aor(length, width):
    return length * width
drink = aor(8,8)
print(drink)

"""
Task 3: Convert Temperature from Celsius to Fahrenheit:
Write a function that takes a temperature in Celsius and returns 
the equivalent temperature in Fahrenheit using the correct formula
"""

def a3(c): #function of the parameter in temperature
    return c * 9/5 + 32 # converts celcius to farenheit 
assert a3 (23) == 73.4
print(a3(23)) #printing the result of the given parameter
"""
Task 4: Calculate the Average of Numbers:
Write a function that takes a list of numbers 
and returns the average (mean) of those numbers.
"""
def avgfun(a):
   # Returns the sum of all six digits
   listtotal = sum(a)
   return listtotal/len(a)
# the variable takes the assigned sum and divides it by the amount
print(avgfun([5,7,7,8,9]))