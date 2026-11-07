# Unit 12 — a parent class and its children
# Run this with the Run button in your editor.

# The PARENT class. Everything that all animals share goes here.

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        return "..."

    def describe(self):
        return f"{self.name} is {self.age} and says {self.speak()}"

    def have_birthday(self):
        self.age += 1


# ---------------------------------------------------------------
# A CHILD class. The name of the parent goes in the brackets.
# With only pass in the body, it gets everything the parent has.

class Hamster(Animal):
    pass

nibbles = Hamster("Nibbles", 1)
nibbles.have_birthday()
print(nibbles.describe())      # Nibbles is 2 and says ...

print()

# ---------------------------------------------------------------
# OVERRIDING. A child can replace one method and keep the rest.
# describe() is not written again, but it calls self.speak(),
# and self is a Dog or a Cat, so the child's speak() runs.

class Dog(Animal):
    def speak(self):
        return "Woof"

class Cat(Animal):
    def speak(self):
        return "Meow"

rex = Dog("Rex", 3)
tom = Cat("Tom", 5)
print(rex.describe())          # Rex is 3 and says Woof
print(tom.describe())          # Tom is 5 and says Meow

print()

# ---------------------------------------------------------------
# super().__init__(...) runs the parent's __init__ first,
# then the child adds what is new.

class GuideDog(Dog):
    def __init__(self, name, age, owner):
        super().__init__(name, age)
        self.owner = owner

    def describe(self):
        # super() works for any method, not only __init__
        return super().describe() + f", and guides {self.owner}"

buddy = GuideDog("Buddy", 4, "Sam")
print(buddy.name, buddy.owner)  # Buddy Sam
print(buddy.speak())            # Woof, from Dog
print(buddy.describe())         # Buddy is 4 and says Woof, and guides Sam

print()

# ---------------------------------------------------------------
# Break it on purpose. Uncomment one block at a time.

# 1. Forgetting super().__init__
# class Puppy(Dog):
#     def __init__(self, name, age, toy):
#         self.toy = toy
# print(Puppy("Bit", 0, "ball").describe())
#   AttributeError: 'Puppy' object has no attribute 'name'
#   The parent's __init__ never ran, so name and age were never set.

# 2. Passing self to super().__init__
# class Puppy(Dog):
#     def __init__(self, name, age, toy):
#         super().__init__(self, name, age)
#         self.toy = toy
# Puppy("Bit", 0, "ball")
#   TypeError: Animal.__init__() takes 3 positional arguments but 4 were given
#   super() already passes self. Do not pass it again.

# 3. Forgetting the brackets after super
# class Puppy(Dog):
#     def __init__(self, name, age, toy):
#         super.__init__(name, age)
#         self.toy = toy
# Puppy("Bit", 0, "ball")
#   TypeError: descriptor '__init__' requires a 'super' object but received a 'str'

# 4. A spelling mistake in the method you meant to override.
#    There is NO error. The parent's version runs, and you get "...".
# class Cow(Animal):
#     def speek(self):
#         return "Moo"
# print(Cow("Daisy", 6).describe())
