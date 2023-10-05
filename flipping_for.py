"""
Exercise 1:
Write a program to print each character of a given string using a for loop.
"""
Brotha = "Man , Can , Less than"
#First I would make a string for the loop
for x in Brotha:
    print(x)    
"""
Exercise 2:
Write a program to calculate the sum of elements in a list using a for loop.
"""
infrit = [3, 7, 19, 21, 5]
sum = 0
for x in infrit:
    print(sum)
"""
Exercise 3:
Write a program to find and print the length of each word in a sentence using a for loop and a list.
"""
T = 'I am here'
T = T.split(" ")
for w in T:
    print(w)
    print(len(w))
"""
Excercise 4:
Write a program that creates a dictionary (atleast 4 key:value pairs) and then
iterates through a dictionary and prints the result

In a comment, answer the following, what do you notice about the output of your code?
Is it what you expected?
"""

random = {
   'pap' : 4,
   'bap' : 3,
   'sap' : 5,
   'map' : 9
}
for x in random:
    print(random)
    #This is not what I expected, I was expecting each  key to be printed out
    #a certain number of times.