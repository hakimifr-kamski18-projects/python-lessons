# Unit 01 — variables
# Run this file with:  python3 variables.py

# A variable is a name for a value.
# The "=" means "put the value on the right into the name on the left".
# Read it as "age gets 25", NOT "age equals 25".

age = 25
name = "Ada"
height = 1.75
is_student = True

print(age)
print(name)
print(height)
print(is_student)

print()  # print() with nothing in it just prints a blank line

# ---------------------------------------------------------------
# Assignment is a moment in time, and it replaces what was there.

score = 10
print("score starts at", score)

score = 20
print("after score = 20, score is", score)

# This looks like maths and is not. Work out the right side first,
# then store the answer back in the same name.
score = score + 5
print("after score = score + 5, score is", score)

# The shortcut for the same thing.
score += 5
print("after score += 5, score is", score)

# ---------------------------------------------------------------
# Names are case sensitive and cannot start with a digit.

value = 1
Value = 2
VALUE = 3

print(value, Value, VALUE)   # three different variables

# ---------------------------------------------------------------
# Print several things at once by separating them with commas.
# Python puts a space between them automatically.

first_name = "Grace"
last_name = "Hopper"
print(first_name, last_name)

# But that space is not always what you want.
print("Hopper", "1959")
