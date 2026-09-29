# Unit 03 — comparisons
# Run this file with:  python3 comparisons.py
# Predict each line before running it.

print("5 > 3  :", 5 > 3)      # True
print("5 < 3  :", 5 < 3)      # False
print("5 == 5 :", 5 == 5)     # True
print("5 != 3 :", 5 != 3)     # True
print("5 >= 5 :", 5 >= 5)     # True
print("5 <= 4 :", 5 <= 4)     # False

print()

# ---------------------------------------------------------------
# ONE equals sign means "put this value in that name".
# TWO equals signs mean "ask whether these are equal".
#
#   age = 25     "age gets twenty five"
#   age == 25    "is age equal to twenty five"
#
# Read both out loud. Do this every time you are unsure.

age = 25
print("age == 25 :", age == 25)     # True
print("age == 26 :", age == 26)     # False

print()

# ---------------------------------------------------------------
# Comparisons work on text too.

print("apple == apple :", "apple" == "apple")     # True
print("apple == Apple :", "apple" == "Apple")     # False, case matters
print("apple < banana :", "apple" < "banana")     # True, alphabetical
print("Zebra < apple  :", "Zebra" < "apple")      # True, capitals sort first

# That last one is not a bug. Capital letters have lower character codes
# than lowercase ones, which is why you almost always compare .lower() text.

print()

# The comparison you will actually write, done properly.
answer = input("Continue? (yes/no) ").strip().lower()
print("You said yes:", answer == "yes")

# Try it with "YES", "Yes", and " yes " and see that all of them work.
