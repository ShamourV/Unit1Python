# Task 1: Greeting Function
# Write a function `greet(name)` that takes a name as a parameter and prints a greeting message like "Hello, [name]!".
def my_function(name):
    #I used the def to define the name of my function

    print("Hello" + name)
my_function(" Rasta ")

# Task 2: Sum of Two Numbers
# Write a function `sum_numbers(a, b)` that takes two numbers as parameters and returns their sum.
def sum_numbers(A, B):
    print(A + B)
    print(200, 81)

# Task 3: Calculate Factorial
# Write a function `factorial(n)` that calculates the factorial of a given number `n`.

def factorial(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial = factorial * i
        print("The factorial of", n, "is", factorial)
        factorial(5)
        
# Task 4: Check Even or Odd
# Write a function `is_even(num)` that takes a number as a parameter and returns `True` if the number is even, and `False` otherwise.
def is_even(num): #
    if num % 2 == 0: #Checking remainder for either even or non even
        print('True')
    else:
        print('False')
        is_even(5)
# Task 5: Calculate Area of a Rectangle
# Write a function `calculate_area(length, width)` that calculates and returns the area of a rectangle given its length and width.
