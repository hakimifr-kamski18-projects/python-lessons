# Unit 05 — list basics
# Run this with the Run button in your editor.
# Predict each line before running it.

numbers = [1, 2, 3, 4, 5]
names = ["Ada", "Grace", "Alan"]
mixed = [1, "two", 3.0, True]
empty = []

print(numbers)
print(names)
print(mixed)
print(empty)

print()

# You have met lists already without knowing it.
print("a,b,c".split())          # a list, from unit 02
print("yes" in ["yes", "y"])    # a list, the trick from unit 03

print()

# ---------------------------------------------------------------
# Getting things out. Exactly the same rules as strings.

print(names[0])      # Ada
print(names[2])      # Alan
print(names[-1])     # Alan, the last one
print(len(names))    # 3
print(names[0:2])    # ['Ada', 'Grace'] a slice of a list is a list

# Uncomment to see the IndexError. Positions start at ZERO.
# print(names[3])

print()

# ---------------------------------------------------------------
# THE BIG DIFFERENCE FROM STRINGS.
# Strings cannot be changed. Lists can.

word = "Ada"
# word[0] = "K" # TypeError, uncomment to see

names = ["Ada", "Grace", "Alan"]
names[0] = "Katherine"

print(names)     # ['Katherine', 'Grace', 'Alan']

# Strings are IMMUTABLE. They cannot be changed.
# Lists are MUTABLE. They can be changed in place.
#
# Use those two words out loud. They come up constantly.
