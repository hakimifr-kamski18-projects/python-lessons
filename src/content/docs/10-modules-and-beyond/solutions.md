---
title: Unit 09 solutions
sidebar:
  label: Solutions
---
## Warm-ups

### 9.1 Predict the output

With `random.seed(1)` in place, both runs give the same answer, which on current Python
is `18`. Remove the `seed` line and the two runs give different answers.

`random.seed(n)` sets the starting point for the random number generator. It does not
make the numbers any less random, it makes them repeatable. Give the same seed and you
get the same sequence every time.

People want this for reproducibility (getting the same result again). If a bug only
shows up occasionally, and it depends on random numbers, you cannot debug it unless you
can make the same random sequence happen again. Seeding lets you replay the exact run that failed.

It is also how you write tests for code that uses randomness. Set the seed, run the
test, and expect a specific answer.

The seed value itself does not matter. It is not a secret and it does not need to be
random. It just has to be the same every time you want the same sequence.

### 9.2 Import styles

```python
# the original
import math
print(math.sqrt(25))
```

```python
# importing the name directly
from math import sqrt
print(sqrt(25))
```

```python
# with a nickname
import math as m
print(m.sqrt(25))
```

The one to prefer is the first one. The dot tells you where the name came
from, so `math.sqrt` is self-explanatory and a bare `sqrt` is not. Predicting where a
name comes from is a real part of reading code.

The nickname form is useful for long module names, and the direct form is fine for one
or two names that are unambiguous.

### 9.3 The star import

`from math import *` pulls every public name out of the module and drops it into your
file as if you had defined it yourself.

Two concrete problems.

**It hides where things came from.** Seeing `sqrt(16)` in a file gives you no clue
whether that is from the standard library, from a file you wrote, or from something you
installed. In a large file, you really cannot tell.

**It can silently overwrite your own names.** If you defined a variable or function
called `floor`, and then do `from math import *`, your `floor` is replaced by the one
from `math`, with no warning and no error. Your code then behaves wrongly in a way that is very
hard to find, because the line that caused it is nowhere near the symptom.

For `math` specifically the damage is mild, since the names are distinctive. For larger
modules, star imports are a real source of mysterious bugs. The rule is simply never to
use them.

---

## Core

### 9.4 Dice roller

```python
import random

how_many = int(input("How many dice? "))
sides = int(input("How many sides? "))

total = 0
rolls = []

for i in range(how_many):
    roll = random.randint(1, sides)
    rolls.append(roll)
    total += roll
    print(f"Die {i + 1}: {roll}")

print(f"Total: {total}")
print(f"Average: {total / how_many:.2f}")

print()

# now 1000 rolls of a six sided die
counts = {}

for i in range(1000):
    roll = random.randint(1, 6)
    counts[roll] = counts.get(roll, 0) + 1

for face in sorted(counts):
    print(f"{face}: {counts[face]}")
```

The counts should come out roughly 166 each, without being exactly equal. That uneven
spread is expected. If they came out exactly equal, something would be wrong with the
random number generator.

Run it a few times and watch the numbers move around. Real random numbers are lumpier
than most people expect.

Note that `random.randint(1, 6)` includes both 1 and 6, unlike `range()`, which stops
before the end.

### 9.5 Random password generator

```python
import random
import string

length = int(input("Password length: "))

allowed = string.ascii_letters + string.digits + "!@#$%^&*"

password = ""
for i in range(length):
    password += random.choice(allowed)

print(password)
```

You should not use this for a real password because `random` is built for games and
simulations. A person who sees enough of its output can work out what comes next, and
an attacker who can do that can guess your password.

There is a separate module for this, `secrets`, which is designed to be unguessable. The
change is small.

```python
import secrets
password += secrets.choice(allowed)
```

There is a right and a wrong way to generate random numbers, and the wrong way looks
identical. A program that works and a program that is correct can be different things.

### 9.6 Coin flip statistics

```python
import random

heads = 0
tails = 0

for i in range(1000):
    if random.choice(["heads", "tails"]) == "heads":
        heads += 1
    else:
        tails += 1

print(f"Heads: {heads} ({heads / 10:.1f}%)")
print(f"Tails: {tails} ({tails / 10:.1f}%)")
```

The percentage is `heads / 1000 * 100`, which simplifies to `heads / 10`. Write it the
long way first so the arithmetic is clear.

Running it several times, the percentages wander around 50 by a few points. At 100000
flips, they get much closer. That is the law of large numbers (more trials give results
closer to the true chance), and you can see it happen in your own program.

If you are interested, you can run the experiment 100 times and plot the spread of
results, which is a nice thing to do with a list and a loop.

### 9.7 Pick a random name

```python
import random

names = []

while True:
    name = input("Name (or 'done'): ").strip()
    if name.lower() == "done":
        break
    if name:
        names.append(name)

if not names:
    print("No names")
else:
    print(f"Chosen: {random.choice(names)}")

    if len(names) >= 3:
        print("Three of you:")
        for name in random.sample(names, 3):
            print(f" {name}")
    else:
        print("Not enough names for three")
```

