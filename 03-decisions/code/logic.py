# Unit 03 — combining conditions
# Run this file with:  python3 logic.py

# and : true when BOTH sides are true
# or  : true when AT LEAST ONE side is true
# not : flips it

print("True  and True  :", True and True)     # True
print("True  and False :", True and False)    # False
print("True  or  False :", True or False)     # True
print("False or  False :", False or False)    # False
print("not True        :", not True)          # False

print()

age = 20
has_ticket = True

if age >= 18 and has_ticket:
    print("You can enter")

print()

# ---------------------------------------------------------------
# THE TRAP. This looks right in English and is always true.

answer = "no"

if answer == "yes" or "y":
    print("Continuing (even though you said no!)")

# Why? Python reads that as:  (answer == "yes")  or  ("y")
# The second part is just the string "y". A non-empty string counts as
# true. So the whole condition is always true.
#
# Run it. It prints, and answer is "no". That is the whole lesson.

print()

# The fix. Repeat the comparison.

answer = "no"

if answer == "yes" or answer == "y":
    print("Continuing")
else:
    print("Stopping")

print()

# A cleaner fix, using in. A list is unit 05, but this one pattern is
# so handy that it is worth knowing now.
# Read it as "is the answer one of these things".

answer = "no"

if answer in ["yes", "y"]:
    print("Continuing")
else:
    print("Stopping")

print()

# ---------------------------------------------------------------
# Chained comparisons, which read very naturally

age = 25

if 18 <= age < 65:
    print("Working age")

# same as, but nicer to read than
if age >= 18 and age < 65:
    print("Working age")

print()

# ---------------------------------------------------------------
# in and not in

name = "Ada Lovelace"

if "Ada" in name:
    print("Found Ada")

if "xyz" not in name:
    print("xyz is not there")

print()

# ---------------------------------------------------------------
# Truthiness. Empty things and zero count as false.

if 0:
    print("this will not print")

if "":
    print("this will not print either")

if "hello":
    print("this DOES print, because non-empty text is true")

# Which produces a very common way of writing it:

name = input("Name: ").strip()

if name:
    print(f"Hello {name}")
else:
    print("You did not enter a name")

# Careful: the STRING "False" is non-empty, so it is true.
# Empty or zero means false. Everything else means true.
