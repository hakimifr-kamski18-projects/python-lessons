# Unit 09 — using your own module
# Run this file with: python3 use_my_tools.py
#
# Watch what appears before your program even starts asking questions.
# That is my_tools.py running its own bottom section, because importing a module runs its top level code.

import my_tools

print()
print("Now the actual program starts")

name = my_tools.get_text("Your name: ")
how_many = my_tools.get_number("How many numbers? ")

numbers = []
for i in range(how_many):
    numbers.append(my_tools.get_number(f"Number {i + 1}: "))

print()
print(f"Hello {name.title()}")
print(f"Average: {my_tools.average(numbers):.2f}")
print(f"Biggest: {my_tools.biggest(numbers)}")

# Note the dot the whole way through: my_tools.get_text, not get_text.
# That is the same idea as random.randint(). The dot tells you where the
# name came from.

# ---------------------------------------------------------------
# Now open my_tools.py and move that bottom section inside a
# "if __name__ == '__main__':" block, as shown in main_guard.py.
# Then run this file again and see the difference.
