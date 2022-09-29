""" Your task is to create slightly different animals, which should have the same properties and methods, 
but should implement the talk() method in different ways. For example. should a cat (when talking) say "Moew", 
a dog "Woff", a fish "Blub" and a Cow "Muuu". 
They should all share the following (private) properties: name (string), age (number), food (list of strings), 
and have the functions get_name, set_name, get_age, set_age, get_food, add_food, remove_food. Finally, all the 
animals must have the talk function, but that function must, as I said, be implemented in each animal, as the 
animals have different sounds.
When you have made the classes, create instances of the classes and put in a list - loop through the list - 
and let all the animals talk! :) """
class Animal:
    def __init__(self, name, age):
        self.__name = name
        self.__food = []
        self.__age = age
    def get_name(self):
      return self.__name

    def set_name(self, name):
      self.__name = name
    def get_age(self):
      return self.__age
    def set_age(self, age):
      self.__age = age
    def get_food(self):
      return self.__food
    def add_food(self, food):
      self.__food.append(food) 
    def remove_food(self, item):
      self.__food.remove(item)


    def talk(self):
        print("talk")

class Dog(Animal):
    def __init__(self, name, food, age):
        super().__init__(name, food, age)

    def talk(self):
        print("Wooff")
class Cat(Animal):
    def __init__(self, name, food, age):
        super().__init__(name, food, age)

    def talk(self):
        print("Meow")
class Fish(Animal):
    def __init__(self, name, food, age):
        super().__init__(name, food, age)

    def talk(self):
        print("Blub")
class Cow(Animal):
    def __init__(self, name, food, age):
        super().__init__(name, food, age)

    def talk(self):
        print("Muuu")

my_dog = Dog("Puppy", "milk", 1)
my_cat = Cat("Kitty", "milk", 2)
my_cow = Cow("calf", "milk", 3)
my_fish = Fish("tilapia", "crumbs", 4)

my_list = [my_cat, my_cow, my_dog, my_fish]
for i in range(len(my_list)):
  i.talk()

"""

The snail climbs up 7 feet each day and slips back 2 feet each night. How many days will it take the snail 
to get out of a well with the given depth?. Using python, write a function to solve this problem. 
Sample Input: 31 Sample Output: 6

Write a function that takes a list of numbers and returns the largest number in the list.

Write a program that accepts a sentence and calculate the number of upper case letters and
 lower case letters. Suppose the following input is supplied to the program: Hello world! 
 Then, the output should be: UPPER CASE 1 LOWER CASE 9

Using Object Oriented Programming, write a program that implements a dice game. 
The game should have two players, and each player should have a name and a score. 
The game should have a method called play that takes two players as arguments and simulates the game.
The game should be played as follows:

Each player rolls a die.
The player with the highest roll wins the round.
The winner gets one point added to their score.
The game ends when one player has 5 points.
The player with the most points at the end of the game wins.
The program should print out the winner's name and score.
If a player rolls a 6, they get an extra roll. If they roll a 6 again, they get another extra roll. 
If they roll a 6 a third time, they get an extra roll, but their turn ends.
Write a Python program that lists out all the default as well as custom properties of the class.

Write a Program in Python to implement a Stack Data Structure using Class and Objects, with push, pop, 
and traversal methods.

Using list comprehension, write a program that takes a list of numbers and returns a list of the squares 
of the numbers.

Using only functions and lists, Implement a queue data structure. The queue should have the following methods:
 enqueue, dequeue, and size. The queue should be "first-in-first-out" (FIFO).

Using a while loop, implement merge sort algorithm.
"""