`random.choice` picks one item and can pick the same one again if you call it twice.
`random.sample` picks several **different** items, and it will not repeat.

Remember this difference. Calling `choice()` three times in a loop to pick a team of
three can pick the same person twice, which is a bug. `sample()` is the right tool for
this.

The `len(names) >= 3` check exists because `random.sample` raises a `ValueError` if you
ask for more items than there are.

### 9.8 Dates

```python
import datetime

text = input("Birth date (YYYY-MM-DD): ").strip()
birth = datetime.datetime.strptime(text, "%Y-%m-%d")
now = datetime.datetime.now()

difference = now - birth

print(f"That was {difference.days} days ago")
print(f"That is about {difference.days // 365} years")
print(f"You were born in {birth.year}")

weekday = birth.strftime("%A")
print(f"That was a {weekday}")
```

Subtracting two dates gives a `timedelta` object, and `.days` is how many days it
covers. The rest of the `timedelta`, hours and seconds, is whatever time of day the two
dates happened to be at, which is usually not interesting.

`difference.days // 365` is an approximation and it will be wrong for people whose
birthday has not happened yet this year. Doing it exactly means comparing months and
days, which is fiddly. So this answer is not exact, and it is up to you whether to fix
it.

`strftime("%A")` turns a date into text, here the name of the day of the week. Each
`%` code stands for one part of the date. Look the codes up when you need them instead
of memorising them.

If the input does not match the format, `strptime` raises a `ValueError`. This is the
same error handling as unit 08, so a validation loop (a loop that asks again until the
answer is valid) works well here.

### 9.9 Your own module

`input_helpers.py`.

```python
def get_number(prompt):
    while True:
        text = input(prompt).strip()
        try:
            return int(text)
        except ValueError:
            print("That is not a whole number, try again")


def get_text(prompt):
    while True:
        text = input(prompt).strip()
        if text:
            return text
        print("You have to type something")


if __name__ == "__main__":
    print(get_number("Test: "))
```

And the file that uses it.

```python
import input_helpers

name = input_helpers.get_text("Name: ")
age = input_helpers.get_number("Age: ")

print(f"{name} is {age}")
```

The main guard is what stops the test line at the bottom of `input_helpers.py` from
running when the second file imports it. Prove it by removing the guard,
running the second file, and watching the test prompt appear before your own program
even starts.

Now you have seen the problem that the guard fixes.

### 9.10 A geometry helper module

`shapes.py`.

```python
import math

def rectangle_area(width, height):
    return width * height

def circle_area(radius):
    return math.pi * radius ** 2

def triangle_area(base, height):
    return base * height / 2


if __name__ == "__main__":
    print(rectangle_area(3, 4))
```

And the program.

```python
import shapes

print("1. Rectangle 2. Circle 3. Triangle")
choice = input("Which shape? ").strip()

if choice == "1":
    width = float(input("Width: "))
    height = float(input("Height: "))
    print(f"Area: {shapes.rectangle_area(width, height):.2f}")

elif choice == "2":
    radius = float(input("Radius: "))
    print(f"Area: {shapes.circle_area(radius):.2f}")

elif choice == "3":
    base = float(input("Base: "))
    height = float(input("Height: "))
    print(f"Area: {shapes.triangle_area(base, height):.2f}")

else:
    print("I did not understand that")
```

Note that `shapes.py` does not print anything at all, and does not ask for input. It is
a file of functions that only calculate and return values, and that is what makes it
reusable. A module that asks questions when you import it is a module you can only use
in one way.

Keep code that talks to the user separate from code that produces values. This is a good
design rule.

---

## Stretch

### 9.11 Reaction timer

```python
import random
import time

input("Press Enter to start...")
print("Wait for it...")

time.sleep(random.uniform(1.5, 4.0))

start = time.time()
input("NOW! Press Enter!")
elapsed = time.time() - start

print(f"Your reaction time: {elapsed:.3f} seconds")

if elapsed < 0.25:
    print("That is suspiciously fast. Did you press Enter early?")
```

`time.sleep(n)` pauses for `n` seconds, and it accepts decimals. `random.uniform(a, b)`
gives a random float between the two, unlike `randint()` which gives whole numbers.

`time.time` gives the current time as a number of seconds since some starting point in
1970. The actual number is meaningless, and the difference between two of them is what
you want.

The check for an implausibly fast reaction is useful, because people sometimes press
Enter early.

`time` also has `time.perf_counter`, which is better for measuring short durations
because it does not jump around if the system clock changes.

### 9.12 Number guessing with a limit

```python
import random

def play():
    secret = random.randint(1, 100)

    for attempt in range(7):
        guess = int(input(f"Guess {attempt + 1}/7: "))

        if guess < secret:
            print("Too low")
        elif guess > secret:
            print("Too high")
        else:
            print(f"Correct in {attempt + 1}")
            return True

    print(f"Out of guesses. It was {secret}")
    return False

play()
```

The `return True` and `return False` let the caller find out what happened without
printing inside the function. This is the unit 06 idea of returning values instead of
printing them.

The strategy is to always guess the middle of the remaining range. With 1 to
100, guess 50, then 25 or 75, and so on. Each guess halves what is left, and seven
guesses is enough because 2 to the power 7 is 128, which is more than 100.

