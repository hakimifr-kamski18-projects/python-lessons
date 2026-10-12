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

print(type(25))     # shows which one: <class 'int'>
str(25)             # "25"   turns a number into text
```

`"25"` is text, not a number. That distinction causes most beginner bugs.

Some values count as False inside an `if`. These are `0`, `""` (empty text), `[]`
(an empty list) and `None`. Almost everything else counts as True. Programmers call
these values falsy and truthy.

---

## Variables

```python
age = 25          # age GETS 25. Not "age equals 25"
age = age + 1     # works out the right side first, then stores it
age += 1          # the same thing, shorter
age -= 1          # also *=  and  //=  and  /=
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
9 ** 0.5    # 3.0        a square root

(2 + 3) * 4    # 20. Use brackets whenever there is any doubt
2 + 3 * 4      # 14. ** first, then * / // %, then + -, left to right

round(3.14159, 2)    # 3.14
abs(-3)              # 3
```

`%` is how you test even and odd (`n % 2 == 0`), and how you split things into hours
and minutes.

---

## Text

```python
name = "Ada"
f"Hello {name}"          # puts values into text. The f is required
f"{price:.2f}"           # two decimal places
f"[{value:>5}]"          # right-align in a width of 5
f"[{name:<5}]"           # left-align in a width of 5

"Age: " + str(25)        # "Age: 25"  + glues text, but both sides must be text
"=" * 10                 # "=========="  repeats the text
"a\tb"                   # \t is a tab
"line one\nline two"     # \n starts a new line

len(name)                # 3
name[0]                  # "A"     first. Positions start at ZERO
name[-1]                 # "a"     last
name[0:2]                # "Ad"    start included, end excluded
name[:2]                 # "Ad"    no start means from the beginning
name[1:]                 # "da"    no end means to the end
name[0:100]              # "Ada"   too big an end is fine for slices

name.upper()             # "ADA"   gives a NEW string
name.lower()
name.strip()             # removes spaces from both ends
name.strip(".,!?")       # removes those characters from both ends
name.title()             # each Word Starts With A Capital
name.replace("A", "B")
name.count("a")          # 1       how many times it appears
name.isalpha()           # True    only letters
"123".isdigit()          # True    only digits
name.startswith("A")     # True
name.split()             # gives a list of pieces
" ".join(words)          # puts a list back together
"x" in name              # False

name.strip().lower()     # chaining. Works left to right
```

String methods give you back a new string. They do not change the original. If
"nothing happened", you forgot to assign the result back.

A method is a function that belongs to a value. You write it after a dot, like
`name.upper()`.

---

## Input and output

```python
name = input("Name? ")           # always gives back TEXT
age = int(input("Age? "))        # convert it yourself
price = float(input("Price? "))  # int() refuses decimals

print("a", "b", "c")                 # a b c
print("a", "b", "c", sep="-")        # a-b-c
print("one", end="")                 # stays on the same line
print(" two")                        # one two
```

`"5" + 5` is a TypeError. `input()` always gives a string, no matter what was typed.
Whatever a person types is text, even `25`, which is the characters 2 and 5.

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

Watch out for `if answer == "yes" or "y"`, which is always true. The part `"y"` on its
own is a value, not a question, and any text that is not empty counts as true. Use
`if answer in ["yes", "y"]` instead, which asks whether `answer` is one of those.

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

Only the first matching branch runs, so put the strictest condition first. A branch
is one of the paths: the `if`, an `elif`, or the `else`.

An `if` can go inside another `if`. Indent the inner one by four more spaces.

---

## Loops

```python
for i in range(5):          # 0 1 2 3 4.  Stops BEFORE the end
    print(i)

for i in range(1, 6):       # 1 2 3 4 5
for i in range(0, 10, 2):   # 0 2 4 6 8
for i in range(5, 0, -1):   # 5 4 3 2 1
list(range(3))              # [0, 1, 2]  see what a range holds

for item in my_list:        # the natural way to walk a list
    print(item)

for letter in "hi":         # a string can be walked too: "h" then "i"
    print(letter)

for i in range(len(items)): # when you need the position as well
    print(i, items[i])

for i, item in enumerate(items, start=1):   # position and item together
    print(i, item)

for a, b in zip(list_a, list_b):            # two lists side by side
    print(a, b)

while count < 10:           # when you do not know how many times
    count += 1

while True:                 # keep going until something happens
    text = input("...")
    if text == "q":
        break

break        # leave the loop
continue     # skip the rest of this pass
```

A loop inside a loop is called nested. The inner loop runs all the way through for
every pass of the outer one.

The accumulator pattern (a variable such as `total` that grows on each pass) is everywhere.

```python
total = 0
for number in numbers:
    total += number
```

To check a loop by hand, trace it. Draw a table on paper with one column for each
variable and one row for each pass. Write down the new values after each pass.

If your program never stops, press the **Stop** button in your editor. If you started
it in a terminal, press `Ctrl` and `C` together. You will then see `KeyboardInterrupt`.
That is normal. It only means you stopped it.

---

## Lists

```python
items = [1, 2, 3]
items[0]              # first. Positions start at ZERO
items[-1]             # last
items[0] = 99         # replace an item. Lists can be changed
items[1:3]            # a slice: a new list, end excluded
items[:2]             # the first two
len(items)
sum(items)            # also min() and max()

