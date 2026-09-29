# Unit 09 exercises

These are lighter than the last few units on purpose. The final one is the real ending
of the course.

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

What is `random.seed` for, and why would you ever want random numbers that are not
random?

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
counts should be roughly equal, and this is a nice way to show that `random` is doing
what it claims.

You already have the counting pattern from unit 07 for the second half.

### 9.5 Random password generator

Ask how long the password should be, and generate one from letters, digits and a few
punctuation characters.

Use `random.choice` on a string of allowed characters, building the password up one
character at a time.

```
import string
string.ascii_letters # all upper and lower case letters
string.digits # 0 to 9
string.punctuation #!"#$%&'*+,-./:;<=>?@[\]^_`{|}~
```

Do not use this for a real password. Tell me why not.

### 9.6 Coin flip statistics

Flip a coin 1000 times and count the heads and tails. Print the counts and the
percentages.

Then run it a few times and look at how much the percentage moves around. Then try
100000 flips and see that it gets closer to 50 percent.

### 9.7 Pick a random name

Ask for a list of names, one per line, until they type `done`. Then pick one at random
and print it.

Then add an option to pick three different names, using `random.sample`.

### 9.8 Dates

Ask for a birth date in the form `YYYY-MM-DD`. Work out how many days ago that was, and
how old the person is in years.

`datetime` will work out the date for you.

```python
import datetime
birth = datetime.datetime.strptime(text, "%Y-%m-%d")
```

Then subtract two dates and see what you get. You will get a `timedelta` object, which
has a `.days` attribute. Work it out from there.

### 9.9 Your own module

Take the validation functions from unit 08 (`get_number`, `get_text`) and put them in a
file called `input_helpers.py`.

Then write a second file that imports them and uses them, as in `use_my_tools.py`.

Then add the main guard to `input_helpers.py` so that any test code at the bottom does
not run when it is imported.

### 9.10 A geometry helper module

Write a module called `shapes.py` with functions for the area of a rectangle, a circle,
and a triangle. Use `math.pi` for the circle.

Then write a program in a different file that imports it and asks the user which shape
they want.

This is the same structure as 9.9 but with functions that actually do something, and it
is the shape of a small real project.

---

## Stretch

### 9.11 Reaction timer

Show the user a message, wait a random number of seconds, tell them to press Enter, and
measure how long they take.

```python
import time
time.sleep(2) # wait 2 seconds
time.time # the current time as a number of seconds
```

The difference between two `time.time` calls is the elapsed time. This is the first
program here that does something you could not easily do by hand.

### 9.12 Number guessing with a limit

Rewrite the guessing game so that the user gets seven guesses, and if they run out, the
secret is revealed.

Then work out the best strategy. With a range of 1 to 100 and seven guesses, what is the
guaranteed way to win? Once you have worked it out, have the computer play perfectly
against itself and watch it.

This is called binary search (cutting the range in half each time) and it is one of the
really useful algorithms, and it is exactly the right thing to have found on your own by
now.

### 9.13 Rock paper scissors tournament

Write a program where the computer plays random moves against itself 1000 times, and
report how many times each move won.

Then make the computer play against a strategy that always picks rock. Before you run
it, write down your prediction for how often the random player wins, loses and draws.
Then run it and see.

Most people guess that the random player wins about two thirds of the time, on the
grounds that it can pick two moves that both beat rock. Work out why that is wrong, and
explain what the actual answer is and why.

### 9.14 Shuffle and sort

Ask for a list of names, shuffle it, then sort it, and print it both times.

Then print it sorted by length, and then by length reversed. Use the `key` argument
 from exercise 5.14.

Then answer this. Why does `random.shuffle()` change the list but `sorted()` does not?

### 9.15 Split your to-do list

Take the to-do list from exercise 8.15 and split it into two files. One file holds the
functions, with a main guard. The other file is the program that uses them.

This is the exercise about structure rather than new features, and it is the last
exercise about refactoring in the course. If it feels easy, that is a good sign.

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

Come and show me what you made.

---

## Where to go next

You have finished the course. Here is what is left, roughly in the order I would tackle
it.

1. **List comprehensions**.
   Twenty minutes, and they are everywhere.
2. **Classes**. The next big idea. It will
   make much more sense now that functions are comfortable.
3. **Type hints**.
   `def add(a: int, b: int) -> int:`. Not required, very common.
4. **Reading and writing better code,** which mostly means naming things well and
   keeping functions short.
5. **Testing,** meaning writing code that checks your other code.

And the most useful thing of all, which is not on any list. Write something you actually
want, badly, and then improve it. That is what everybody does, including people who have
been doing this for twenty years.
