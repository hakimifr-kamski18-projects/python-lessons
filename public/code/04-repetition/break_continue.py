# Unit 04 — break and continue
# Run this with the Run button in your editor.
# Predict both loops before running.

print("break when number is 5:")

for number in range(1, 11):
    if number == 5:
        break
    print(number)

# prints 1 2 3 4, then stops entirely

print()

print("continue when number is 5:")

for number in range(1, 11):
    if number == 5:
        continue
    print(number)

# prints 1 2 3 4 6 7 8 9 10, skipping only 5

print()

# break -> leave the loop immediately
# continue -> skip the rest of THIS pass, go to the next one
#
# Say both out loud. They are easy to mix up under pressure.

print()

# ---------------------------------------------------------------
# while True with break.
# This is the common way to write "keep going until something happens".

total = 0

while True:
    text = input("Number to add, or q to finish: ").strip()

    if text.lower() == "q":
        break

    total += int(text)

print(f"Total: {total}")

# Why this is nicer than the version in while_loop.py:
# - the input line is written once, not twice
# - the exit condition is right there in the middle,
# where the reader will actually see it
#
# "while True" is always true, so the only way out is the break.
# That is honest about how the loop really works.

print()

# ---------------------------------------------------------------
# A nested loop, for the multiplication table you are about to write.

for row in range(1, 6):
    for star in range(row):
        print("*", end="")
    print()

# end="" stops print() from adding a newline, so the stars stay on one line.
# The bare print() at the end moves to the next line.
#
# Trace the outer loop by hand:
# row 1: star 0 -> *
# row 2: star 0, star 1 -> **
# row 3: 0, 1, 2 -> ***
