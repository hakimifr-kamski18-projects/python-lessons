# Unit 09 — errors that come with files
# Run this with the Run button in your editor.

# ---------------------------------------------------------------
# A recap first. You learned try and except in unit 05.

text = input("Number (try typing hello): ")

try:
    number = int(text)
    print(f"Double: {number * 2}")
except ValueError:
    print("That was not a number")

print()

# ---------------------------------------------------------------
# FileNotFoundError, the error you will meet most with files.
# The message names the file exactly.

try:
    with open("missing.txt") as file:
        contents = file.read()
except FileNotFoundError:
    print("There is no file called missing.txt")

print()

# ---------------------------------------------------------------
# Checking first, or trying?
# In unit 05, checking first with isdigit() and trying with int()
# were both fine. With files, trying is the only sensible way.
# Nothing you know can look at a file name and say whether the file
# is there, so you try to open it and catch FileNotFoundError.

# ---------------------------------------------------------------
# Reading data can fail in two separate ways, so there are two
# except blocks. The file can be missing, or a line can be wrong.
# Try renaming scores.txt, or adding a line like  Ada,lots

total = 0
try:
    with open("scores.txt") as file:
        for line in file:
            name, score = line.strip().split(",")
            total += int(score)
except FileNotFoundError:
    print("There is no scores.txt next to this program")
except ValueError:
    print("A line in scores.txt is not in the form name,score")
else:
    print(f"Total: {total}")    # runs only if the reading worked

# One message for both? Use a tuple, as in unit 05:
#     except (FileNotFoundError, ValueError):

# ---------------------------------------------------------------
# finally is mostly for cleanup. The with statement already closes
# the file, so with files you will rarely need it.
