---
title: Unit 09 — Modules and what comes next
sidebar:
  hidden: true
pagefind: false
prev: false
next: false
---
**Files for this unit.** [`main_guard.py`](/code/09-modules-and-beyond/main_guard.py), [`modules_demo.py`](/code/09-modules-and-beyond/modules_demo.py), [`my_tools.py`](/code/09-modules-and-beyond/my_tools.py), [`use_my_tools.py`](/code/09-modules-and-beyond/use_my_tools.py)

These live in `public/code/09-modules-and-beyond/` in the repository, and the links above
open them as plain text. Every snippet the student needs is already inline in the
exercises, so the files are for the session itself, when you are both at the
keyboard.

**Goal for the session.** They can find and use code other people wrote, they can split
their own code across files, and they know what to learn next.

**Time.** One to two sessions. This unit is lighter than the last few on purpose, and it
is partly a wrap-up.

**Prerequisites.** Everything. This is the last unit.


---

## 0. Warm-up

Have them write a program that saves and loads a dictionary (a collection you look
things up in by name) with `json`, with no notes. That is the unit 08 retrieval check
and it should be quick.

Then ask them the closing question from last session. "What do you do when you need
something Python does not seem to have?" That is today.

## 1. Modules

They have already used `import random` (pull a module in so you can use it) in unit 04
and `import json` in unit 08. Now they get the full story.

A module (a file of code you can import) is a file full of code that somebody else
wrote, which you can use.

```python
import random

print(random.randint(1, 6))
print(random.choice(["rock", "paper", "scissors"]))
```

The `import` statement makes the module available, and then you reach into it with a
dot. `random.randint` means the `randint` thing that lives inside `random`.

### The three ways to import

```python
# 1. import the module, use it with a dot
import random
print(random.randint(1, 6))
```

```python
# 2. import names directly
from random import randint
print(randint(1, 6))
```

```python
# 3. import names with a nickname
import random as rnd
print(rnd.randint(1, 6))
```

The first is the one to use by default. The dot is a feature, not annoying, because it
tells you where the name came from. Six months later, `random.randint` is clear and
`randint` could be anything.

The third form is common for a few modules with long names, and you will see `import
numpy as np` all over the internet. Not needed here.

The second form is the one to be careful about.

```python
from math import *

sqrt(16)      # where did sqrt come from?
```

That star import pulls in every name from the module without telling you what they are.
It makes code hard to read and it can overwrite your own variables silently. Tell them
never to use it, and to recognise it when they see it in tutorials.

### `import` needs the module to exist

```python
import maths      # ModuleNotFoundError
```

Have them see that error once. It is the same shape as `NameError`, and the fix is
either the right name or installing the thing, which is section 4.

## 2. A tour of the standard library

Open [`modules_demo.py`](/code/09-modules-and-beyond/modules_demo.py). Python ships with a huge library and they only need to know
a few parts of it exist.

### `random`

```python
import random

random.randint(1, 6)              # a whole number from 1 to 6, both included
random.choice(["a", "b", "c"])    # a random item from a list
random.shuffle(items)             # shuffles a list in place (changed directly, without a copy)
random.sample(items, 3)           # three different items
```

Note `shuffle` changes the list and returns `None`, exactly like `sort` and `append`
from unit 05. The command-sounding name rule applies.

### `math`

```python
import math

math.sqrt(16)         # 4.0
math.pi               # 3.141592653589793
math.floor(3.7)       # 3
math.ceil(3.2)        # 4
math.factorial(5)     # 120
```

Note `math.floor` and `math.ceil` alongside `int()`. `int(3.7)` truncates toward zero,
so `int(-3.7)` is `-3`, while `math.floor(-3.7)` is `-4`. That difference surprises
people and is worth showing.

### `datetime`

```python
import datetime

now = datetime.datetime.now()
print(now.year, now.month, now.day)
print(now.strftime("%Y-%m-%d %H:%M"))
```

`strftime` formats a date as text. The percent codes are fiddly and there is no point
memorising them. Tell them to search for "python strftime" when they need one.

Date arithmetic is really awkward, and the honest advice is to look it up when you need
it rather than learning it now.

### `statistics`

```python
import statistics

numbers = [4, 7, 2, 9, 4]

statistics.mean(numbers)        # 5.2
statistics.median(numbers)      # 4
statistics.mode(numbers)        # 4
```

