# Unit 08 — the validation loop
# Run this with the Run button in your editor.
#
# This is THE pattern for getting a usable value out of a user,
# and you will use it constantly from now on.

def get_number(prompt):
    while True:
        text = input(prompt).strip()

        try:
            return int(text)        # if this works, the function is DONE
        except ValueError:
            print("That is not a whole number, try again")

# Trace the two cases.
#
# valid input: int(text) succeeds, return runs, the
# function ends, and the loop ends with it
#
# bad input: ValueError happens, the message prints, the loop goes
# round again and asks once more
#
# The neat part is that the return is inside the try. If the conversion
# works, the function is finished.

age = get_number("Your age: ")
print(f"Next year you will be {age + 1}")

print()

# Reuse it for anything.

how_many = get_number("How many numbers? ")

total = 0
for i in range(how_many):
    total += get_number(f"Number {i + 1}: ")

if how_many > 0:
    print(f"Average: {total / how_many:.2f}")

print()

# ---------------------------------------------------------------
# A version that also accepts decimals, and refuses nonsense

def get_float(prompt):
    while True:
        text = input(prompt).strip()
        try:
            return float(text)
        except ValueError:
            print("That is not a number, try again")

# ---------------------------------------------------------------
# A version for non-empty text

def get_text(prompt):
    while True:
        text = input(prompt).strip()
        if text:
            return text
        print("You have to type something")
