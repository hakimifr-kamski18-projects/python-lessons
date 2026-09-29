# Unit 01 — the basic types
# Run this with the Run button in your editor.

# Four kinds of value, for now.

whole_number = 25          # int
decimal_number = 1.75      # float
text = "Ada"               # str
truth_value = True         # bool

# type() tells you which kind something is.
# The output looks ugly but it is readable. <class 'int'> means int.

print(type(whole_number))
print(type(decimal_number))
print(type(text))
print(type(truth_value))

print()

# The important one. These three are different kinds of thing.

print(type(2))       # <class 'int'>
print(type(2.0))     # <class 'float'>
print(type("2"))     # <class 'str'>

print()

# int plus int gives int.
print(2 + 3)

# int plus float gives float. Python upgrades to the safer kind.
print(2 + 3.0)

# str plus str gives str. This GLUES the text together. It is not maths.
print("2" + "3")

# str plus int is an error. Uncomment the next line and run it to see.

# print("2" + 3)

# Read the error out loud, bottom up. It says something like:
# TypeError: can only concatenate str (not "int") to str
#
# Python cannot tell whether you meant 23 or 5, so it refuses to guess.

print()

# Booleans are capitalised. Lowercase true and false are NameErrors.
# Uncomment the next line to see.

# print(true)
