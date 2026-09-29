# Unit 04 — while loops
# Run this with the Run button in your editor.
# TRACE this on paper before running. Write down "count" at each step.

count = 1

while count <= 5:
    print(count)
    count = count + 1

print("Done")

# The three pieces of every while loop:
#   1. something set up BEFORE the loop      count = 1
#   2. a condition checked before EVERY pass count <= 5
#   3. something inside that eventually
#      makes the condition false             count = count + 1
#
# Piece 3 is the one beginners forget. If you forget it, the condition
# never becomes false and the loop runs forever.

print()

# ---------------------------------------------------------------
# An infinite loop, on purpose.
# Uncomment these three lines, run it, watch it scroll, then
# click the Stop button next to Run to stop it.

# count = 1
# while count <= 5:
#     print(count)

# Stopping a runaway program is normal. Everyone writes infinite
# loops, all the time, forever. It is a normal thing, not a failure.

print()

# ---------------------------------------------------------------
# A while loop does not need a counter. It can run until something
# in the data says stop.

total = 0
number = int(input("Number to add (0 to finish): "))

while number != 0:
    total = total + number
    number = int(input("Number to add (0 to finish): "))

print(f"Total: {total}")

# Notice the input line had to be written TWICE. That is awkward.
# Later in this unit you will meet a neater way (while True with break).