The computer playing against itself looks like this. It needs `import random` from the
block above.

```python
def computer_play():
    secret = random.randint(1, 100)
    low = 1
    high = 100

    for attempt in range(7):
        guess = (low + high) // 2
        print(f"Guess {attempt + 1}: {guess}")

        if guess == secret:
            print(f"Found it in {attempt + 1}")
            return
        elif guess < secret:
            low = guess + 1
        else:
            high = guess - 1

    print("Failed")
```

The two variables `low` and `high` track the range that the answer could still be in,
and each guess cuts it in half. This is binary search, and it is the same method behind
searching a sorted list, and behind the "guess the number between 1 and 1000" trick.

### 9.13 Rock paper scissors tournament

```python
import random

moves = ["rock", "paper", "scissors"]

def beats(a, b):
    return (a == "rock" and b == "scissors") or \
           (a == "scissors" and b == "paper") or \
           (a == "paper" and b == "rock")

# first part: two random players
first_wins = 0
second_wins = 0
draws = 0

for i in range(1000):
    first = random.choice(moves)
    second = random.choice(moves)

    if first == second:
        draws += 1
    elif beats(first, second):
        first_wins += 1
    else:
        second_wins += 1

print(f"First: {first_wins}, Second: {second_wins}, Draws: {draws}")

# second part: a random player against always rock
wins = 0
losses = 0
draws = 0

for i in range(1000):
    random_move = random.choice(moves)
    fixed_move = "rock"

    if random_move == fixed_move:
        draws += 1
    elif beats(random_move, fixed_move):
        wins += 1
    else:
        losses += 1

print(f"Wins: {wins}, Losses: {losses}, Draws: {draws}")
```

With two random players, each of the three results comes out at roughly a third. Against
always-rock the answer is the same, roughly a third of each.

The wrong reasoning is "two of the three moves beat rock, so the random player wins two
thirds of the time". The flaw is that only one move beats rock, which is paper. Scissors
loses to rock, and rock against rock is a draw. So the three outcomes are one third win,
one third lose, one third draw, and the random player does no better than always-rock.

Always-rock is not a bad strategy against random play. Wins and losses are equal, and a
third of the rounds are draws. Rock only loses to a fixed strategy that always plays
paper, and only wins against one that always plays scissors.

If you want to take it further, find the strategy that beats always-rock reliably (it
is always-paper, which wins every round). Then note that always-paper loses every round
to always-scissors. This circle is what makes rock paper scissors interesting. No
single strategy beats all the others.

### 9.14 Shuffle and sort

```python
import random

names = ["Ada", "Grace", "Alan", "Barbara", "Edsger"]

random.shuffle(names)
print("Shuffled:", names)

print("Sorted: ", sorted(names))
print("By length:", sorted(names, key=len))
print("Longest first:", sorted(names, key=len, reverse=True))
```

`random.shuffle` changes the list in place (changed directly, without a copy) and
returns `None`. `sorted()` returns a new list and leaves the original alone. This is the
same difference as `sort()` and `sorted()` in unit 05.

`shuffle` is a function from `random`, not a list method. There is no built-in that
returns a shuffled copy, but `random.sample(names, len(names))` does the same job and
leaves the original list alone.

### 9.15 Split your to-do list

`todo_lib.py`.

```python
import json

def load_todos(filename):
    try:
        with open(filename) as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except ValueError:
        print("The save file is damaged, starting fresh")
        return []


def save_todos(filename, todos):
    with open(filename, "w") as file:
        json.dump(todos, file, indent=2)


def show_todos(todos):
    if not todos:
        print("(nothing to do)")
        return
    for i, todo in enumerate(todos, start=1):
        print(f"{i}. {todo}")


def get_number(prompt):
    while True:
        text = input(prompt).strip()
        try:
            return int(text)
        except ValueError:
            print("Please enter a number")


if __name__ == "__main__":
    print("This is the library file. Run todo.py instead.")
```

And `todo.py`.

```python
import todo_lib

FILENAME = "todos.json"

todos = todo_lib.load_todos(FILENAME)

while True:
    print()
    todo_lib.show_todos(todos)

    print("\n1. Add 2. Remove 3. Quit")
    choice = input("Choose: ").strip()

    if choice == "1":
        todos.append(input("What? ").strip())
        todo_lib.save_todos(FILENAME, todos)
    elif choice == "2":
        index = todo_lib.get_number("Which number? ")
        if 1 <= index <= len(todos):
            print(f"Removed: {todos.pop(index - 1)}")
            todo_lib.save_todos(FILENAME, todos)
        else:
            print("No such item")
    elif choice == "3":
        break
```

This solution splits the basic version of 8.15, where each item is plain text. The
improvement over the single file version is that the filename becomes a parameter rather
than a fixed string. Now the library can be used for more than one list, and you can
test it without touching a real file.

Note also that `todo.py` is almost entirely input and output, and the other work lives
in the library. A program that has grown large should take this shape.

---

## The last exercise

There is no solution to 9.16, on purpose. Whatever you wrote is the answer.
