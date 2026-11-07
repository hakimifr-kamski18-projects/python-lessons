# Unit 11 — your first class
# Run this with the Run button in your editor.

# You have been calling methods since unit 02. upper() belongs to
# strings and append() belongs to lists. type() tells you the type of a
# value. Look at the word it uses in its answer.

print(type("hello"))     # <class 'str'>
print(type([1, 2]))      # <class 'list'>

print()

# ---------------------------------------------------------------
# A CLASS is a blueprint. Calling it with brackets makes an OBJECT.
# pass means "do nothing, on purpose", from unit 03.

class Dog:
    pass

rex = Dog()
fido = Dog()

print(type(rex))         # <class '__main__.Dog'>
print(rex)               # <__main__.Dog object at 0x...>
print(fido)              # a different number, because it is a different object

# The number after "at" changes every time you run the file.
# It is where the object lives in memory, and you never need it.

print()

# You can give an object an attribute from outside.
# Real code does not do this. It is here to show what __init__ fixes.
rex.name = "Rex"
fido.name = "Fido"
print(rex.name)          # Rex
print(fido.name)         # Fido

# Uncomment to see what happens when you forget to set one.
# spot = Dog()
# print(spot.name)       # AttributeError: 'Dog' object has no attribute 'name'

print()

# ---------------------------------------------------------------
# __init__ sets up a new object, and Python runs it by itself every
# time you create one. self is the new object. This Dog replaces the
# empty one above.

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

rex = Dog("Rex", 3)
fido = Dog("Fido", 7)

print(rex.name, rex.age)     # Rex 3
print(fido.name, fido.age)   # Fido 7

# Change an attribute of one object. The other one is untouched.
rex.age = 4
print(rex.age, fido.age)     # 4 7

print()

# ---------------------------------------------------------------
# Break it on purpose. Uncomment one line at a time and read the error.

# Dog("Rex")
#   TypeError: Dog.__init__() missing 1 required positional argument: 'age'

# Dog("Rex", 3, 4)
#   TypeError: Dog.__init__() takes 3 positional arguments but 4 were given
#   You gave 3 values. Python counts self as well, which makes 4.

# Misspell __init__ as _init_ (one underscore each side) in the class
# above, then run Dog("Rex", 3) again.
#   TypeError: Dog() takes no arguments
