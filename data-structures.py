# storing multiple values together
# Lists, Dictionaries, Tuples, Sets

# Lists

my_list = ["apple", "orange", "banana", "cherry"]
my_list.append("mango")
my_list.remove("orange")
print(my_list)
print(type(my_list))

print(my_list[-1]) # last element
print(my_list[-2]) # second last element
print(my_list[0:2]) # first two elements
print(my_list[2:]) # last two elements
print(my_list[:2]) # first two elements
print(my_list[:]) # all elements
print(len(my_list)) # length of list
print(my_list[::2]) # print every second element

print("============================")

# List of different data types
age = 30
has_license = True
my_list1 = ["Monty", age, has_license, 20.5]
print(my_list1)
print(my_list1[2]) # Accessing list elements
print(type(my_list1[2]))

print("===========================")

# Dictionaries
my_dict = {}

person = {
    "name" : "Monty",
    "age": 35,
    "city": "Bangalore",
    "is_learner": True
}

print(person)
print(type(person))

person["has_license"] = True
print(person)

# Accessing elements
print(person["name"])
print(person["age"])
print(person["city"])
print(person["is_learner"])

del person["has_license"]
print(person)

print(person.keys())
print(person.values())
print(person.items())

if "name" in person:
    print("name found!")

# Update multiple values
person.update({"age": 36, "job": "Engineer", "country": "India"})
print(person)

print("===========================")

# Tuples - immutable sequences

coordinates = (10.0, 20.0)

print(coordinates)
print(type(coordinates)) # <class 'tuple'>

print(coordinates[0])
print(coordinates[1])

# TypeError: 'tuple' object does not support item assignment
# coordinates[0] = 12.0
# print(coordinates)

print("===========================")

# Sets - Unordered, Mutable, No duplicates
# 2 ways  - set() or curly braces

empty_set = set()
print(empty_set)
print(type(empty_set)) # <class 'set'>

scores = [85, 90, 92, 90, 85, 98]
my_numbers_set = set(scores)
print(my_numbers_set)
print(type(my_numbers_set))

fruits = set(["apple", "banana", "cherry"])
print(fruits)
print(type(fruits))

# remove duplicates
numbers = {1, 4, 3, 4, 8, 2, 3}
print(numbers) # {1, 2, 3, 4, 8} removes the duplicates
print(type(numbers)) # <class 'set'>

colors = {"red", "green", "yellow"}
# colors.remove("blue") # throws error
colors.discard("blue") # does not throw error
print(colors)