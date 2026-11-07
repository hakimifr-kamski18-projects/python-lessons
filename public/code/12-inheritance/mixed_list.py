# Unit 12 — isinstance and a list of mixed objects
# Run this with the Run button in your editor.

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "..."


class Dog(Animal):
    def speak(self):
        return "Woof"


class Cat(Animal):
    def speak(self):
        return "Meow"


class Bird(Animal):
    def speak(self):
        return "Tweet"


rex = Dog("Rex")

# ---------------------------------------------------------------
# isinstance(object, class) answers True or False.
# A Dog is also an Animal, because Dog was made from Animal.

print(isinstance(rex, Dog))        # True
print(isinstance(rex, Animal))     # True
print(isinstance(rex, Cat))        # False
print(isinstance("hello", str))    # True, it works for every type
print(isinstance(42, str))         # False

print()

# type() only gives the exact class, so it does not see the parent.
print(type(rex) == Dog)            # True
print(type(rex) == Animal)         # False

print()

# ---------------------------------------------------------------
# The loop makes the same method call on every object, and each
# object answers in its own way.

animals = [Dog("Rex"), Cat("Tom"), Bird("Tweety"), Dog("Fido"), Animal("Mystery")]

for animal in animals:
    print(f"{animal.name}: {animal.speak()}")

print()

# The loop does not check what kind of animal it has.
# Adding a new kind of animal does not change the loop at all.

# ---------------------------------------------------------------
# isinstance is useful when you need only one kind out of the list.

dogs = 0
for animal in animals:
    if isinstance(animal, Dog):
        dogs += 1
print(f"Dogs: {dogs}")             # Dogs: 2

# Every one of them is an Animal, including the plain one.
count = 0
for animal in animals:
    if isinstance(animal, Animal):
        count += 1
print(f"Animals: {count}")         # Animals: 5
