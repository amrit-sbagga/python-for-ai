
# Import whole module
import math

math.sqrt(16)

# import specific function from module
from math import sqrt, pi

print(sqrt(16))
print(pi)


import random

number = random.randint(1, 10)
print(number)
choice = random.choice(["cat", "dog", "bird"])
print(choice)


from datetime import datetime
now = datetime.now()
print(now)

today = datetime.today().date()
print(today)


import os
current_directory = os.getcwd()
print(current_directory)



import json
data = { "name" : "Monty", "age" : 32 }
json_string = json.dumps(data)
print(json_string)