Which is a nice thing to show, since they wrote all of these by hand in unit 04.

### `pathlib` and working with files

```python
from pathlib import Path

Path("data.txt").exists()
Path(".").iterdir()             # what is in this folder
```

Not needed for anything in this course, but worth knowing it exists so that directory
work does not feel impossible.

### The point of the tour

There are hundreds of modules. Nobody knows them all. The skill is knowing that the
standard library probably has something for your problem, and being able to find it.

Tell them the two habits that matter more than any list.

1. Search for "python how to do X" and expect a standard library answer.
2. Read the official docs at docs.python.org. They are better than most tutorials,
   and they have a search box.

## 3. Splitting your own code across files

Open [`my_tools.py`](/code/09-modules-and-beyond/my_tools.py) and [`use_my_tools.py`](/code/09-modules-and-beyond/use_my_tools.py).

`my_tools.py` is a file with some functions in it. Nothing special.

```python
# my_tools.py
def get_number(prompt):
    ...
```

`use_my_tools.py` is a different file in the same folder, which uses them.

```python
# use_my_tools.py
import my_tools

age = my_tools.get_number("Age: ")
```

That is all there is to it. Your own files are modules too, as long as they are in the
same folder.

This matters for a practical reason. Once a program gets past a couple of hundred lines,
one file is hard to work with. Splitting it into a file of functions and a file that
uses them is the first step, and it is worth doing on purpose once so they know it is
allowed.

### The main guard

Open [`main_guard.py`](/code/09-modules-and-beyond/main_guard.py). This is a small piece of boilerplate (fixed code you copy
without changing much) that looks mysterious and has a simple explanation.

```python
def main():
    print("Running the program")

if __name__ == "__main__":
    main()
```

The problem it solves. If another file does `import my_tools`, Python runs the top level
of `my_tools.py`, and anything not inside a function gets executed. So if `my_tools.py`
has a print at the bottom for testing, that print fires whenever anyone imports it.

The guard (a check that stops something bad happening) says "only run this when this
file is run directly, not when it is imported".

The explanation of `__name__`. When you run a file directly, Python sets a variable
called `__name__` to the string `"__main__"`. When a file is imported, `__name__` is the
name of the module instead. So the check is "am I the file that was run?"

Have them show it. Run `main_guard.py` directly and see the message. Then import it from
another file and see that the message does not appear.

Tell them they do not need this yet, and that they will see it in every real Python file
they open, so it is worth recognising.

## 4. Installing things other people wrote

The standard library is what comes with Python. Everything else is on PyPI and installed
with `pip`.

```
pip install requests
```

Then you can import it like anything else.

```
python3 -m pip install requests
```

The `python3 -m pip` form is the one to prefer, because it installs into the same Python
that `python3` runs. Plain `pip` sometimes refers to a different installation and it is
a common source of "I installed it but Python cannot find it".

### Virtual environments, briefly

Explain the problem, not the full solution.

If you install packages (bundles of code somebody else wrote, that you install) into
your system Python, you end up with one shared pile of packages for every project, and
two projects that need different versions of the same library cannot both work. So each
project gets its own folder of packages.

```
python3 -m venv .venv
source .venv/bin/activate          # Linux and macOS
.venv\Scripts\activate             # Windows
pip install requests
```

That is really all they need to know for now. They do not need to do it in this course,
since nothing here uses third party packages. But the moment they follow a tutorial that
says `pip install`, they will meet it, and knowing the words "virtual environment" (a
private folder of packages for one project) means they can search for the rest.

### The honest warning

Do not install things from the internet casually. Packages run with the same permissions
as your own code, and there is a real problem with malicious ones, especially packages
with names that look almost like a popular one. Tell them to check that the name is
right and to prefer packages with plenty of users.

## 5. A few last language features

Short, and mostly for recognition rather than use.

### `None`, properly

They have met it several times. It is the value that means "nothing".

```python
result = None

if result is None:
    print("there is nothing there")
```

Compare with `is` rather than `==` when checking for `None`, because `is` asks whether
it is literally the same object. It is the usual way, and everyone follows it.

And the short way, using the truthiness from unit 03.

```python
if not result:
    print("there is nothing there")
```

Which is shorter and slightly different, since it is also true for `0`, `""` and empty
collections. Be deliberate about which you mean.

### Conditional expressions

