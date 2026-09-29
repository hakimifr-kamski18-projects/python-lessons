# Unit 05 — code broken on purpose
# Run this file with: python3 list_traps.py
#
# Each section below is broken ON PURPOSE. Uncomment one section at a time,
# run it, read the error out loud bottom up, predict the fix, then fix it.

print("Uncomment one section at a time, below this line.")
print()

# ===============================================================
# TRAP 1 — Changing a list while looping over it
#
# This is meant to remove all the even numbers. It does not work.

# numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# for n in numbers:
# if n % 2 == 0:
# numbers.remove(n)
# print(numbers)

# Some items get skipped, because changing the list shifts the positions
# that the loop is counting through underneath you.
#
# THE RULE: never change a list while looping over it.
# Either loop over a COPY (for n in numbers[:])
# or build a new list instead.

# numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# odds = []
# for n in numbers:
# if n % 2!= 0:
# odds.append(n)
# print(odds)

# ===============================================================
# TRAP 2 — Two names for one list
#
# PREDICT what this prints BEFORE you uncomment and run it. Most people
# get this wrong.

# a = [1, 2, 3]
# b = a
# b.append(4)
# print(a)

# It prints [1, 2, 3, 4]. Both names point at the SAME list.
# b = a does not copy the list, it gives the same list a second name.
#
# If you want a real copy:
# b = a[:] a slice of the whole thing
# b = list(a) or this

# ===============================================================
# TRAP 3 — Off by one at the end

# names = ["Ada", "Grace", "Alan"]
# print(names[len(names)])

# IndexError. The last valid position is len - 1, not len.
# The last item is names[len(names) - 1], or more simply names[-1].

# ===============================================================
# TRAP 4 — append() returns None

# names = ["Ada", "Grace"]
# names = names.append("Alan")
# print(names)
# print(len(names))

# The first print() gives None. The second gives a TypeError, because
# None has no length. append() does its work by changing the list,
# so it has nothing to give back.

# ===============================================================
# TRAP 5 — append() with a list instead of an item

# names = ["Ada", "Grace"]
# names.append(["Alan", "Katherine"])
# print(names)
# print(len(names))

# That adds ONE item, which happens to be a list. The length is 3, not 4.
# To add several items, use extend() or append() them one at a time.
