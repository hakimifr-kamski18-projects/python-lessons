# Unit 09 — your own module
# This file is a module. It just happens to be one you wrote.
#
# Note the print() and the test call at the BOTTOM of this file. They are the
# problem that main_guard.py solves. Leave them there for now.

def get_number(prompt):
    while True:
        text = input(prompt).strip()
        try:
            return int(text)
        except ValueError:
            print("That is not a whole number, try again")


def get_text(prompt):
    while True:
        text = input(prompt).strip()
        if text:
            return text
        print("You have to type something")


def average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)


def biggest(numbers):
    if not numbers:
        return None
    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
    return largest


# ---------------------------------------------------------------
# This runs whenever the file runs. It ALSO runs when another file
# imports this one, which is usually not what you want.

print("Setting up my_tools...")

scores = [88, 95, 72]
print(f"Average of the test scores: {average(scores):.1f}")
