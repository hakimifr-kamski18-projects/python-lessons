# Unit 02 — input() and the type problem
# Run this with the Run button in your editor.
# You will need to type answers when it asks.

# input() shows a prompt, waits for the user to type something and press Enter,
# and then hands back what they typed as a value.

name = input("What is your name? ")
print(f"Hello, {name}!")

print()

# ---------------------------------------------------------------
# This fails. Uncomment it and run it.

# age = input("How old are you? ")
# print(f"Next year you will be {age + 1}")

# The error is:
#   TypeError: can only concatenate str (not "int") to str
#
# Read that out loud. Then find out WHY, rather than being told.
# Uncomment these two lines and run them.

# age = input("How old are you? ")
# print(type(age))

# It prints <class 'str'>. Everything the user types comes back as TEXT.
# Even if they typed 25. The character "2" then the character "5".

print()

# ---------------------------------------------------------------
# The fix, and the safe pattern. Two lines instead of one,
# so you can inspect the text before converting it.

age_text = input("How old are you? ")
print(f"You typed: {repr(age_text)}")
print(f"Its type before converting: {type(age_text)}")

age = int(age_text)
print(f"Its type after converting:  {type(age)}")
print(f"Next year you will be {age + 1}")

print()

# ---------------------------------------------------------------
# The shorthand everyone writes eventually. Fine once you are
# comfortable, but harder to debug when it goes wrong.

# age = int(input("How old are you? "))

print()

# ---------------------------------------------------------------
# Conversions do not always go how you expect.

print(int("25"))       # 25
print(int(" 25 "))     # 25, Python forgives surrounding spaces
print(int("-25"))      # -25
print(float("25"))     # 25.0
print(float("1.75"))   # 1.75
print(str(25))         # "25"

# These all fail. Uncomment one at a time and read the error.

# print(int("hello"))    # ValueError
# print(int("1.75"))     # ValueError, int() will not silently drop the .75
# print(int(""))         # ValueError, empty text is not a number
# print(int("25abc"))    # ValueError
