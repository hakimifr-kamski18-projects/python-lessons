# This file contains a mistake on purpose. Run it and read the error.
#
# Notice something important as you do: "Line one" never gets printed.
# That is because a SyntaxError happens before the program starts running at all.
# Python reads the whole file first, and if it cannot understand it, it refuses
# to run any of it. So a syntax error means nothing in the file ran, even the
# lines above the mistake.

print("Line one")
print("Line two)
print("Line three")
