# Unit 07 — changing a dictionary
# Run this file with: python3 dict_methods.py
# Print the dictionary after each step so you can watch it change.

student = {"name": "Ada"}

student["age"] = 36             # adding a new key
student["subject"] = "maths"    # adding another
print(student)

student["name"] = "Grace"       # changing an existing key
print(student)

# Adding and updating look identical. If the key is there it is replaced,
# if it is not it is created. That is convenient.

del student["age"]              # removing a key
print(student)

print()

# ---------------------------------------------------------------
# Size and the three views

student = {"name": "Ada", "age": 36}

print(len(student))         # 2, how many key-value pairs

print(student.keys())       # dict_keys(['name', 'age'])
print(student.values())     # dict_values(['Ada', 36])
print(student.items())      # dict_items([('name', 'Ada'), ('age', 36)])

# Those outputs look strange. dict_keys is not a list, though it works
# in a loop. If you want a real list, wrap it:

print(list(student.keys()))     # ['name', 'age']

print()

# ---------------------------------------------------------------
# pop() works on dictionaries too. It takes a KEY, not a position.

student = {"name": "Ada", "age": 36}
removed = student.pop("age")

print(f"Removed: {removed}")    # 36
print(student)                  # {'name': 'Ada'}

# ---------------------------------------------------------------
# Sorting. Dictionaries remember the order you added things in, but do
# not rely on that. Sort the keys if the order matters.

scores = {"Grace": 95, "Ada": 88, "Alan": 72}

for name in sorted(scores):
    print(f"{name} scored {scores[name]}")
