# Unit 07 — tuples
# Run this with the Run button in your editor.

# A tuple.

point = (3, 4)

print(point[0])     # 3
print(point[1])     # 4
print(len(point))   # 2

# Uncomment to see the TypeError.
# point[0] = 5

# Round brackets instead of square brackets.
# Immutable, like strings. Unlike lists.

print()

# ---------------------------------------------------------------
# You have been using tuples since unit 01 without knowing it.

a, b = "first", "second"
a, b = b, a         # tuple unpacking, the swap trick
print(f"a is {a}, b is {b}")

def min_and_max(numbers):
    return min(numbers), max(numbers)       # return. The comma makes a tuple

low, high = min_and_max([3, 1, 4, 1, 5])
print(f"low {low}, high {high}")

# Unpacking:

point = (3, 4)
x, y = point

print(x, y)

# Which is the same as:
x = point[0]
y = point[1]

print()

# ---------------------------------------------------------------
# WHEN TO USE A TUPLE RATHER THAN A LIST
#
# Honest answer: use a list unless you have a reason not to.
#
# list an ordered collection you might add to or remove from
# tuple a fixed group of values that belong together
#
# If you find yourself wanting to append() to it, it should have been a list.
#
# The most common place you will actually create one is a function
# returning several values. So you are already using them.

print()

# ---------------------------------------------------------------
# A small trap

single = (5)
print(type(single))         # <class 'int'> NOT a tuple!
                            # the brackets are just grouping

actual_single = (5,)
print(type(actual_single))  # <class 'tuple'>

# The trailing comma is what makes a one-item tuple.