items.append(4)       # add to the end
items.insert(0, 9)    # add at a position
items.remove(3)       # remove by value
items.pop()           # remove and give back the last
items.pop(0)          # remove and give back the first
items.sort()          # sorts IN PLACE
items.sort(reverse=True)   # biggest first
items.reverse()       # flips the order. It does NOT sort
sorted(items)         # gives a NEW sorted list
sorted(words, key=len)     # sort by length. key= says what to compare
sorted(words, reverse=True)

3 in items
items.count(3)
items.index(3)        # the position
```

List methods change the list. String methods do not. `items = items.append(4)` is a
bug, because `append` gives back `None`.

`b = a` does not copy a list, it gives it a second name. Use `b = a[:]` for a copy.

A list can hold lists. Lists of lists sort by their first item.

```python
pairs = [[95, "Grace"], [88, "Ada"]]
pairs[0]              # [95, "Grace"]
pairs[0][1]           # "Grace"
sorted(pairs)         # [[88, "Ada"], [95, "Grace"]]
```

---

## Dictionaries

```python
scores = {"Ada": 88, "Grace": 95}

scores["Ada"]              # 88.  KeyError if it is not there
scores.get("Bob")          # None instead of an error
scores.get("Bob", 0)       # a default instead

scores["Alan"] = 72        # adds a new key
del scores["Alan"]         # removes it
"Ada" in scores            # True. It checks the KEYS

for key in scores: ...
for value in scores.values(): ...
for key, value in scores.items(): ...      # the one you want most

len(scores)
sorted(scores)             # the keys, in order
copy = dict(scores)        # a real copy. b = a is not
```

`88 in scores` is False. `in` checks keys, and `88` is a value. Use
`88 in scores.values()`.

The counting pattern.

```python
counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1
```

Grouping into a dictionary of lists. Make the empty list first, then add to it.

```python
groups = {}
for word in words:
    letter = word[0]
    if letter not in groups:
        groups[letter] = []
    groups[letter].append(word)
```

A dictionary can hold dictionaries.

```python
grades = {"Ada": {"maths": 90, "art": 75}}
grades["Ada"]["maths"]     # 90
```

---

## Tuples

```python
point = (3, 4)          # like a list, but cannot be changed
single = (5,)           # a tuple with one item needs the comma
x, y = point            # unpacking
a, b = b, a             # the swap trick

for name, score in [("Ada", 88), ("Grace", 95)]:   # unpacks each pair
    print(name, score)
```

A function returning several values makes one.

Which one to use.

- A **list** holds many things in order, and you change it as you go.
- A **dictionary** holds things you look up by a name (a key).
- A **tuple** holds a few things that belong together and should not change, like
  `(x, y)`.

---

## Functions

```python
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

result = greet("Ada")
print(greet("Ada", "Hi"))
```

`def` only defines the function. Nothing runs until you call it with brackets, like
`greet("Ada")`. `greet` without brackets is the function itself, not a result.

`print` shows a human. `return` hands a value back to the program. If you forget the
`return`, the function gives back `None`, and you will see errors about `None` later.

The moment a `return` runs, the function stops. Any lines after it are skipped.

A function can call another function, as long as that one is defined before the call
happens.

Parameters and the variables you make inside a function are local. They do not exist
outside.

Parameters with a default must come last. `def f(a=1, b)` is a SyntaxError.

Give the wrong number of arguments and you get a TypeError, for example
`greet()` gives `missing 1 required positional argument: 'name'`.

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
else:
    print("Got it")           # runs only if nothing went wrong
finally:
    print("Done")             # runs every time
```

Catch specific error types. Never use a bare `except:`.

You can start an error yourself with `raise`.

```python
if age < 0:
    raise ValueError("age cannot be negative")
```

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
random.randint(1, 6)        # 1 to 6, both ends included
random.choice(["a", "b"])   # one item from a list
random.shuffle(items)       # mixes the list in place
random.sample(items, 3)     # 3 different items
random.uniform(1, 2)        # a float between 1 and 2
random.seed(1)              # makes the random numbers repeat each run

from math import sqrt      # imports just that name
import random as rnd       # a nickname
import math
math.pi                    # 3.14159...
math.floor(2.7)            # 2

import datetime
now = datetime.datetime.now()
now.strftime("%A %d %B %Y")    # a date as text, like "Monday 12 October 2026"
start = datetime.datetime(2025, 1, 10)
(now - start).days             # whole days between two dates

import json
json.dump(data, file)      # save a structure
data = json.load(file)     # load it back
```

Useful ones. `random`, `math`, `datetime`, `statistics`, `string`, `time`.

Never use `from module import *`.

Your own file is a module too. If `my_tools.py` is in the same folder, `import my_tools`
runs it, and `my_tools.double(5)` calls a function from it. Put the code that should
run only when you press Run under this guard.

```python
def double(n):
    return n * 2

if __name__ == "__main__":
    print(double(4))       # runs when you run this file, not when it is imported
```

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

More detail on each one is on the [errors page](/cheat-sheets/errors/).

---

## The five habits

1. Read the error from the BOTTOM UP, out loud. The last line says what went wrong.
   The `File ... line N` line above the code says where.
2. Print things to find out what is in them. `print(repr(x))` shows hidden spaces.
3. Run your code often, in small pieces.
4. When something is confusing, check the TYPE. `print(type(x))`.
5. Name things well. `total_price`, not `tp`.
