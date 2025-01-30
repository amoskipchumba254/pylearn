message = "hello python world!"
print(message)

message = "hello python crash course world!"
print(message)

name = "ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())


first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)
print(f"Hello, {full_name.title()}!")
message = f"Hello, {full_name.title()}!"
print(message)

print("Languages:\n\tPython\n\tC\n\tJavaScript")
favorite_language = " python "
favorite_language = favorite_language.rstrip()
print(favorite_language)

favorite_language = " python"
favorite_language = favorite_language.lstrip()
print(favorite_language)

favorite_language = " python "
favorite_language = favorite_language.strip()
print(favorite_language)

# single and double quotes, double quotes with apostrophe
message = "one of python's strengths is its diverse community."
print(message)

first_name = "amos"
last_name = "kipchumba"
full_name = f"{first_name} {last_name}"
print(f"Hello, {full_name.title()} would you like to learn some python today?")

first_name = "amos"
last_name = "kipchumba"
full_name = f"{first_name} {last_name}"
print(full_name.lower())
print(full_name.upper())
print(full_name.title())

first_name = "Albert"
last_name = "Einstein"
full_name = f"{first_name} {last_name}"
famous_quote = "A person who never made a mistake never tried anything new."
print(f'{full_name.title()} once said, "{famous_quote}"')

famous_person = "Albert Einstein"
message = "A person who never made a mistake never tried anything new."
print(f'{famous_person.title()} once said, "{message}"')

x = 2
y = 3
c = 4
print(x+y*c)
print((x+y)*c)

m = 0.1
n = 0.2
print(m+n)
print(2*0.1)

age = 23
message = "Happy " + str(age) + "rd Birthday!"
print(message)

a = 2
b = 4
c = 6
d = 8
e = 10
f = 32
print(a + c)
print(e - a)
print(b * a)
print(f / b)

favorite_number = 7
message = f"My favorite number is {favorite_number}."
print(message)

# lists
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

# accessing elements in a list
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0].title())   
print(bicycles[1].title())
print(bicycles[2].title())
print(bicycles[-1].title())

# using individual values from a list  
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
message = f"my first bicycle was a {bicycles[0].title()}."
print(message)
motorcycles = ['honda', 'yamaha', 'suzuki'] 
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles.append('ducati')
print(motorcycles)

motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
motorcycles.append('ducati')
motorcycles.append('kawasaki')
motorcycles.append('bmw')

print(motorcycles)
 
# inserting elements into a list
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')
print(motorcycles)

#removing elements from the list
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

del motorcycles[0]
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
  
del motorcycles[1]
print(motorcycles)

# removing the item using the pop method
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}")

# popping any item from the list
motorcycles = ['honda', 'yamaha', 'suzuki']

first_owned = motorcycles.pop(0)
print(f"The first motorcycle i owned was a {first_owned.title()}.")

# removing an item by value
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")

invited_guest = ['amos', 'kipchumba', 'victor', 'peter', 'mercy']
print(invited_guest)

print(f"Hello {invited_guest}! You are invited to dinner at my place.")

invited_guest = ['amos', 'kipchumba', 'victor', 'peter', 'mercy']
print(invited_guest)

print(f"Hello, {invited_guest[0].title()} will not be able to make it to dinner.")

invited_guest = ['amos', 'kipchumba', 'victor', 'peter', 'mercy']
print(invited_guest)
invited_guest[0] = 'jane'
print(invited_guest)

invited_guest = ['amos', 'kipchumba', 'victor', 'peter', 'mercy']
print(invited_guest)

for guest in invited_guest:
    print(f"Hello {guest}, you are invited to dinner at my place, see you there!")
    
invited_guest = ['amos', 'kipchumba', 'victor', 'peter', 'mercy']   
print("Good news! I just found a bigger dinner table.")
invited_guest.insert(0, 'jane')
middle_index = len(invited_guest)//2
invited_guest.insert(middle_index, 'james')
invited_guest.append('susan')

for guest in invited_guest:
    print(f"hello {guest.title()}, you are invited to dinner at my place!")

# organizing a list
# sorting a list permanently with the sort() method
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)

# sorting a list temporarily with the sorted() function
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)

# printing a list in reverse order
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)

cars.reverse()
print(cars)

places_to_visit = ['india', 'paris', 'new york', 'london', 'tokyo']
print(places_to_visit)

print("\nlist in alphabetical order:")
print(sorted(places_to_visit))

print("\noriginal list after using sorted():")
print(places_to_visit)

