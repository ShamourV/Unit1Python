"""
1. Simple Counter:
Write a program that uses a while loop to print numbers from 1 to 10.
"""
i = 0
while i < 10:
  i += 1
  print(i)

"""
2. Countdown:
Write a program that uses a while loop to print numbers from 10 to 1 in descending order.
"""
num = 10
while num > 0:
    print(num)
    num -= 1

"""
3. Factorial Calculation:
Write a program that calculates the factorial of a given number using a while loop.
"""
product = 1
fact = int(input('pick a number'))
while fact >1:
   product = fact * product
   fact -= 1
   print('product')
"""
4. Password Guessing Game:
Create a simple password guessing game using a while loop. Ask the user to guess a predefined password and provide appropriate feedback.
"""
c = ''
while c != 'Ginger':
   c = input('Guess the password:')
   if c == 'Ginger':
      print('congrats')
   else:
      print('try again')
"""
5. Sum of Digits:
Write a program that calculates the sum of the digits of a given number using a while loop.
"""
a = 'Start'
while a != 'Stop':
   value = input('Give me a number')
   value2 = input('Give me a second number:')
   print(int(value) + int(value2))
"""
6. Fibonacci Series:
Write a program that prints the first n numbers in the Fibonacci sequence using a while loop.
"""