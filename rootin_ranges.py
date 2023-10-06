"""
Exercise 1:
Write a program to print numbers from 1 to 10 using a for loop.
"""
for x in range(1, 11):
    #This for loop is in a range this condition starts the first number
    #to the last number which is the given range
    print(x)
    #This print prints out x which is used to print 1-11
"""
Exercise 2:
Write a program to count by 10s from 900 to 1000
"""
for x in range(900, 1000, 10):
    print(x)
    #Starting off at 900 I was meant to keep counting by 10s
    #until the code eventually reached to 1000 then stopped.
"""
Exercise 3:
Write a program that counts form 1-100 by 9
"""
for x in range(1, 100, 9 ):
    print(x)
    #The starting range is 1 and the last number 9 is what I am counting by
    #until I hit 100 by just counting by 9s
"""
Exercise 4:
Write a program to calculate the sum of all numbers from 1 to 10 using a for loop.
"""
sum = 0
for x in range(1, 11):
    sum += x
    print(sum)
    print('---------')
"""
Excercise 5:
Uncomment the following code and run it. Then answer the following:
- What is the ouput of the code?

- Explain the iterative process that this code executes to get that output
"""
rows = 5
for i in range(rows):
    for j in range(i+1):
        print('*', end=' ')
        print()
        #The code kept outputting * over and over
        #The code kept adding on and on multiple times and counted ever row
        #by one * so the first row with have one *
        #and the last row would have five *