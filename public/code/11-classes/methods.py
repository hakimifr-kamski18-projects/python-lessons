# Unit 11 — methods and __str__
# Run this with the Run button in your editor.

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.tricks = []

    # A method that GIVES BACK a value, like name.upper()
    def describe(self):
        return f"{self.name} is {self.age} years old"

    # A method that CHANGES the object, like items.append()
    def have_birthday(self):
        self.age += 1

    # A method with a parameter of its own, after self
    def add_trick(self, trick):
        self.tricks.append(trick)

    # __str__ gives the text that print() shows for the object
    def __str__(self):
        return f"{self.name} ({self.age})"


rex = Dog("Rex", 3)

print(rex.describe())        # Rex is 3 years old
rex.have_birthday()
print(rex.describe())        # Rex is 4 years old

rex.add_trick("sit")
rex.add_trick("roll over")
print(rex.tricks)            # ['sit', 'roll over']

print()

# A method that changes something gives back None, the same as append().
result = rex.have_birthday()
print(result)                # None
print(rex.age)               # 5

print()

# ---------------------------------------------------------------
# Where self comes from. These two lines do exactly the same thing.
print(rex.describe())
print(Dog.describe(rex))

# And the same is true for the string methods you already know.
print("ada".upper())
print(str.upper("ada"))

print()

# ---------------------------------------------------------------
# __str__ in action. print(), str() and f-strings all use it.
print(rex)                   # Rex (5)
print(f"My dog is {rex}")    # My dog is Rex (5)

print()

# ---------------------------------------------------------------
# Break it on purpose. Each of these is a small class of its own,
# so you can uncomment one block at a time.

# 1. Forgetting self in the def
# class Cat:
#     def speak():
#         return "Meow"
# print(Cat().speak())
#   TypeError: Cat.speak() takes 0 positional arguments but 1 was given

# 2. Forgetting self. before an attribute
# class Cat:
#     def __init__(self, name):
#         self.name = name
#     def shout(self):
#         return name.upper()
# print(Cat("Tom").shout())
#   NameError: name 'name' is not defined. Did you mean: 'self.name'?

# 3. Forgetting the brackets when calling a method
# print(rex.describe)
#   <bound method Dog.describe of <__main__.Dog object at 0x...>>
#   No error. You get the method itself, not its answer.

# 4. __str__ that prints instead of returning
# class Cat:
#     def __str__(self):
#         print("a cat")
# print(Cat())
#   It shows "a cat" first, because the print inside __str__ runs.
#   Then: TypeError: __str__ returned non-string (type NoneType)
