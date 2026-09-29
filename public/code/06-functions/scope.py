# Unit 06 — scope
# Run this with the Run button in your editor.

def double(number):
    result = number * 2
    return result

print(double(5))

# Uncomment this. It is a NameError, and the reason is the lesson.
# print(result)

# "result" only exists INSIDE the function. When the function finishes,
# it is gone. A function is its own little world.

print()

# ---------------------------------------------------------------
# A function CAN read a global variable.

message = "hello"

def show():
    print(message)

show()          # hello

print()

# ---------------------------------------------------------------
# But assigning to a name inside a function makes a NEW local one.

message = "hello"

def change():
    message = "goodbye"     # this creates a LOCAL message
    print(f"inside the function: {message}")

change()
print(f"outside the function: {message}")

# inside the function: goodbye
# outside the function: hello <- unchanged!
#
# The assignment inside created a new local variable that shadows the
# global one. The global is untouched.

print()

# ---------------------------------------------------------------
# THE RULE
#
# Functions should take what they need as PARAMETERS and hand back what they produce with RETURN. Do not have functions that quietly change things outside themselves.
#
# Good:

def add_tax(price, rate):
    return price * (1 + rate)

price = 20
price_with_tax = add_tax(price, 0.15)
print(price_with_tax)

# "price" outside is untouched, and it is clear what the function did.

print()

# ---------------------------------------------------------------
# Functions calling functions

def area_of_rectangle(width, height):
    return width * height

def cost_of_floor(width, height, price_per_square_metre):
    return area_of_rectangle(width, height) * price_per_square_metre

print(cost_of_floor(3, 4, 25))

# cost_of_floor uses area_of_rectangle without knowing or caring how it
# works inside. That is the point of functions, arriving in full.
