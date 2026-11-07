# Unit 08 — reading files
# Run this with the Run button in your editor.
#
# sample.txt sits in this same folder, next to this script. If your editor
# runs from a different folder, you get a FileNotFoundError instead, which is
# the most common problem with files and is never a code problem.

# ---------------------------------------------------------------
# THE FORM TO USE. The "with" block closes the file for you,
# even if something goes wrong partway through.

with open("sample.txt") as file:
    contents = file.read()

print(contents)

print("----")

# ---------------------------------------------------------------
# Reading it as a list of lines

with open("sample.txt") as file:
    lines = file.readlines()

print(lines)

print("----")

# ---------------------------------------------------------------
# THE ONE TO ACTUALLY USE. Line by line, in a loop.
# Notice the blank line between each line of output. Work out why
# before reading the fix below.

with open("sample.txt") as file:
    for line in file:
        print(line)

# Each line from a file INCLUDES the newline character at the end.
# So "line" holds "This is the first line...\n", and print() adds ANOTHER
# newline, which gives you the blank line.

print("----")

# Fix 1: strip it off
with open("sample.txt") as file:
    for line in file:
        print(line.strip())

print("----")

# Fix 2: stop print() adding its own newline
with open("sample.txt") as file:
    for line in file:
        print(line, end="")

print()
print("----")

# ---------------------------------------------------------------
# Reading a file into a dictionary.
# Note the int conversion. Everything from a file is TEXT, exactly
# like input(). This is the same problem as unit 02.

scores = {}

with open("scores.txt") as file:
    for line in file:
        line = line.strip()

        if not line:            # skip blank lines, common at the end of a file
            continue

        name, score = line.split(",")
        scores[name] = int(score)

print(scores)
print(type(scores["Ada"]))
