# Unit 05 — The validation loop
# Run this with the Run button in your editor.
# Type some bad answers on purpose (abc, 4.5, or just Enter) before
# you type a good one.

import random

# ---------------------------------------------------------------
# 1. Keep asking until the answer is a whole number.

while True:
    text = input("How old are you? ")
    try:
        age = int(text)
        break
    except ValueError:
        print("Please type a whole number, like 25.")

print(f"Next year you will be {age + 1}.")
print()

# The break is inside try, right after the line that can fail.
# It is only reached if int(text) worked. A bad answer jumps to
# except, prints the message, and the loop goes round again.
#
# The input() line must be INSIDE the loop. If it is above the loop,
# the same bad answer is checked again and again, forever.

# ---------------------------------------------------------------
# 2. The guessing game from exercise 4.13, without .isdigit().

secret = random.randint(1, 100)
attempts = 0

while True:
    text = input("Guess a number between 1 and 100: ")

    try:
        guess = int(text)
    except ValueError:
        print("That is not a whole number, try again.")
        continue

    attempts += 1

    if guess < secret:
        print("Too low")
    elif guess > secret:
        print("Too high")
    else:
        print(f"Correct! You took {attempts} attempts")
        break

# Here the try sits inside a bigger loop, so the shape is different.
# A bad answer uses continue to skip the rest of the pass, so it does
# not count as an attempt. A good answer carries on to the game, and
# only the right guess leaves the loop, with break.
