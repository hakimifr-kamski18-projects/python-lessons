# Unit 05 — list methods
# Run this with the Run button in your editor.

# ---------------------------------------------------------------
# ADDING

names = ["Ada", "Grace"]

names.append("Alan")            # add to the end
print(names)                    # ['Ada', 'Grace', 'Alan']

names.insert(0, "Katherine")    # insert at a position
print(names)                    # ['Katherine', 'Ada', 'Grace', 'Alan']

# append() takes the ITEM, not a list.
extra = ["Ada", "Grace"]
extra.append(["Alan"])          # this adds a list INSIDE the list
print(extra)                    # ['Ada', 'Grace', ['Alan']]

print()

# ---------------------------------------------------------------
# REMOVING

names = ["Ada", "Grace", "Alan"]

names.remove("Grace")           # remove by VALUE
print(names)                    # ['Ada', 'Alan']

last = names.pop()              # remove and give back the LAST item
print(last)                     # 'Alan'
print(names)                    # ['Ada']

names = ["Ada", "Grace", "Alan"]
names.pop(0)                    # remove and give back the item at POSITION 0
print(names)                    # ['Grace', 'Alan']

# remove() takes a value. pop() takes a position.

print()

# ---------------------------------------------------------------
# THE IMPORTANT DISCOVERY.
#
# In unit 02, name.upper() changed nothing. String methods give you
# back a NEW string.
#
# List methods are different. They change the list IN PLACE.

names = ["Ada", "Grace"]
names.append("Alan")
print(names)                    # ['Ada', 'Grace', 'Alan'] <- it changed!

# Which produces this classic bug. Uncomment and run.

# names = ["Ada", "Grace"]
# names = names.append("Alan")
# print(names) # None
# print(len(names)) # TypeError

# append() gives back None, because it does the work by changing the list
# rather than by returning a new one.

print()

# RULE OF THUMB
# command-sounding names change the thing   append(), sort(), reverse(), remove()
# description-sounding names return new     upper(), split(), sorted(), strip()

print()

# ---------------------------------------------------------------
# SORTING AND REVERSING

numbers = [3, 1, 4, 1, 5, 9, 2, 6]

numbers.sort()
print(numbers)                  # [1, 1, 2, 3, 4, 5, 6, 9]

numbers.sort(reverse=True)
print(numbers)                  # [9, 6, 5, 4, 3, 2, 1, 1]

numbers = [3, 1, 4, 1, 5]
numbers.reverse()
print(numbers)                  # [5, 1, 4, 1, 3] reverse is NOT sorting

# sorted() gives a new list and leaves the original alone.

numbers = [3, 1, 4]
print(sorted(numbers))          # [1, 3, 4]
print(numbers)                  # [3, 1, 4] untouched

print()

# ---------------------------------------------------------------
# ASKING QUESTIONS

numbers = [3, 1, 4, 1, 5]

print(len(numbers))         # 5
print(3 in numbers)         # True
print(10 in numbers)        # False
print(numbers.count(1))     # 2
print(numbers.index(4))     # 2, position of the first 4
print(sum(numbers))         # 14
print(min(numbers))         # 1
print(max(numbers))         # 5

# index() raises a ValueError if the item is not there.
# a bad position raises an IndexError instead. Similar names, different things.
# Uncomment to see the ValueError.
# print(numbers.index(99))
