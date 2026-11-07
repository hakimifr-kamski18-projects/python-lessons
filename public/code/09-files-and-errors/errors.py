# Unit 08 — handling errors
# Run this with the Run button in your editor.

# ---------------------------------------------------------------
# You have been READING errors for eight units.
# Now you learn to HANDLE them.

text = input("Number (try typing hello): ")

try:
    number = int(text)
    print(f"Double: {number * 2}")
except ValueError:
    print("That was not a number")

# Read it out loud:
#   "try to do this. If this particular kind of error happens,
#    do this instead."

# ---------------------------------------------------------------
# The except is SPECIFIC. It catches ValueError and nothing else.
# Uncomment this and enter 0. You will still get a ZeroDivisionError,
# because try/except does not hide errors you did not ask it to catch.

# text = input("Number (try typing 0): ")
# try:
#     number = int(text)
#     print(100 / number)
# except ValueError:
#     print("That was not a number")

print()

# ---------------------------------------------------------------
# Catching more than one thing

text = input("Number (try 0, then try hello): ")

try:
    number = int(text)
    result = 100 / number
    print(f"100 divided by {number} is {result}")
except ValueError:
    print("That was not a number")
except ZeroDivisionError:
    print("Cannot divide by zero")

print()

# ---------------------------------------------------------------
# BARE except IS A BAD HABIT.
#
#     except:
#
# with nothing after it catches EVERYTHING, including typos in your own
# code and errors you never intended to handle. It makes bugs invisible.
# Always name the error type.

# ---------------------------------------------------------------
# Checking first, versus asking for forgiveness.
# Both are legitimate. The first is clearer when the check is simple.

text = "42"

if text.isdigit():              # check first
    number = int(text)
    print(f"checked: {number}")

try:                            # or just try it
    number = int(text)
    print(f"tried:   {number}")
except ValueError:
    print("not a number")

# Use try/except when there is no simple check. Reading a file that
# may not exist, for example.

print()

# ---------------------------------------------------------------
# else and finally. Mentioned here so you recognise them.

text = "42"

try:
    number = int(text)
except ValueError:
    print("not a number")
else:
    print("that worked")        # runs only if there was no error
finally:
    print("this always runs")
