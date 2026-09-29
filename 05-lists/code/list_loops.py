# Unit 05 — loops and lists together
# Run this file with: python3 list_loops.py

names = ["Ada", "Grace", "Alan"]

# No range(), no len(), no indices. The loop variable takes each ITEM in turn.

for name in names:
    print(f"Hello, {name}!")

print()

# Compare with the indexed version. This works, and it is more work.

for i in range(len(names)):
    print(f"{i}: {names[i]}")

# Reach for the first version by default. Use the second only when you
# really need the position for something.

print()

# ---------------------------------------------------------------
# BUILDING A LIST IN A LOOP
# The accumulator pattern, but with a list instead of a number.

squares = []

for number in range(1, 6):
    squares.append(number ** 2)

print(squares)      # [1, 4, 9, 16, 25]

print()

# ---------------------------------------------------------------
# FILTERING. Build a new list from an old one, keeping what passes a test.

numbers = [4, 7, 2, 9, 4, 1, 8]

evens = []
for number in numbers:
    if number % 2 == 0:
        evens.append(number)

print("Evens:", evens)      # [4, 2, 4, 8]

print()

# ---------------------------------------------------------------
# TRANSFORMING. Build a new list from an old one, changing each item.

names = ["ada", "grace", "alan"]

loud = []
for name in names:
    loud.append(name.upper())

print(loud)     # ['ADA', 'GRACE', 'ALAN']

print()

# There is a shorter way to write exactly this, called a list comprehension:
#
# loud = [name.upper() for name in names]
#
# It is everywhere in real Python code. Do NOT use it yet.
# Write the loop version. The comprehension is a unit ten thing, and it is
# much easier to learn once loops are automatic.

print()

# ---------------------------------------------------------------
# LISTS OF LISTS

grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

print(grid[0])        # [1, 2, 3]
print(grid[0][0])     # 1
print(grid[2][1])     # 8

# Read grid[2][1] inside out:
# take item 2 of the outer list -> [7, 8, 9]
# take item 1 of THAT -> 8
#
# Same idea as parts[0][0] from unit 02, one level up.

print()

for row in grid:
    for value in row:
        print(value, end=" ")
    print()
