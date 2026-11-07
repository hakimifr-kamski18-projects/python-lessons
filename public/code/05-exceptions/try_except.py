# Unit 05 — try and except
# Run this with the Run button in your editor.
# Run it several times. Type a whole number one time, and something
# like abc or 0 another time, and compare what happens.

# ---------------------------------------------------------------
# 1. The shape.

text = input("Type a whole number: ")

try:
    number = int(text)
    print("The conversion worked.")
    print(f"Double that is {number * 2}")
except ValueError:
    print("That was not a whole number.")

print("The program carries on here either way.")
print()

# If int(text) fails, the two print lines inside try are skipped.
# Python jumps straight to except, then carries on after it.
# If int(text) works, the except block is skipped instead.

# ---------------------------------------------------------------
# 2. Two different errors, two different except blocks.

text = input("Share 100 sweets between how many people? ")

try:
    people = int(text)
    print(f"Each person gets {100 // people}")
except ValueError:
    print("That was not a whole number.")
except ZeroDivisionError:
    print("Nobody to share with.")

print()

# Python checks the except blocks in order and runs the first one
# whose error type matches. Only one of them runs.
#
# The same thing with one except block for both errors. The round
# brackets hold the error types, with a comma between them.
# Uncomment these five lines to try it.

# try:
#     people = int(text)
#     print(f"Each person gets {100 // people}")
# except (ValueError, ZeroDivisionError):
#     print("Please type a whole number bigger than 0.")

# ---------------------------------------------------------------
# 3. Looking at Python's own message, with "as".

text = input("Type a decimal number: ")

try:
    value = float(text)
    print(f"Half of that is {value / 2}")
except ValueError as error:
    print("Python says:", error)

print()

# "error" is a variable name you choose. After "as", it holds the
# error, and printing it shows the message from the last line of
# the traceback.

# ---------------------------------------------------------------
# 4. else and finally. You will not need them often.

text = input("One more whole number: ")

try:
    number = int(text)
except ValueError:
    print("Not a whole number.")
else:
    print(f"else runs only when there was no error. You typed {number}.")
finally:
    print("finally runs every time, error or not.")
