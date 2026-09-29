# Unit 03 — the if statement
# Run this with the Run button in your editor.

age = 20

if age >= 18:
    print("You can vote")

# Three things about that shape:
# 1. the condition ends with a colon
# 2. the body is indented (four spaces)
# 3. the body runs only when the condition is True
#
# Now break it, one at a time, and read the error.
# a) remove the colon
# b) put the print() back at the left margin
# c) change 20 to 15 and run it again

print()

# ---------------------------------------------------------------
# else

age = 15

if age >= 18:
    print("You can vote")
else:
    print("Too young to vote")

# Exactly one of the two branches runs. Never both, never neither.

print()

# ---------------------------------------------------------------
# elif, for more than two options

score = 75

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("Needs work")

# Only the FIRST matching branch runs. Python stops there,
# even if a later condition would also have been true.

print()

# ---------------------------------------------------------------
# Which is why the order matters. This version is broken.

score = 95

if score >= 70:
    print("C or better")
elif score >= 90:
    print("A")

# It prints "C or better" for a score of 95, and never reaches the A branch.
# Fix it by putting the strictest condition first.

print()

# ---------------------------------------------------------------
# if with nothing to do yet

x = 10

if x > 5:
    pass        # "do nothing, on purpose"
