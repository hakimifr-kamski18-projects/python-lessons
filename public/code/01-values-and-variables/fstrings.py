# Unit 01 — f-strings
# Run this file with:  python3 fstrings.py

name = "Ada"
age = 36

# The painful way. Gluing text and values with +.
# This works and it is horrible to write. Note the str(), which is needed
# because you cannot glue a number onto text.

print("My name is " + name + " and I am " + str(age) + " years old")

# The good way. One f before the opening quote, braces around the values.

print(f"My name is {name} and I am {age} years old")

print()

# ---------------------------------------------------------------
# The braces can hold a calculation, not just a name.

price = 20
quantity = 3

print(f"{quantity} items at {price} dollars each is {price * quantity} dollars")

print(f"Half of 100 is {100 / 2}")

print()

# ---------------------------------------------------------------
# Formatting decimals, which is what you want for money.

cost = 19.9876
print(f"full precision:  {cost}")
print(f"two decimals:    {cost:.2f}")
print(f"no decimals:     {cost:.0f}")

# .2f means "fixed point, two digits after the point", and it rounds.

print()

# ---------------------------------------------------------------
# A small receipt, built from variables.

item = "coffee"
unit_price = 4.5
count = 3
total = unit_price * count
tax = total * 0.15

print(f"{count} x {item} at {unit_price:.2f} each")
print(f"Subtotal: {total:.2f}")
print(f"Tax:      {tax:.2f}")
print(f"Total:    {total + tax:.2f}")

print()

# ---------------------------------------------------------------
# Things that go wrong.

# 1. The f must touch the quote. Uncomment to see the error.
# print(f "hello {name}")

# 2. Without the f it is just text, and the braces print literally.
print("Without the f: {name}")

# 3. Forgetting the braces is SILENT. No error, just the wrong output.
print(f"Forgot the braces: name is name")

# That last one is the dangerous kind of bug. It runs, and it is wrong.
