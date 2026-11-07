---
title: Unit 09 exercises
sidebar:
  label: Exercises
---
These are lighter than the last few units on purpose. The last exercise is the real
ending of the course.

## Before you start

A **module** (a file of code you can import and use) gives you tools you did not write.
There are three ways to import one. All three work, and they differ only in how you
write the name afterwards.

```python
import math                # use it as math.sqrt(25)
from math import sqrt      # use it as sqrt(25)
import math as m           # use it as m.sqrt(25)
```

The numbers from `random` are not truly random. They come from a formula that starts at
some number, called the seed. `random.seed(5)` sets the starting number by hand. The
same seed always gives the same numbers. Without it, Python picks a different start
every time. Other `random` tools you will meet are `random.choice(items)` (one item),
`random.sample(items, n)` (n different items), `random.shuffle(items)` (mixes a list in
place) and `random.uniform(a, b)` (a decimal number between a and b).

To get the date and time, use `datetime`.

```python
import datetime
now = datetime.datetime.now()
print(now.year, now.strftime("%A"))   # the year, and the day of the week
```

Your own files are modules too. If `tools.py` holds a function `greet()`, then another
file in the same folder can write `import tools` and call `tools.greet()`. When you
import a file, Python runs every line of it that is not inside a function. To stop test
code at the bottom of a module from running on import, put it under this check.

```python
if __name__ == "__main__":
    print("This only runs when you run this file directly")
```

When you run a file directly, Python sets the variable `__name__` to `"__main__"`. When
the file is imported, `__name__` is the module's name instead. This check is called the
main guard.

---

## Warm-ups

### 9.1 Predict the output

```python
import random

random.seed(1)
print(random.randint(1, 100))
```

Run it twice. Does it give the same answer both times? Then remove the `seed` line and
run it twice again.

What is `random.seed` for, and why would you ever want random numbers that repeat?

### 9.2 Import styles

Rewrite this using a different import style, both other ways.

```python
import math
print(math.sqrt(25))
```

Then say which of the three you prefer and why.

### 9.3 The star import

Why is this a bad idea?

```python
from math import *
```

Give two concrete problems it can cause.

---

## Core

### 9.4 Dice roller

Ask how many dice to roll and how many sides each one has. Roll them, print each result,
and print the total and the average.

Then roll a six-sided die 1000 times and print how many times each number came up. The
counts should be roughly equal. This shows that `random` is doing what it claims.

You already have the counting pattern from unit 07 for the second half.

### 9.5 Random password generator

Ask how long the password should be, and generate one from letters, digits and a few
punctuation characters.

Use `random.choice` on a string of allowed characters, building the password up one
character at a time.

`string` is a module, so you import it. It holds ready-made text to choose from.

```python
import string
print(string.ascii_letters)  # all upper and lower case letters
print(string.digits)         # 0 to 9
print(string.punctuation)    # punctuation marks such as ! # $ % & ?
```

Do not use this for a real password. Explain why not.

### 9.6 Coin flip statistics

Flip a coin 1000 times and count the heads and tails. Print the counts and the
percentages.

Then run it a few times and look at how much the percentage moves around. Then try
100000 flips and see that it gets closer to 50 percent.

### 9.7 Pick a random name

Ask for a list of names, one per line, until the user types `done`. Then pick one at random
and print it.

Then add an option to pick three different names, using `random.sample`.

### 9.8 Dates

Ask for a birth date in the form `YYYY-MM-DD`. Work out how many days ago that was, and
how old the person is in years. A rough answer for the years is fine, for example the
number of days divided by 365.

`datetime` will work out the date for you. In this code, `text` is what the user typed.
`strptime` turns text into a date, and `"%Y-%m-%d"` describes the shape of that text
(year, month, day).

```python
import datetime
birth = datetime.datetime.strptime(text, "%Y-%m-%d")
now = datetime.datetime.now()
```

Then subtract the two dates (`now - birth`) and see what you get. You will get a
`timedelta` object (the gap between two dates), which has a `.days` attribute. Work it
out from there.

