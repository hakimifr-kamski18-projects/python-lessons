---
title: Python basics, one page
---
A reference sheet. Keep it open while you work, and try to need it less each week.

---

## Values and types

```python
25            # int      whole number
1.75          # float    has a decimal point
"hello"       # str      text, in quotes
True          # bool     True or False, capitalised
None          # NoneType nothing

type(25)      # tells you which one
```

`"25"` is text, not a number. That distinction causes most beginner bugs.

---

## Variables

```python
age = 25          # age GETS 25. Not "age equals 25"
age = age + 1     # works out the right side first, then stores it
age += 1          # the same thing, shorter
```

Names. Letters, digits and underscores, cannot start with a digit, case sensitive.
Use lowercase with underscores, and be descriptive.

---

## Arithmetic

```python
10 + 3      # 13
10 - 3      # 7
10 * 3      # 30
10 / 3      # 3.333...   division ALWAYS gives a float
10 // 3     # 3          how many whole times it fits
10 % 3      # 1          what is left over
10 ** 3     # 1000       to the power of

(2 + 3) * 4    # 20. Use brackets whenever there is any doubt
```

`%` is how you test even and odd (`n % 2 == 0`), and how you split things into hours
and minutes.

---

## Text

```python
name = "Ada"
f"Hello {name}"          # puts values into text. The f is required
f"{price:.2f}"           # two decimal places
f"{value:10}"            # pad to width 10

len(name)                # 4
name[0]                  # "A"     first. Positions start at ZERO
name[-1]                 # "a"     last
name[0:2]                # "Ad"    start included, end excluded

name.upper()             # "ADA"   gives a NEW string
name.lower()
name.strip()             # removes spaces from both ends
name.title()
name.replace("A", "B")
name.split()             # gives a list of pieces
" ".join(words)          # puts a list back together
"x" in name              # True
```

String methods give you back a new string. They do not change the original. If
"nothing happened", you forgot to assign the result back.

---

## Input

```python
name = input("Name? ")           # always gives back TEXT
age = int(input("Age? "))        # convert it yourself
price = float(input("Price? "))  # int() refuses decimals
```

`"5" + 5` is a TypeError. `input()` always gives a string, no matter what was typed.

Add `.strip()` to input to remove stray spaces, and `.lower()` to ignore case.

---

## Comparisons and logic

```python
=       put this value in that name
==      ask whether these are equal

5 > 3      5 < 3      5 >= 5      5 <= 4      5 != 3

and     both sides must be true
or      at least one side must be true
not     flips it

0 <= x <= 10            # a range, reads naturally
"a" in "cat"            # True
```

Watch out for `if answer == "yes" or "y"`, which is always true. Use
`if answer in ["yes", "y"]` instead.

---

## Decisions

```python
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
else:
    print("C")
```

The colon is required. The indentation is required, and it is how Python knows what
is inside what. Four spaces, never tabs.

Only the first matching branch runs, so put the strictest condition first.

---

## Loops

```python
for i in range(5):          # 0 1 2 3 4.  Stops BEFORE the end
    print(i)

for i in range(1, 6):       # 1 2 3 4 5
for i in range(0, 10, 2):   # 0 2 4 6 8
for i in range(5, 0, -1):   # 5 4 3 2 1

for item in my_list:        # the natural way to walk a list
    print(item)

while count < 10:           # when you do not know how many times
    count += 1

while True:                 # keep going until something happens
    text = input("...")
    if text == "q":
        break

break        # leave the loop
continue     # skip the rest of this pass
```

The accumulator pattern, which is everywhere.

```python
total = 0
for number in numbers:
    total += number
```

---

## Lists

```python
items = [1, 2, 3]
items[0]              # first. Positions start at ZERO
items[-1]             # last
len(items)
sum(items)            # also min() and max()

items.append(4)       # add to the end
items.insert(0, 9)    # add at a position
items.remove(3)       # remove by value
items.pop()           # remove and give back the last
items.sort()          # sorts IN PLACE
sorted(items)         # gives a NEW sorted list

3 in items
items.count(3)
items.index(3)        # the position
```

List methods change the list. String methods do not. `items = items.append(4)` is a
bug, because `append` gives back `None`.

`b = a` does not copy a list, it gives it a second name. Use `b = a[:]` for a copy.

---

## Dictionaries

```python
scores = {"Ada": 88, "Grace": 95}

scores["Ada"]              # 88.  KeyError if it is not there
scores.get("Bob")          # None instead of an error
scores.get("Bob", 0)       # a default instead

scores["Alan"] = 72        # adds a new key
del scores["Alan"]         # removes it
"Ada" in scores            # checks the KEYS

for key in scores: ...
for value in scores.values(): ...
for key, value in scores.items(): ...      # the one you want most

len(scores)
```

`"Ada" in scores` is False. `in` checks keys, and `"Ada"` is a value.

The counting pattern.

```python
counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1
```

---

## Tuples

```python
point = (3, 4)          # like a list, but cannot be changed
x, y = point            # unpacking
a, b = b, a             # the swap trick
```

A function returning several values makes one.

---

## Functions

```python
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

result = greet("Ada")
```

`print` shows a human. `return` hands a value back to the program. If you forget the
`return`, the function gives back `None`, and you will see errors about `None` later.

Everything inside a function is local. It does not exist outside.

A function name should say what it does, and `is_even` should return `True` or
`False`, not print.

---

## Files

```python
with open("data.txt") as file:
    for line in file:
        print(line.strip())

with open("out.txt", "w") as file:      # "w" WIPES the file
    file.write("hello\n")               # write does not add a newline

with open("log.txt", "a") as file:      # "a" adds to the end
    file.write("another line\n")
```

Each line read from a file includes its newline character, which is why you get blank
lines unless you `.strip()`.

Everything from a file is text, just like `input()`. Convert it yourself.

---

## Handling errors

```python
try:
    number = int(input("Number? "))
except ValueError:
    print("That was not a number")
```

Catch specific error types. Never use a bare `except:`.

The validation loop, for getting a usable value out of a user.

```python
def get_number(prompt):
    while True:
        text = input(prompt).strip()
        try:
            return int(text)
        except ValueError:
            print("Not a number, try again")
```

---

## Modules

```python
import random
random.randint(1, 6)

from math import sqrt      # imports just that name
import random as rnd       # a nickname

import json
json.dump(data, file)      # save a structure
data = json.load(file)     # load it back
```

Useful ones. `random`, `math`, `datetime`, `statistics`, `string`, `time`.

Never use `from module import *`.

---

## The errors you will actually meet

```
SyntaxError        the file is not valid Python, so NOTHING ran
IndentationError   the spacing at the start of a line is wrong
NameError          a name that does not exist, usually a typo or a capital
TypeError          wrong kind of value, like "5" + 5
ValueError         right kind, bad content, like int("hello")
KeyError           a dictionary key that is not there
IndexError         a position the list does not have
AttributeError     asking a value to do something it cannot
FileNotFoundError  the file is not where the program is looking
ZeroDivisionError  divided by zero
```

---

## The five habits

1. Read the error from the BOTTOM UP, out loud.
2. Print things to find out what is in them. `print(repr(x))` shows hidden spaces.
3. Run your code often, in small pieces.
4. When something is confusing, check the TYPE. `print(type(x))`.
5. Name things well. `total_price`, not `tp`.