print("\nlist in reverse alphabetical order:")
print(sorted(places_to_visit, reverse=True))

print("\noriginal list after using sorted() in reverse:")
print(places_to_visit)

places_to_visit.reverse()
print("\nlist after using reverse():")
print(places_to_visit)

places_to_visit.sort()
print("\nlist after using sort() to arrange in alphabetical order:")
print(places_to_visit)

places_to_visit.sort(reverse=True)
print("\nlist after using sort() to arrange in reverse alphabetical order:")
print(places_to_visit)

invited_guest = ['amos', 'kipchumba', 'victor', 'peter', 'mercy']
for guest in invited_guest:
    print(f"hello {guest.title()}, you are invited to dinner at my place!")
    
number_of_guests = len(invited_guest)
print(f"\nI am inviting {number_of_guests} people to dinner.")

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)
    
# a closer look at looping
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")
    
print("Thank you, everyone. That was a great magic show!")

favorite_pizzas = ['pepperoni', 'margherita', 'bbq chicken']

for pizza in favorite_pizzas:
    print(f"I like {pizza} pizza.")
    
print("\nI really enjoy trying different types of pizza.")
print("Pizza is one of my favorite foods because is is so versatile and delicious.")
print("I could eat pizza any day of the week. I really love pizza!")

# making numerical lists
for value in range(1, 5):
    print(value)
    
numbers = list(range(1, 6))
print(numbers)

# using to list even numbers between 1 and 10
even_numbers = list(range(2, 11, 2))
print(even_numbers)

# first 10 square numbers
squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
    
print(squares)  

squares = []
for value in range(1, 11):
    squares.append(value ** 2)
    
    
print(squares)  

# using list comprehension
squares = [value ** 2 for value in range(1, 11)]
print(squares)

# counting 1to 20
for value in range(1, 21):
    print(value)
    
# counting from 1 to 1,000,000 using min(), max() and sum()
numbers = list(range(1, 100001))
print(min(numbers))
print(max(numbers))
print(sum(numbers))

# odd numbers
add_numbers = list(range(1, 21, 2))
for number in add_numbers:
    print(number)
    
# threes
threes = list(range(3, 31, 3))
for number in threes:
    print(number)
    
# cubes 
cubes = []
for value in range(1, 11):
    cubes.append(value ** 3)
    print(cubes)
    
#cube compression
cubes = [value ** 3 for value in range(1, 11)]
print(cubes)

# slicing a list 
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[1:4])
print(players[:4])
print(players[2:])
print(players[-3:])

# looping through a slice
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())
    
# copying a list
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

# initial list of items
items = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape']

# adding lines to meet the requirements

print("The first three items in the list are:")
print(items[:3])

# print three items from the middle of the list
print("three items from the middle of the list are:")
middle_index = len(items)//2
print(items[middle_index-1:middle_index+2])

# print the last three items in the list
print("the last three items in the list are:")
print(items[-3:])

# tuples
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# looping through all values in a tuple
dimensions = (200, 50)
for dimension in dimensions:
    print(dimension)
    
# writing over a tuple
dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)
    
dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)
    
# foods
foods = ('pizza', 'falafel', 'carrot cake', 'cannoli', 'ice cream')
for food in foods:
    print(food)
    
# revised foods
foods = ('pizza', 'falafel', 'carrot cake', 'apple', 'banana')
for food in foods:
    print(food)

# if statements
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

# checking for inequality
requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
    print("Hold the anchovies!")  
# numerical comparisons
answer = 17

if answer != 42:
    print("That is not the correct answer. please try again!")
    
# checking whether a value is not in a list
banned_users = ['andrew', 'carolina', 'david']
user = "marie"

if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")

# boolean expressions
car = 'subaru'
fruit = 'apple'
age = 25
temperature = 30
is_raining = True

# true tests
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\nIs fruit == 'apple'? I predict True.")
print(fruit == 'apple')

print("\nIs age > 25? I predict True.")
print(age > 25)

print("\nIs temperature < 40? I predict True.")
print(temperature < 40)

print("\nIs is_raining == True? I predict True.")
print(is_raining == True)

# false tests
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

print("\nIs fruit == 'banana'? I predict False.")
print(fruit == 'banana')

print("\nIs age < 25? I predict False.")
print(age < 25)

print("\nIs temperature > 35? I predict False.")
print(temperature > 35)

print("\nIs is_raining == False? I predict False.")
print(is_raining == False)

# if statements
age = 19
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
    
