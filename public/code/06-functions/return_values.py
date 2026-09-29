# Unit 06 — returning values
# Run this file with: python3 return_values.py
#
# THIS IS THE MOST IMPORTANT FILE IN THE UNIT.
# print() shows a human. return gives a value to the program.

def double_print(number):
    print(number * 2)

def double_return(number):
    return number * 2

x = double_print(5)     # prints 10, and x is...
y = double_return(5)    # prints nothing, and y is...

print(f"x is {x}")
print(f"y is {y}")

# x is None! The print() version showed you the answer and threw it away.
# Only the return version actually handed the answer to the caller.

print()

# The practical difference.

print(f"double_return(5) + 1 = {double_return(5) + 1}")

# Uncomment to see the TypeError:
# print(double_print(5) + 1)

# TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'
#
# None + 1. That is what a missing return looks like from the outside.
# You will see this error a lot in your own code over the next few weeks.

print()

# ---------------------------------------------------------------
# No return means the function gives back None.

def add(a, b):
    total = a + b       # computed, then thrown away

print(f"add(2, 3) gives: {add(2, 3)}")

print()

# ---------------------------------------------------------------
# return also ENDS the function right there.

def check(number):
    if number < 0:
        return "negative"
    return "not negative"

print(check(-5))    # negative
print(check(5))     # not negative

# Handling the special cases first and returning early is a very
# common pattern, and it reads better than nesting in else branches.

def check_two(number):
    if number < 0:
        return "negative"
    if number == 0:
        return "zero"
    return "positive"

print(check_two(-5), check_two(0), check_two(5))

print()

# ---------------------------------------------------------------
# You can return more than one value. The comma makes a tuple, which is unit 07, so just note the shape for now.

def min_and_max(numbers):
    return min(numbers), max(numbers)

low, high = min_and_max([3, 1, 4, 1, 5])
print(f"low is {low}, high is {high}")
