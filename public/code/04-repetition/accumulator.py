# Unit 04 — the accumulator pattern
# Run this file with: python3 accumulator.py
#
# This is the most important idea in the unit, and one of the most
# important in the whole course.
#
# The shape:
# start with something
# change it a little on every pass
# look at it when you are done

# ---------------------------------------------------------------
# 1. ADDING UP

total = 0

for number in range(1, 6):
    total = total + number

print("Sum of 1 to 5:", total)     # 15

# TRACE IT ON PAPER before trusting it.
# total = 0
# pass 1: total = 0 + 1 = 1
# pass 2: total = 1 + 2 = 3
# pass 3: total = 3 + 3 = 6
# pass 4: total = 6 + 4 = 10
# pass 5: total = 10 + 5 = 15

print()

# The famous one.
total = 0
for number in range(1, 101):
    total += number
print("Sum of 1 to 100:", total)   # 5050

print()

# ---------------------------------------------------------------
# 2. COUNTING

count = 0

for number in range(1, 101):
    if number % 2 == 0:
        count += 1

print("Even numbers from 1 to 100:", count)   # 50

print()

# ---------------------------------------------------------------
# 3. BUILDING UP TEXT

result = ""

for word in "python is fun".split():
    result = result + word + " "

print(repr(result))     # 'python is fun '

# There is a trailing space on the end. That is normal, and it is
# usually cleaned up afterwards with .strip()

print(repr(result.strip()))

print()

# ---------------------------------------------------------------
# 4. TRACKING THE BIGGEST SO FAR

biggest = 0

# The square brackets here are a LIST, which is unit 05. You met one
# already in unit 03 with "answer in [\"yes\", \"y\"]". For now, just
# read it as "these four numbers".
for number in [3, 7, 2, 9, 4]:
    if number > biggest:
        biggest = number

print("Biggest:", biggest)     # 9

# Now here is the interesting question. What if every number is negative?
# Uncomment and run.

# biggest = 0
# for number in [-3, -7, -2]:
# if number > biggest:
# biggest = number
# print("Biggest:", biggest)

# It prints 0, which is wrong. The starting value has to be smaller than
# anything you might actually see, or the pattern breaks.

print()

# ---------------------------------------------------------------
# 5. COMBINING IT WITH input()
# This is the shape of most exercises in this unit.

how_many = int(input("How many numbers? "))
total = 0

for i in range(how_many):
    number = float(input(f"Number {i + 1}: "))
    total += number

if how_many > 0:
    print(f"Total: {total}")
    print(f"Average: {total / how_many:.2f}")

# Note i + 1 in the prompt. The loop variable counts from 0,
# but humans count from 1. That little adjustment shows up constantly.