# if-else statements
age = 17
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")
    
# if-elif-else chain
age = 12
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $25.")
else:
    print("Your admission cost is $40.")
    
age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40

print(f"Your admission cost is ${price}")

# using multiple elif blocks
age = 65

if age < 4:
    price = 0
elif age < 18:  
    price = 25
elif age < 65:              
    price = 40
else:
    price = 20

print(f"Your admission cost is ${price}.")
 
# testing multiple conditions
requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")
    
print("\nFinished making your pizza!")   

# stages of life
age = 65

if age < 2:
    stage = 'baby'
elif age < 4:
    stage = 'toddler'
elif age < 13:
    stage = 'kid'
elif age < 20:
    stage = 'teenager'
elif age < 65:
    stage = 'adult'
else:
    stage = 'elder'
    
print(f"You are a/an {stage}.")

# using if statements with lists
# checking for special items
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    print(f"Adding {requested_topping}.")
    
print("\nFinished making your pizza!")

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print(f"Adding {requested_topping}.")
        
print("\nFinished making your pizza!")

# checking that a list is not empty
requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")
    
# using multiple lists
available_toppings = ['mushrooms', 'olives', 'green peppers',
                      'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")
    
print("\nFinished making your pizza!")

# usernames

# list of current users
current_users = ['amos', 'kipchumba', 'victor', 'peter', 'mercy']

# list of new users
new_users = ['amos', 'kipchumba', 'victor', 'jane', 'james']

#convert current_users to lowercase
current_users_lower = [user.lower() for user in current_users]

# loop through new_users
for user in new_users:
    if user.lower() in current_users_lower:
        print(f"Sorry {user}, that username is taken.")
    else:
        print(f"Great, {user} is available.")
        
# dictionaries
# a simple dictionary
alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

alien_0 = {'color': 'green', 'points': 5}
new_points = alien_0['points']
print(f"You just earned {new_points} points!")

alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# starting with an empty dictionary
alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5

print(alien_0)

# modifying values in a dictionary
alien_0 = {'color': 'green'}
print(f"The alien is {alien_0['color']}.")
alien_0['color'] = 'yellow'

print(f"The alien is now {alien_0['color']}.")

# tracking the position of an alien that can move at different speeds
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position: {alien_0['x_position']}")

# move the alien to the right
# determine how far to move the alien based on its current speed
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # this must be a fast alien
    x_increment = 3

# the new position is the old position plus the increment
alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"New position: {alien_0['x_position']}")

# removing key-value pairs
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0['points']
print(alien_0)

favorite_language = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

language = favorite_language['sarah'].title()
print(f"Sarah's favorite language is {language}.")

# using get() to access values
alien_0 = {'color': 'green', 'speed': 'slow'}

point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)

# looping through all key-value pairs
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi'
}
for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")
    
favorite_language = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

for name, language in favorite_language.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")
    
# looping through all the keys in a dictionary
favorite_language = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

for name in favorite_language.keys():
    print(name.title())
    
favorite_language = {
    
}

friends = ['phil', 'sarah']
for name in favorite_language.keys():
    print(name.title())

    if name in friends:
        language = favorite_language[name].title()
        print(f"\t{name.title()}, I see you love {language}!")
        
if 'erin' not in favorite_language.keys():
    print("Erin, please take our poll!")
    
# looping through a dictionary's keys in order
favorite_language = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

for name in sorted(favorite_language.keys()):
    print(f"{name.title()}, thank you for taking the poll.")
    
# looping through all values in a dictionary
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())
    
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())

# nesting dictionaries
# a list of dictionaries
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)
    
# make an empty list for storing aliens
aliens = []

# make 30 green aliens
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

# show the first 5 aliens
for alien in aliens[:5]:
    print(alien)
print("...")

# show how many aliens have been created
print(f"Total number of aliens: {len(aliens)}")

# make an empty list for storing aliens
aliens = []

# make 30 green aliens
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
        
# show the first 5 aliens
for alien in aliens[:5]:
    print(alien)
print("...")
    
# store information about a pizza being ordered 
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese']
}

# summarize the order
print(f"You ordered a {pizza['crust']}-crust pizza " 
      "with the following toppings:")

for topping in pizza['toppings']:
    print("\t" + topping)
    
favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell']
}

for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")

# a dictionary in a dictionary
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton'
    },
    
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris'
    }
}

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']
    
    print(f"\tFull_name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")

# introducing while loops
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

# using continue in a loop
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    
    print(current_number)
    
