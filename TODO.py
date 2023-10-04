Todo = []
while (1):
    print('What are my Todos:')
#Printing out what my Todos are 
todo = input['Would you like to add, remove, or check your todos']
#using the [] I use it to store multiple values in a single location,
#and are apart of the iterable family
if (todo == 'add' or todo == 'Add'):
    added = input('What do you want to add')
    Todo.append(added)
    print(Todo)
elif (todo == 'remove' or todo == 'Remove'):
    remove = int(input('Which numbered item would you like to remove from your Todos?'))
    del Todo [remove - 1]
    print(Todo)
elif (todo == 'check' or todo == 'Check'):
    print(Todo)
else:
    print('The command you input was invalid try agaim!')
