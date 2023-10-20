from datetime import date, time, datetime
"""
Exercise 1:
Write a Python program that prints the current date and time using the datetime module.
"""
print(datetime.now())

"""
Exercise 2:
Write a Python program that prints the current date and time using the datetime module.
Using the strftime function format the date in standard U.S. date format (MM/DD/YYYY)
"""
from datetime import datetime

now = datetime.now()

year = now.strftime("%Y")
print('year:', year)

month = now.strftime('%m')
print('month:', month)

day = now.strftime('%d')
print('day:', day)

"""
Exercise 3:
Using the strptime function, convert two strings into dates.
Then find the difference in days between the two.
"""
str_d1 = '2023/10/12'
str_d2 = '2023/12/12'

d1 = datetime.strptime(str_d1, "%Y/%m/%d")
d2 = datetime.strptime(str_d2, "%Y/%m/%d")
delta = d2 - d1
print(f'Difference is {delta.days} days')
"""
Excercise 4:
Write a program that asks the user for their birthdate and calculates their current 
age using the datetime module.
"""
from datetime import datetime, timedelta

# Get the current date
now = datetime.now()

# Ask the user for their date of birth
print("Enter your date of birth (YYYY-MM-DD):")
dob_input = input()

# Parse the user's input into a datetime object
birthday = datetime.strptime(dob_input, "%Y-%m-%d")

# Calculate the difference between the current date and the birthday
difference = now - birthday

# Calculate the person's age in years
age_in_years = difference.days // 365

print(f"You are {age_in_years} years old.")