# avoiding infinite loops
x = 1
while x <= 5:
    print(x)
    x += 1
    
# moving items from one list to another
# start with users that need to be verified,
# and an empty list to hold confirmed users
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

# verify each user until there are no more unconfirmed users
# move each verified user into the list of confirmed users
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    
    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)
    
# display all confirmed users
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
        
        
# removing all instances of specific values from a list
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')
    
print(pets)

# chapter8 functions
# defining a function
def greet_user():
    """Display a simple greeting."""
    print("Hello!")

greet_user()

# passing information to a function
def greet_user(username):
    """Display a simple greeting."""
    print(f"Hello, {username.title()}!")

greet_user('jesse')

# positional arguments
def describe_pet(animal_type, pet_name):
    
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
    

describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')

# keyword arguments
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
    
describe_pet(animal_type='hamster', pet_name='harry')

# default values
def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(pet_name='willie')

# returning a simple value
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

# making an argument optional
def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('john', 'lee', 'hooker')
print(musician)

# returning a full name when the middle name is optional
def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)

# returning a dictionary
def build_person(first_name, last_name):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    return person

musician = build_person('jimi', 'hendrix')
print(musician)

# passing a list
def greet_users(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)
        
usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)

# modifying a list in a function
# start with some designs that need to be printed
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

# simulate printing each design, until none are left
# move each design to completed_models after printing
while unprinted_designs:
    current_design = unprinted_designs.pop()
    
    # simulate creating a 3D print from the design
    print(f"Printing model: {current_design}")
    completed_models.append(current_design)
    
# display all completed models
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)
    
# modifying a list using two functions
def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until none are left.
    Move each design to completed_models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        
        # simulate creating a 3D print from the design
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

# passing an arbitrary number of arguments
def make_pizza(*toppings):
    """Print the list of toppings that have been requested."""
    print(toppings)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

# looping through all the values
def make_pizza(*toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

# mixing positional and arbitrary arguments
def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# using arbitrary keyword arguments
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics')
print(user_profile)

# importing the entire module 
import pizza

pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# importing specific functions
from pizza import make_pizza

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# using as to give a function an alias
from pizza import make_pizza as mp

mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')

# using as to give a module an alias
import pizza as p

p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# importing all functions in a module
from pizza import *

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# creating and using a class
# creating the dog class
class Dog:
    """A simple attempt to model a dog."""
    
    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age
        
    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")
        
    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")

my_dog = Dog('willie', 6)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")

# the car class
class Car:
    """A simple attempt to represent a car."""
    
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())

# setting a default value for an attribute
class Car:
    """A simple attempt to represent a car."""
    
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")
        
my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()

# ,\modifying attribute's value through a method
class Car:
    """A simple attempt to represent a car."""
    
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")
        
    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
            
            
my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())

my_new_car.update_odometer(23)
my_new_car.read_odometer()

# incrementing an attribute's value through a method
class Car:
    """A simple attempt to represent a car."""
    
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")
        
    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
            
    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles
        
        
my_used_car = Car('subaru', 'outback', 2015)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23_500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()

# inheritance
# the __init__() method for a child class

class Car:
    """A simple attempt to represent a car."""
    
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")
    
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
            
    def increment_odometer(self, miles):
        self.odometer_reading += miles
class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    
    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)
        super().__init__(make, model, year)


my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())

# defining attributes and methods for the child class
class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    
    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery_size = 75
        
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")
        
my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()

# overriding methods from the parent class
class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    
    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery_size = 75
        
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")
        
    def fill_gas_tank(self):
        """Electric cars don't have gas tanks."""
        print("This car doesn't need a gas tank!")
        
# instances asa attributes
class Car:
    """A simple attempt to represent a car."""
    
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")
    
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
            
    def increment_odometer(self, miles):
        self.odometer_reading += miles

class Battery:
    """A simple attempt to model a battery for an electric car."""
    
    def __init__(self, battery_size=75):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size
        
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")
        
    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
            
        print(f"This car can go about {range} miles on a full charge.")


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    
    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()
        
my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

# importing a single class
from car import Car

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()


from car import ElectricCar

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

# importing multiple classes
from car import Car, ElectricCar

my_beetle = Car('volkswagen', 'beetle', 2019)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'roadster', 2019)
print(my_tesla.get_descriptive_name())

# importing the entire module
import car

my_beetle = car.Car('volkswagen', 'beetle', 2019)
print(my_beetle.get_descriptive_name())

