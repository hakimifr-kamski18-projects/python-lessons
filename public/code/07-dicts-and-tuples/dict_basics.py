# Unit 07 — dictionary basics
# Run this with the Run button in your editor.

student = {
    "name": "Ada",
    "age": 36,
    "subject": "maths",
}

print(student)

# Compare with the unit 05 way of storing the same thing:

names = ["Ada", "Grace"]
scores = [88, 95]

scores_dict = {"Ada": 88, "Grace": 95}
print(scores_dict)

# The dictionary cannot get out of sync with itself. The name and the
# score are ONE thing, not two things kept in step by hand.

print()

# ---------------------------------------------------------------
# Getting things out. The position is a KEY, not a number.

print(student["name"])       # Ada
print(student["age"])        # 36

# Uncomment to see the KeyError. Note that the message names the key,
# which is unusually helpful.
# print(student["colour"])
#
# Compare with a bad list index. IndexError tells you a NUMBER, which is
# rarely a typo. KeyError tells you the KEY, which usually is one.

print()

# ---------------------------------------------------------------
# .get(), for when you are not sure the key is there

print(student.get("name"))                  # Ada
print(student.get("colour"))                # None, no error
print(student.get("colour", "unknown"))     # unknown

# WHEN to use which:
# student["name"] the key must be there, and crashing is correct
# student.get("name") a missing key is a normal situation
#
# Do not use .get() everywhere. A key that should have been there but
# is not is a bug, and crashing is how you find out about it.

print()

# ---------------------------------------------------------------
# Checking whether a key is there.
# NOTE: "in" checks the KEYS, not the values.

print("name" in student)            # True
print("colour" in student)          # False
print("Ada" in student)             # False! "Ada" is a VALUE
print("Ada" in student.values())    # True

print()

# ---------------------------------------------------------------
# The three ways to loop over a dictionary

for key in student:
    print(key)

print()

for value in student.values():
    print(value)

print()

for key, value in student.items():
    print(f"{key}: {value}")

# items() gives back PAIRS, and "for key, value in" separates them.
# That is tuple unpacking, which is later in this unit.
