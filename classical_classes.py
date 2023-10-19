"""
Task 1: People Class
Define a class called Person with attributes name and age.
Then, write a method within the class to introduce the person with their name and age.

Create a new object using this new class, and call the method you created.
"""
class Person:

   def __init__(self, name, age):
     self.name = name
     self.age = age
     
     def hello (self):
        print(self.name)
        print(self.age)

        Shammy = Person(str("Shammy"), 17)
        Shammy.hello()

"""
Task 2: Animals Speak
Create a base class Animal with a empty method called speak. 

Then create two subclasses, Dog and Cat, each with their own speak method. 

Create objects using these subclasses and call the speak method.
"""
class Animal():
   def speak(self):
      print()
      class Dog(Animal):
         def speak(self):
            print("woof")

            speak = Dog()
            speak.speak()

            class cat(Animal):
               def speak(self):
                  print("meow")
                  speak = cat
                  speak.speak

"""
Task 3: Banking
Create a class BankAccount with attributes balance and owner. 

Include methods for depositing and withdrawing money, which should modify the balance attribute.

Test these methods with instances of the class.
"""