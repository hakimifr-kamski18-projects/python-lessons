# Unit 06 — functions broken on purpose
# Run this with the Run button in your editor.
#
# Each function below has a problem. Work through them one at a time.
# For each one:
# 1. call it. There are suggested calls at the bottom
# 2. read the error out loud, bottom up
# 3. predict the fix
# 4. fix it and run again

# ---------------------------------------------------------------
# 1. The missing return
# Call it in the shell: broken_one(5) + 1

def broken_one(number):
    result = number * 2


# ---------------------------------------------------------------
# 2. Printing instead of returning
# Call it: x = broken_two(5)
# print(x)
# It prints 10, and then x is None. Both of those facts matter.
# Make a version that returns instead, then compare.

def broken_two(number):
    print(number * 2)


# ---------------------------------------------------------------
# 3. Using a variable that only exists inside another function
# Calling broken_three(4) works. The error is on the line after.
# Fix it so that the answer is handed back instead of left behind.

def broken_three(number):
    answer = number ** 2
    print(answer)


# ---------------------------------------------------------------
# 4. Wrong number of arguments
# Call it: broken_four("Ada")

def broken_four(name, age):
    print(f"{name} is {age}")


# ---------------------------------------------------------------
# 5. The default parameter in the
# wrong place
# This is a SyntaxError, so the file will not run at all until you
# comment it out or fix it. Parameters (the name in the definition that
# receives the value) without defaults must come
# before parameters with defaults.

# def broken_five(greeting="Hello", name):
# print(f"{greeting}, {name}")


# ---------------------------------------------------------------
# 6. Forgetting the brackets when calling
# Uncomment the last two lines and run. Note that there is NO ERROR.
# That is what makes this one hard to spot.

def broken_six():
    print("Did I run?")

# This calls it:
# broken_six

# This does not call it, and does not complain:
# broken_six


print()
print("Uncomment the calls above and work through the problems one at a time.")
print("Start with problem 1, and read the error out loud before fixing it.")

# One thing to try at the end. Uncomment broken_five (problem 5) and run the
# file without fixing it. Notice that NONE of the output above appears,
# not even the prints at the bottom. A SyntaxError means Python refused to
# run any of this file at all. That is the same lesson as unit 00.
