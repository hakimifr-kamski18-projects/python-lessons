# Unit 06 — the first function
# Run this file with: python3 first_function.py

def greet():
    print("Hello!")
    print("Welcome to Python.")

greet()
greet()
greet()

# DEFINING does not RUN it. The body only runs when you CALL it.
# Delete the three greet lines above and run the file again.
# Nothing happens at all. That is worth seeing.

print()

# The brackets are required even when there is nothing inside them.
# "greet" without brackets is the function itself, not a call to it.
# If you forget them you get NO OUTPUT and NO ERROR, which is confusing.

print()

# ---------------------------------------------------------------
# PARAMETERS let you hand data in.

def greet_person(name):
    print(f"Hello, {name}!")

greet_person("Ada")
greet_person("Grace")

# When greet_person("Ada") runs, "name" becomes "Ada" inside the function.
# It is just a variable that starts out holding whatever you passed.

print()

# A function with a parameter used in arithmetic.
# Note what happens when you pass the wrong TYPE.

def double(number):
    print(number * 2)

double(5)         # 10
double("ab")      # abab (string repetition, from unit 01)
double("5")       # 55 (gluing two strings, NOT maths)

# That last one is the input type problem from unit 02, in a new place.
# The function did exactly what it was told.

print()

# ---------------------------------------------------------------
# Two parameters. Order matters.

def describe(name, age):
    print(f"{name} is {age} years old")

describe("Ada", 36)

# describe(36, "Ada") gives a silly result rather than an error.
# Python does not check whether your argument order makes sense.

print()

# ---------------------------------------------------------------
# Default values. Parameters with defaults must come LAST.

def greet_with(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet_with("Ada")                     # Hello, Ada!
greet_with("Ada", "Good morning")     # Good morning, Ada!
greet_with("Ada", greeting="Hi")      # Hi, Ada! keyword argument

# Uncomment to see the SyntaxError from putting the default first.
# def broken(greeting="Hello", name):
# print(name)