A one-line `if`. They may have seen it in a solution file.

```python
mark = "x" if done else " "
```

Which is the same as.

```python
if done:
    mark = "x"
else:
    mark = " "
```

Read out loud it is "x if done, otherwise a space". It is worth knowing so it does not
look like a typo, and the two line version is usually clearer.

### Functions that take functions

They met this in exercise 6.20 and in `sorted(key=len)`. A very brief reminder.

```python
words = ["banana", "fig", "apple"]
print(sorted(words, key=len))
print(sorted(words, key=str.lower))
```

The `key` argument takes a function and calls it on each item to decide the order. That
is all.

### The things not taught on purpose

Be honest with them about this list, because it is where the course stops.

- **Classes** (a way to invent your own kind of thing). It is the next big topic and
  it is much easier once functions are comfortable.
- **List comprehensions** (a short way of writing a loop that builds a list).
  `[x * 2 for x in numbers]`. Shorter than the loop version and everywhere in real
  code. Twenty minutes to learn once loops are solid.
- **Decorators** (a label above a function that changes how it behaves), `@something`.
  They will see them and they are not scary, just unexplained for now.
- **Generators and `yield`** (a way to produce values one at a time instead of all at
  once).
- **Type hints** (optional notes about the types, which other tools can check).
  `def add(a: int, b: int) -> int:`. Very common in modern code.
- **Writing your own exceptions,** meaning your own kinds of error, and class
  hierarchies.
- **Async** (for doing several things at the same time). Only needed for a specific
  kind of program.

The message. Everything left is a smaller step than the ones they have already taken.
Unit 04, loops, and unit 06, functions, were the hard parts, and both are behind them.

## 6. Writing a program from nothing

The last thing to do with them, and it is the real ending of the course.

Ask them to write something from an empty file, with no exercise prompt, no starter
code, and no list of requirements. Anything they want. Something small.

Then let them work, and only answer questions. Do not suggest features, do not fix their
structure, do not steer.

Signs to look for that the course worked.

- They start with data, or with a list of what the program should do, rather than
  typing `print` and hoping.
- They run the program often and in small pieces, rather than writing fifty lines and
  then running it.
- When something fails, they read the error before asking.
- They use functions without being told to.
- They test with a small case first.

If they get stuck, the useful question is "what is the smallest version of this that
would do something?" Almost every project is easier once you have a tiny version
running.

---

## Teaching notes for this unit

**This unit is a wind-down, and it should feel like one.** The bulk of the learning
happened in units 03 to 07. Do not introduce pressure here.

**Do not try to cover the whole standard library.** Pick three modules they will
actually use and let the rest be a list of names. `random` and `datetime` are the two
that will come up in their own projects.

**The `pip` and virtual environment material is awareness only.** They will forget the
commands and that is fine, as long as they recognise the words when they meet them in a
tutorial.

**The main guard is pure boilerplate.** Show it, explain it once, and tell them to copy
it. Do not let it become a mysterious line that scares them.

**Be honest about what is not taught.** A student who knows that classes exist and are
learnable is in a very different position from one who thinks they have finished and
there is nothing left.

**The free project is the assessment, and there is no grade.** If they can write
something small without help, the course worked. If they freeze on an empty file, that
is useful information, and the fix is more exercises from units 04 to 07 rather than
more new material.

**Leave them with somewhere to go.** Recommend the official tutorial at
docs.python.org/3/tutorial, and tell them that the best next step is to write something
they personally want, badly, and then improve it. That is what everyone does.

**Stay in touch.** If they have enjoyed it, offer to look at whatever they write next,
or to pair with them on a small project. The course ending well matters more than the
course covering everything.

**The reaction timer.** Mention `time.perf_counter` once.

**The last exercise.** When you look at it, the things worth commenting on are not the
code style or the features. They are these.

- Did they get something running early and build on it?
- Did they read their errors, or did they ask you first?
- Did they use functions, without being reminded?
- Can they explain what each part does?
- Do they know what they would add next?

If the answer to all five is yes, the course worked regardless of what the program does.

And if the program is short and unfinished, that is also a completely normal outcome,
and a much better one than a large program they cannot explain. Something small that
they understand and could extend is the right place to stop.

Then tell them what to do next, which is to keep going on the same thing, or start
something else, and to come back when they get stuck. That offer is the last piece of
teaching in the course, and it matters more than unit 09 does.
