# Unit 05 — What went wrong?
# Run this with the Run button in your editor.
# As it is, this file runs without any errors. Each section below has
# one line that is commented out. Uncomment ONE of those lines, run the
# file, and read the error from the bottom up. Then comment the line
# out again before you try the next one.

print("The file started running.")
print()

# ---------------------------------------------------------------
# ValueError: the right type of value, but the content is wrong.
# int() takes a string, but "abc" is not a number written as text.

print(int("42"))
# print(int("abc"))

# Pressing Enter without typing anything gives an empty string "",
# and int("") is a ValueError too.
# print(int(""))

# ---------------------------------------------------------------
# ZeroDivisionError: dividing by zero.

print(10 / 4)
# print(10 / 0)

# ---------------------------------------------------------------
# TypeError: the wrong type of value for this operation.
# You cannot glue a number onto text with +.

print("Score: " + str(10))
# print("Score: " + 10)

# ---------------------------------------------------------------
# NameError: a name Python does not know, usually a typo.

total = 5
print(total)
# print(totle)

# ---------------------------------------------------------------
# IndexError: a position the string does not have.
# "cat" has positions 0, 1 and 2, so 3 is one too far.

print("cat"[2])
# print("cat"[3])

print()
print("The file reached the end.")

# ---------------------------------------------------------------
# All of the errors above are exceptions. They happen while the
# program is running, so the lines BEFORE the error still run.
# Look for "The file started running." above each traceback.
#
# A SyntaxError is different. Uncomment the line below (it has no
# colon at the end) and run the file again.

# if 5 > 3

# This time even the first print does not appear. Python reads the
# whole file before it runs any of it, and a file that is not valid
# Python never starts. That is also why try and except cannot catch
# a SyntaxError. The try line would never run either.
