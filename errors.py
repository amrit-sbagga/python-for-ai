# compile time error if x not defined
x=2
if x < 5:
    print("x is less than 5")

# runtime error
# result = 10 / 0 # ZeroDivisionError

# TypeError: can only concatenate str (not "int") to str
# "Hello" + 5

try:
    # pyrefly: ignore [division-by-zero]
    result = 10 / 0
except:
    print("Error: Cannot divide by zero")
    print("Please provide a non-zero number")

try:
    "Hello" + 5
except ValueError:
    print("Error!!")
    print("Please provide a string or int")
except TypeError:
    print("Error: Cannot concatenate str and int")
    print("Please provide a string or int")
except:
    print("Error: Something went wrong")
finally:
    print("Finally block executed")