#name code
name = input('What is your name? ')
color = input('What is your favorite color? ')
print(f'{name} likes {color}')

#weight code
weight = input('What is your weight in pounds? ')
kilogram = int(weight) * 0.45
print(kilogram)

#if code
name = "Jake"
if (len(name)) < 3:
    print("Name must be at least 3 characters")
elif len(name) > 50:
    print("Name must be less than 50 characters")
else:
    print("Name looks good")

#Weight code
weight = int(input("Weight: "))
unit = input('(L)bs or (K)g: ')
if unit.upper() == "L" :
    converted = weight * 0.45
    print(f"You are {converted} kilos")
else:
    converted = weight / 0.45
    print(f"You are {converted} pounds")
    
#loop
    i = 1
while i <= 5:
    print(i)
    i = i + 1
print("done")

#guess game
secret_number = 5
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input('Guess: '))
    guess_count += 1
    if guess == secret_number:
        print('You won')
        break
else:
    print("You lost")
    
    
#car game
command = ""
started = False
while True:
    command = input("> ").lower()
    if command == 'start':
        if started:
            print("Car is already started")
        else:
            started = True
            print("Car started....")
    elif command == "stop":
        if not started:
            print("Car is already stopped")
        else:
            started = False
            print("Car stopped.")
    elif command == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to quit
        """)
    elif command == "quit":
        break
    else:
        print("Sorry, I don't understand that!")
        
#L shape
numbers = [2, 2, 2, 2, 5]
for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += 'x'
    print(output)
    
#f shape
numbers = [5, 2, 5, 2, 2]
for x_count in numbers:
    print('x' * x_count)
    
# max number
numbers = [1, 5, 9, 2, 4]
# 0 = 1
max = numbers[0]
#is 1 > 5, # is 5 >     9
for number in numbers:
    if number > max:
        max = number
print(max)

#matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for row in matrix:
    for item in row:
        print(item)
        
#removing duplicates
numbers = [2, 2, 4, 6, 3, 4, 6, 1]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)


#Phone number
phone = input("Phone: ")
digits_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four"
}
output = ""
for ch in phone:
    output += digits_mapping.get(ch, "!") + " "
print(output)

#emoji converter

message = input(">")
words = message.split(' ')
emojis = {
    ":)": "😊",
    ":(": "😔"
}
output = ""
for word in words: 
    output += emojis.get(word, word) + " "
print(output)

#modified emoji converter
def emoji_converter(message):

    words = message.split(" ")
    emojis = {
        ":)": "😊",
        ":(": "🥲"
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output

        
message = input(">")
result = emoji_converter(message)
print(result)

#functions
def greet_user(name):
    print(f"Hello {name}")
    print(f"What's good")
    
    
print("Start")
greet_user("John")
greet_user("Mary")
print("Finish")

#number
def square(number):
    return number * number


print(square(3))

#Try and except
try:
    age = int(input("Age: "))
    income = 20000
    risk = income / age
    print(age)
except ZeroDivisionError:
    print("Age cannot be zero")
except ValueError:
    print('Invalid Error')
    

#class point
class Point:
    def move(self):
        print("move")
        
    def draw (self):
        print("draw")
        
        
point1 = Point()
point1.x = 10
point1.y = 20
point1.draw()

point2 = Point()
point2.x = 1
print(point2.x)

#class person
class Person:
    def __init__(self, name):
        self.name = name
        
    def talk(self):
        print("talk")
        
john = Person("John Smith")
print("john.name")
john.talk()

#class

class Mammal:
    def walk(self):
        print("walk")
    


class Dog(Mammal):
    def bark(self):
        print("bark")


class Cat(Mammal):
    def be_annoying(self):
        print("annoying")
        

cat1 = Cat()
cat1.be_annoying()

dog1 = Dog()
dog1.bark()


#random
import random

class Dice:
    def roll(self):
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        return first, second


dice = Dice()
print(dice.roll()) 

#Paths
from pathlib import Path

path = Path()
for file in path.glob('*.py'):
    print(file) 