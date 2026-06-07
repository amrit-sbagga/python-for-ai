
def greet():
    print("Hello!!!!")

greet()


def calculate_total():
    pass

calculate_total()


def func1():
   # Alternative to pass
   ...

# Works on same line too
def func2(): ...          
 # Does nothing if called
func1()                  
func2()


def check_weather():
    temperature = 25
    if temperature > 25:
        print("Hot")
    else:
        print("Cold")

check_weather()


# with parameters
def greet(name="Monty"):
    print(f"Hello {name}!!!!")

greet()
greet("Amrit")
greet("Amrit Bagga")


def greet1(first_name, last_name="Bagga"):
    print(f"Hello {first_name} {last_name}!!!!")

greet1("Amrit")
greet1("Amrit", "Singh")
greet1(last_name="Singh", first_name="Amrit")

# Keyword arguments
def create_profile(name, age, city):
    print(f"{name} is {age} years old and lives in {city}.")

create_profile("Amrit", 22, "Bangalore")
create_profile(age=22, name="Amrit", city="Bangalore")
create_profile("Amrit", city="Bangalore", age=22)
create_profile(city="Bangalore", age=22, name="Amrit")


# Return 
def add_return(a, b):
    return a + b

result = add_return(10, 20)
print(result)

def simple_function():
    numbers = [1, 2, 3, 4, 5]
    first_number = numbers[0]
    last_number = numbers[-1]
    return first_number, last_number

f, l = simple_function()
print(f)
print(l)