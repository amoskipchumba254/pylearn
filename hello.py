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

    