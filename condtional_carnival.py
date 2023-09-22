'''
TASK 1 Even or Odd
Determine if a number is even or odd.
'''

number = int(input('Enter a number:')) 

number = number % 2

if number == 0:
    print('Even')
else:
    print('Odd')

'''
TASK 2 Positive, Negative, or Zero:
Determine if a number is positive, negative, or zero.

EXTRA CREDIT: Tell the user if they did not enter a valid number
'''
nums = int(input('Enter a number'))

if nums > 0 :
    print('Positive')
elif nums < 0 :
    print('Odd')
elif nums == 0 :
    print('This is a zero value')
else :
    print('invalid')
'''
TASK 3: Largest of Three
Find and print the largest of three numbers.
'''
my_numbers = ['203' , '75' , '319']

my_numbers[2]

print(2)
'''
TASK 4: Leap Year
Determine if a year is a leap year or not.
'''
Year =int(input('Enyer birth year'))
if Year % 4 == 0:
    print("Congrats, you were on a leap year")
else:
    print('Sorry, you were not born on a leap year')
'''
TASK 5: Vowel or Consonant:
Identify if a character is a vowel or consonant.

EXTRA CREDIT: Tell the user if they did not enter a valid letter
'''

GG = input('asdfgh')

vowel = ['a' , 'e' , 'i' , 'o' , 'u']

for letter in vowel:
    if letter in GG:
        print('yes')
        break
    else:
        print('nuh uh')
        break