my_tesla = car.ElectricCar('tesla', 'roadster', 2019)
print(my_tesla.get_descriptive_name())

# reading an entire file
with open('C:\\Users\\amoki\\OneDrive\\Desktop\\.py tests\\.pytest\\pi_digits.txt') as file_object:
    contents = file_object.read()
print(contents)

with open('C:\\Users\\amoki\\OneDrive\\Desktop\\.py tests\\.pytest\\test.txt') as file_object:
    contents = file_object.read()
print(contents)

filename = 'C:\\Users\\amoki\\OneDrive\\Desktop\\.py tests\\.pytest\\pi_digits.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line)
        
filename = 'C:\\Users\\amoki\\OneDrive\\Desktop\\.py tests\\.pytest\\pi_digits.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())
        
# making a list of lines from a file
filename = 'C:\\Users\\amoki\\OneDrive\\Desktop\\.py tests\\.pytest\\pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())
    
# working with a file's contents
filename = 'C:\\Users\\amoki\\OneDrive\\Desktop\\.py tests\\.pytest\\pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.rstrip()
    
print(pi_string)
print(len(pi_string))

for line in lines:
    pi_string += line.strip()
    
print(pi_string)
print(len(pi_string))

# writing to a file
# writing to an empty file_object
filename = 'programming.txt'

with open(filename, 'w') as file_object:
    file_object.write("I love programming.")
    
# writing multiple lines
filename = 'programming.txt'

with open(filename, 'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")
    
# appending to a file
filename = 'programming.txt'

with open(filename, 'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")
    
# exceptions
# handling the ZeroDivisionError exception
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")
    
# handling the FileNotFoundError exception
filename = 'alice.txt'

try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
        
except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exist.")
    
# analyzing text
filename = 'programming.txt'

try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exist.")
else:
    # count the approximate number of words in the file
    words = contents.split()
    num_words = len(words)
    print(f"The file {filename} has about {num_words} words.")
    
# using json.dump() and json.load()
import json

numbers = [2, 3, 5, 7, 11, 13]

filename = 'numbers.json'
with open(filename, 'w') as f:
    json.dump(numbers, f)
    
# reading data back
import json

filename = 'numbers.json'
with open(filename) as f:
    numbers = json.load(f)

print(numbers)

import json

filename = 'username.json'

with open(filename) as f:
    username = json.load(f)
    print(f"Welcome back, {username}!")

# combining the two programs
import json

# load the username, if it has been stored previously
# otherwise, prompt for the username and store it
filename = 'username.json'
try:
    with open(filename) as f:
        username = json.load(f)
except FileNotFoundError:
    username = input("What is your name? ")
    with open(filename, 'w') as f:
        json.dump(username, f)
        print(f"We'll remember you when you come back, {username}!")
else:
    print(f"Welcome back, {username}!")

# refactoring
import json

def greet_user():
    """Greet the user by name."""
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        username = input("What is your name? ")
        with open(filename, 'w') as f:
            json.dump(username, f)
            print(f"We'll remember you when you come back, {username}!")
    else:
        print(f"Welcome back, {username}!")
        
greet_user()

# refactoring greet user so that it's not doing too much
import json

def get_stored_username():
    """Get stored username if available."""
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username
    
    def greet_user():
        """Greet the user by name."""
        username = get_stored_username()
        if username:
            print(f"Welcome back, {username}!")
        else:
            username = input("What is your name? ")
            filename = 'username.json'
            with open(filename, 'w') as f:
                json.dump(username, f)
                print(f"We'll remember you when you come back, {username}!")
                
greet_user()

def get_new_username():
    """Prompt for a new username."""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username

def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username}!")
        
greet_user()

    
# a passing test
import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """Tests for 'name_function.py'."""
    
    def test_first_last_name(self):
        """Do names like 'Janis Joplin' work?"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')
        
    def test_first_last_middle_name(self):
        """Do names like 'Wolfgang Amadeus Mozart' work?"""
        formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')
        
if __name__ == '__main__':
    unittest.main()
    
# testing a class
from survey import AnonymousSurvey

# define a question, and make a survey
question = "What language did you first learn to speak?"
my_survey = AnonymousSurvey(question)

# show the question, and store responses to the question
my_survey.show_question()
print("Enter 'q' at any time to quit.\n")
while True:
    response = input("Language: ")
    if response == 'q':
        break
    my_survey.store_response(response)
    
# show the survey results
print("\nThank you to everyone who participated in the survey!")
my_survey.show_results()
