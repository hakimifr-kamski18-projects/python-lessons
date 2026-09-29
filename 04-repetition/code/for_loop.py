# Unit 04 — for loops and range
# Run this file with: python3 for_loop.py
# Predict each output before running.

for i in range(5):
    print(i)

# Prints 0 1 2 3 4.
# It starts at 0 and STOPS BEFORE the end. Same rule as string slicing.
# So range(5) gives five numbers, 0 to 4.

print()

# ---------------------------------------------------------------
# The same loop, written both ways. Compare them.

print("while version:")
count = 0
while count < 5:
    print(count)
    count += 1

print("for version:")
for i in range(5):
    print(i)

# The for version has no counter to set up and no counter to increment.
# That is what it is for.

print()

# ---------------------------------------------------------------
# range() in all its forms.

print(list(range(5)))           # [0, 1, 2, 3, 4]
print(list(range(1, 6)))        # [1, 2, 3, 4, 5]
print(list(range(2, 11, 2)))    # [2, 4, 6, 8, 10]
print(list(range(10, 0, -1)))   # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

# list() turns the range() into something you can actually look at.
# That is the trick for checking what a range() gives you.

# ---------------------------------------------------------------
# THE OFF-BY-ONE RULE. Say it out loud.
#
# To print 1 to 5, you write range(1, 6).
# The end number is one MORE than the last number you want.

print()
print("range(1, 5) gives:", list(range(1, 5)))
print("range(1, 6) gives:", list(range(1, 6)))

# range(1, 5) stops at 4. That is the mistake you will make for months.

print()

# ---------------------------------------------------------------
# Looping over text directly, no range needed.

for letter in "Python":
    print(letter)

print()

sentence = "the quick brown fox"

for word in sentence.split():
    print(word.upper())

print()

# ---------------------------------------------------------------
# A countdown, which is the classic first loop.
# The natural attempt range(10, 0) gives NOTHING. You need the -1 step.

print("range(10, 0) gives:", list(range(10, 0)))
print("range(10, 0, -1) gives:", list(range(10, 0, -1)))
