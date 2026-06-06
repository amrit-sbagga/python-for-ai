# Data types
# Numbers -> Integers & Floats
# Strings -> "Hello"
# Lists -> [1, 2, 3, 4]
# Tuples -> (1, 2, 3, 4)
# Dictionaries -> {"name": "John", "age": 30}
# Boolean -> True/False


my_long_string = """
My name is Amrit
My last name is Bagga
"""
print(my_long_string)

# f-strings (formatted string literals)
name = "Monty"
last_name = "Bagga"
new_name = f"My name is {name} {last_name}"
print(new_name)

# Length
print(len(my_long_string))


# Booleans
is_logged_in = True
is_admin = False
print(is_logged_in)
print(is_admin)

# if-else statements
if is_logged_in:
    print("Welcome back, " + name + "!")
else:
    print("Please log in")