# Unit 01 — arithmetic
# Run this file with:  python3 arithmetic.py
# Before running each block, predict the answer.

print("Addition:        ", 10 + 3)
print("Subtraction:     ", 10 - 3)
print("Multiplication:  ", 10 * 3)
print("Power:           ", 10 ** 3)
print("Division:        ", 10 / 3)
print("Floor division:  ", 10 // 3)
print("Remainder:       ", 10 % 3)

print()

# Division ALWAYS gives a float, even when it divides evenly.
print(10 / 2)      # 5.0, not 5
print(type(10 / 2))

# Floor division gives a whole number, discarding the remainder.
print(10 // 2)     # 5
print(type(10 // 2))

print()

# ---------------------------------------------------------------
# Why // and % matter. A number is even when n % 2 is 0.

print("10 % 2 =", 10 % 2)    # 0, so 10 is even
print("11 % 2 =", 11 % 2)    # 1, so 11 is odd

print()

# Splitting a total into hours and minutes.

total_minutes = 137

hours = total_minutes // 60
minutes = total_minutes % 60

print(total_minutes, "minutes is", hours, "hours and", minutes, "minutes")

print()

# ---------------------------------------------------------------
# Order of operations. Multiplication before addition, like maths.
# Use brackets whenever there is any doubt at all.

print(2 + 3 * 4)         # 14, not 20
print((2 + 3) * 4)       # 20

print()

# ---------------------------------------------------------------
# Big numbers. Python handles them without complaint.

print(2 ** 100)

print()

# Decimals are not stored exactly. Do not be alarmed by this,
# and do not compare decimal numbers for exact equality.

print(0.1 + 0.2)
print(0.1 + 0.2 == 0.3)     # False. That is the same as in maths class, roughly.

print()

# ---------------------------------------------------------------
# Your turn. Work these out on paper first, then check by running.

# 1. 17 // 5
# 2. 17 % 5
# 3. 5000 seconds is how many hours, minutes and seconds?
#    Hint: start with seconds // 3600, then go from there.
