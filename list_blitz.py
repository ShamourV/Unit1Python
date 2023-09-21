"""
Task 1: Create a list
Create a list with 4 elements and print it.
"""
my_list = ["Drinks", "Dragon Ball" "Money" "Food"]
print(my_list)
# I added different items to my list and used the print function to print it
# on the terminal
"""
Task 2: Add Element to a List
Add an element to the end of the list. Print the updated 
list.
"""
my_list.append('Celery')
print(my_list)
# Using append I was able to add Celery to my list
"""
Task 3: Remove Element from a List
Remove a specific element from the list. Print the 
updated list.
"""
my_list.remove ("Food")
print(my_list)
# remove is one of the ways you can remove an item from your list
"""
Task 4: Modify Element in a List
Modify an element at a specific index with a new value. 
Print the updated list.
"""
my_list[1] = "1"
print(my_list)
"""
Task 5: Append Multiple Elements to a List
Append multiple elements to the end of the list. Print 
the updated list.
"""
my_list.append("Koolaid")
my_list.append("watermelon")
print(my_list)
"""
Task 6: Delete Element at a Specific Index
Delete an element at a specific index. Print the updated 
list.
"""
del my_list[2]
print(my_list)
"""
Task 7: Subsetting lists
Create a new variable equal to the first 2 items of your list
Then print out the new variable
"""
JK_Q = my_list[:3]
print(JK_Q)

"""
Task 8: Extend a List
Extend the list with the elements of another list. Print 
the updated list.
"""
JK_Q = ['Bread' , 'Milk']
JK_Q = my_list + JK_Q
print(my_list)