### 9.9 Your own module

Take the validation functions from unit 08 (`get_number`, `get_text`) and put them in a
file called `input_helpers.py`.

Then write a second file, in the same folder, that imports them and uses them. Call the
functions as `input_helpers.get_number(...)`.

Then add the main guard (the `if __name__ == "__main__":` check from "Before you start")
to `input_helpers.py`, with a test line under it. The test line must not run when the
file is imported.

### 9.10 A geometry helper module

Write a module called `shapes.py` with functions for the area of a rectangle, a circle,
and a triangle. Use `math.pi` for the circle.

Then write a program in a different file that imports it and asks the user which shape
they want.

This is the same structure as 9.9, with functions that calculate something. It is the
shape of a small real project.

---

## Stretch

### 9.11 Reaction timer

Show the user a message, wait a random number of seconds, tell them to press Enter, and
measure how long they take.

```python
import time
time.sleep(2) # wait 2 seconds
time.time() # the current time as a number of seconds
```

The difference between two `time.time()` calls is the elapsed time.

### 9.12 Number guessing with a limit

Rewrite the guessing game so that the user gets seven guesses, and if they run out, the
secret is revealed.

Then work out the best strategy. With a range of 1 to 100 and seven guesses, what is the
guaranteed way to win? Once you have worked it out, write a version where the computer
plays that strategy against itself, with the same seven guesses, and watch it.

The strategy is called binary search (cutting the range in half each time). Try it
yourself before you read the solution.

### 9.13 Rock paper scissors tournament

Write a program where the computer plays 1000 rounds of rock paper scissors, with two
players that both pick random moves. Count how many rounds the first player won, how
many the second player won, and how many were draws.

Then make the first player a random player, and the second player a strategy that
always picks rock. Before you run it, write down your prediction for how often the
random player wins, loses and draws. Then run it and see.

Most people guess that the random player wins about two thirds of the time, on the
grounds that it can pick two moves that both beat rock. Work out why that is wrong, and
explain what the actual answer is and why.

### 9.14 Shuffle and sort

Ask for a list of names, shuffle it, then sort it, and print it both times.

Then print it sorted by length, and then by length reversed. Use the `key` argument
from exercise 5.14.

Then answer this. Why does `random.shuffle()` change the list but `sorted()` does not?

### 9.15 Split your to-do list

Take the basic to-do list from exercise 8.15 (save, load, add and remove, with items
stored as plain text) and split it into two files. One file holds the functions, with a
main guard. The other file is the program that uses them. If you added extra features
such as marking items as done, the functions that show and change the list must handle
those too.

This exercise is about structure rather than new features.

---

## The last exercise

### 9.16 Write something you want

No prompt. No starter code. No requirements. From an empty file, write a program.

Something small, and something you personally want. A tool to track something, a silly
generator, a quiz, a game, a calculator for something specific to you. It does not
matter what it is.

Some advice, which is the same advice for every project from now on.

- Start with the smallest version that does anything at all.
- Get that running before adding anything.
- When something breaks, read the error before changing anything.
- Add one thing at a time.
- Save often.

If you get stuck, ask a smaller question. Not "how do I write this program", but "how do
I get this one value onto the screen".

Show what you made to someone, or keep it and come back to it later.

---

## Where to go next

You have finished the course. Here is what is left, in a sensible order.

1. **List comprehensions** (a short way of writing a loop that builds a list),
   such as `[x * 2 for x in numbers]`. Twenty minutes, and they are everywhere.
2. **Classes** (a way to invent your own kind of thing). The next big idea. It will
   make much more sense now that functions are comfortable.
3. **Type hints** (optional notes about the types, which other tools can check),
   such as `def add(a: int, b: int) -> int:`. Not required, very common.
4. **Reading and writing better code,** which mostly means naming things well and
   keeping functions short.
5. **Testing,** meaning writing code that checks your other code.

And the most useful thing of all, which is not on any list. Write something you actually
want, badly, and then improve it. That is what everybody does, including people who have
been doing this for twenty years.
