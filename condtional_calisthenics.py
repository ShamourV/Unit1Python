'''
Exercise 1:
Check if an integer is even and greater than 10.
Return True if both conditions are met, False otherwise.
'''

'''
Exercise 2:
Determine the ticket price based on age and student status.
Price is $10 if under 18 or a student, $20 otherwise.
'''

'''
Exercise 3:
Prompt the user to enter a fruit name. Check if the fruit is in the list. 
If it is, print "Yes, that fruit is in the list." 
If it's not, print "No, that fruit is not in the list."
'''
fruit_names = ("watermelon" , "cucumber" , "mango")
if 'watermelon' 'cucumber' 'mango' in fruit_names:
    print("Yes, that fruit is in the list")
else:
    print('Thats not in the list!')
'''
Exercise 4:
Check if a year is a century year and a leap year.
'''
Year =int(input('Enyer birth year'))
if Year % 4 == 0:
    print("Congrats, you were on a leap year")
else:
    print('Sorry, you were not born on a century year')
if Year % 100 == 0:
    print("Congrats, you were on a century year")
else:
    print('Sorry, you were not born on a century year')
'''
Exercise 5:
Calculate the cost of shipping for an online order based on the order weight and destination zone. 
The shipping cost is $5 per kilogram for Zone A and $7 per kilogram for Zone B. 
If the order weight is less than 0 kg, return an error message.
'''

weight = int(input("What is the weight"))
zone = input('What is the zone you are shipping to')
if zone == 'zone A':
    print(weight * 7)
elif zone == 'zone b':
    print(weight * 5)
elif weight == 0:
    print('Invalid weight')

'''
Exercise 6:
Determine the type of a triangle based on side lengths.
Equilateral, Isosceles, Scalene, or Not a triangle.
'''