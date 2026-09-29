# Unit 04 — Repetition

**Goal for the session.** Their programs can do the same thing many times, and they know
the accumulator pattern (a variable you add to on every pass), which is the basis of
about half of all beginner programming.

**Time.** Two sessions. This is the biggest conceptual jump in the whole course, and the
unit where students either start to feel powerful or start to feel lost. Do not compress
it.

**Prerequisites.** Unit 03. Conditionals, comparison, combined conditions.

**Files used.** `code/while_loop.py`, `code/for_loop.py`, `code/accumulator.py`,
`code/break_continue.py`

---

## 0. Warm-up

Have them write an even or odd checker from scratch, with no notes. That is the unit 03
retrieval check.

Then ask them this question, and let it sit for a moment. "How would you print the
numbers 1 to 100? Write the code." Let them start writing a hundred print lines, and
stop them after a few. That frustration is the motivation for today.

## 1. `while`

Start here, because it makes how it works visible. `for` later is then a convenience
rather than a mystery.

Open `code/while_loop.py`.

```python
count = 1

while count <= 5:
    print(count)
    count = count + 1

print("Done")
```

Trace it before running, out loud, one pass at a time. Ask them to say the value of
`count` at each step.

```
count is 1  -> 1 <= 5 is True  -> print 1, count becomes 2
count is 2  -> 2 <= 5 is True  -> print 2, count becomes 3
...
count is 5  -> 5 <= 5 is True  -> print 5, count becomes 6
count is 6  -> 6 <= 5 is False -> loop ends
```

The structure to name.

- Something set up before the loop, here `count = 1`.
- A condition that is checked before every pass.
- Something inside the loop that eventually makes the condition false.

That third piece is the one beginners forget, and forgetting it gives an infinite loop.

### The infinite loop, on purpose

Have them delete the `count = count + 1` line and run it. The output scrolls forever.
Let it run for a few seconds, then tell them to press Ctrl+C in the terminal to stop it.

Two things to get from this.

- Ctrl+C is how you stop a runaway program, and it is a normal part of
  programming rather than a failure state. Everyone writes infinite loops, all the
  time, forever.
- Forgetting to change the thing the condition depends on is the single most common
  loop bug.

Put the line back and confirm it works.

### `while` with a condition on the data

A `while` does not need a counter. It can run until some condition in the program
becomes true.

```python
total = 0
number = int(input("Number to add (0 to finish): "))

while number != 0:
    total = total + number
    number = int(input("Number to add (0 to finish): "))

print(f"Total: {total}")
```

Ask them to trace this with the inputs 5, 3, 0. The pattern where the same `input` line
appears both before the loop and inside it is a bit awkward. Spell it out, and say the
usual fix is `while True` with a `break`, which they will meet later in this unit.

## 2. `for` and `range()`

Open `code/for_loop.py`.

```python
for i in range(5):
    print(i)
```

Ask them to predict the output before running. It prints 0, 1, 2, 3, 4.

Four things to land.

**It starts at 0 and stops before the end.** So `range(5)` gives five numbers, 0 to 4,
not 1 to 5. This is the same "start included, end excluded" rule as string slicing,
which they already met in unit 02, and it is worth connecting the two.

**No counter to manage.** There is no `count = 1` before, and no `count = count + 1`
inside. Everything that was three pieces of manual bookkeeping in the `while` version is
handled by the `for`.

**The same loop in `while` form for comparison.** Have them write both and put them side
by side. That comparison is the whole point of showing `while` first.

```python
# while version
count = 0
while count < 5:
    print(count)
    count += 1

# for version
for i in range(5):
    print(i)
```

**The loop variable name is your choice.** `i` is the usual name for a counter and comes
from maths. More descriptive names are better when the meaning is not clear.

```python
for attempt in range(3):
    print(f"Attempt {attempt + 1}")
```

### `range()` in all its forms

```python
range(5)          # 0, 1, 2, 3, 4
range(1, 6)       # 1, 2, 3, 4, 5         start at 1, stop before 6
range(2, 11, 2)   # 2, 4, 6, 8, 10       step of 2
range(10, 0, -1)  # 10, 9, 8, ..., 1     counting down
```

Have them predict each one and then check. The trick for checking, which is really
useful.

```python
print(list(range(2, 11, 2)))
```

`list()` turns the range into a list they can see. They met `list` brackets briefly in
unit 02 with `split()`, and the full treatment is next session.

The countdown form `range(10, 0, -1)` is worth a minute, since generating a countdown is
the classic first loop and the natural attempt is `range(10, 0)`, which gives nothing at
all. Have them run that and be confused, then fix it with the `-1` step.

### The off-by-one rule

Say this out loud, and repeat it over the next few sessions.

To print 1 to 5, you write `range(1, 6)`. The end number is one more than the last
number you want.

Have them write `range(1, 5)` and see it stop at 4. Then have them fix it. This is worth
doing rather than just hearing, because it is a mistake they will make for months.

### Looping over text

A `for` loop can go over the characters of a string directly, without `range`.

```python
for letter in "Python":
    print(letter)
```

And over the pieces of a sentence.

```python
sentence = "the quick brown fox"

for word in sentence.split():
    print(word.upper())
```

Note to them that `split()` gives back several values in one box, and a `for` loop walks
through the box one at a time. That is a preview of unit 05, and it is safe to use now.

## 3. The accumulator pattern

Open `code/accumulator.py`. This is the most important section of the unit, and possibly
of the whole course.

The shape. Start with something, change it a little on every pass, look at it when you
are done.

```python
total = 0

for number in range(1, 6):
    total = total + number

print(total)     # 15
```

Trace it on paper with them, writing the value of `total` after each pass.

```
total = 0
pass 1: total = 0 + 1 = 1
pass 2: total = 1 + 2 = 3
pass 3: total = 3 + 3 = 6
pass 4: total = 6 + 4 = 10
pass 5: total = 10 + 5 = 15
```

Do the paper trace. It takes two minutes and it converts a mysterious loop into a clear
one.

### Three variations on the same shape

**Adding up.**

```python
total = 0
for number in range(1, 101):
    total += number
print(total)     # 5050
```

**Counting.**

```python
count = 0
for number in range(1, 101):
    if number % 2 == 0:
        count += 1
print(count)     # 50 even numbers
```

**Building up text.**

```python
result = ""
for word in ["python", "is", "fun"]:
    result = result + word + " "
print(result)    # "python is fun "
```

The third one has a trailing space, which is normal and usually fixed afterwards with
`.strip()`. Worth pointing out rather than letting them find it and worry.

**Tracking the biggest so far.**

```python
biggest = 0

for number in [3, 7, 2, 9, 4]:
    if number > biggest:
        biggest = number

print(biggest)   # 9
```

This one is different in an important way. The starting value has to be smaller than
anything you might see, or the pattern breaks. Ask them what happens if the list
contains only negative numbers. The answer is that `biggest` stays 0 and the answer is
wrong. That is a really instructive failure, and it is worth them finding it before they
need to know the fix.

### Asking the user how many times

The combination of `input`, `int` and `range`, which is the shape of most exercises in
this unit.

```python
count = int(input("How many numbers? "))
total = 0

for i in range(count):
    number = float(input(f"Number {i + 1}: "))
    total += number

print(f"Total: {total}")
```

Note `i + 1` in the prompt. The loop variable is 0-based, but humans count from 1. This
little adjustment appears constantly.

## 4. `break` and `continue`

Open `code/break_continue.py`.

`break` leaves the loop immediately. `continue` skips the rest of this pass and goes to
the next one.

```python
for number in range(1, 11):
    if number == 5:
        break
    print(number)
# prints 1 2 3 4
```

```python
for number in range(1, 11):
    if number == 5:
        continue
    print(number)
# prints 1 2 3 4 6 7 8 9 10
```

Have them predict both before running. Then ask them to describe the difference in their
own words. It is worth doing, because "break stops, continue skips" is easy to say and
easy to mix up under pressure.

Note that neither of these is a common thing to need at this stage, and using them to
patch a badly designed loop is a bad habit. The one place `break` is really the right
tool is `while True`.

### `while True` with `break`

The common way to write "keep going until something happens".

```python
total = 0

while True:
    text = input("Number to add, or q to finish: ").strip()

    if text.lower() == "q":
        break

    total += int(text)

print(f"Total: {total}")
```

This fixes the awkwardness from section 1, where the input line had to be written twice.
Explain the shape. `while True` is always true, so the loop runs forever, and the only
exit is the `break`, which is right there in the middle where a reader will see it.

The stopping condition is really inside the loop, which is honest, rather than
duplicated at the top where it is easy to get out of sync.

## 5. Nested loops

A loop inside a loop, which is nested (put inside another one). Show the triangle, which
is the classic.

```python
for row in range(1, 6):
    for star in range(row):
        print("*", end="")
    print()
```

Note `end=""`, which stops `print` from adding a newline so the stars stay on one line.
Then the bare `print()` at the end moves to the next line. This is the first time they
have needed `end`, so show the output without it first, one star per line, and then add
it.

Have them trace the outer loop by hand for `row = 1` and `row = 2`. Actually writing out
which stars are printed on each pass makes the nesting concrete.

```
row 1: star 0        -> *
row 2: star 0, star 1 -> **
row 3: star 0,1,2    -> ***
```

Do not do more than this with nesting. It is here so that a multiplication table, the
clear next exercise, does not look terrifying, and so that they have seen the shape.

## 6. Putting it together

Build a number guessing game together. It covers everything in the unit.

```python
import random

secret = random.randint(1, 100)
attempts = 0

while True:
    guess = int(input("Guess a number between 1 and 100: "))
    attempts += 1

    if guess < secret:
        print("Too low")
    elif guess > secret:
        print("Too high")
    else:
        print(f"Correct! You took {attempts} attempts")
        break
```

Explain what `import` does (it pulls a module in) and `random.randint` briefly. It gives
a random whole number between the two values, both included. The full story of modules
(a file of code you can import) is unit 09, and for now "import gives you extra tools
someone else wrote" is enough.

Then have them extend it. Some ideas.

- Limit the guesses to 7 and print a different message when they run out. That
  needs a `for` loop or an attempt counter check with `break`.
- Change the range to 1 to 1000 and see that the number of guesses needed barely
  changes. That is a nice moment about binary search, and it is optional.
- Print the secret number at the end when they fail.
- Ask to play again at the end, which needs a loop around the whole thing.

---

## Teaching notes for this unit

**Trace on paper, every time, for the first hour.** Do not let a loop go past untraced.
A student who can read a loop and be right is guessing. A student who can write out the
variable values on each pass is reasoning, and that is the thing that generalises.

**Teach `while` first, then `for`.** It is more work up front and it makes `for` look
like the convenience it is. Going straight to `for` leaves students unable to write a
loop whose end condition is not a number of passes.

**The infinite loop demo is not optional.** Let it run, let it fill the screen, and
teach Ctrl+C. Fear of the infinite loop stops people from experimenting, and
experimenting is how they learn.

**The accumulator pattern earns its own session.** If this unit takes three sessions
instead of two because they spent a long time on accumulators, that is the correct
outcome. Sum, count, and biggest-so-far are the three shapes that turn up inside almost
every program they will write for the next year.

**The off-by-one needs repetition, not explanation.** They will get it wrong in
exercises. When they do, do not explain it again, ask them "what does `range(1, 5)`
actually give you? Print it and see." Making them check is worth more than making them
listen.

**`break` and `continue` are lower priority.** Get through them if there is room, and do
not worry about it if they need prompting later. The only `break` usage that matters at
this stage is `while True`.

**Nested loops are awareness only.** Print the triangle, look at it, move on. Real
comfort with nesting comes later, with lists.

**Watch for the loop that reads input forever.** A student writing `while number != 0`
without re-reading the input inside the loop will create an infinite loop that hangs
waiting for input, which looks like the program has frozen. It is a common shape of
confusion and worth recognising instantly.

**Exercise 4.15, the square root shortcut.** Do not lead with this. Have them write the
slow version, confirm it works, then ask "How much of that work was wasted?" and let
them think.

**Preview of next unit.** They can repeat. Next session they meet lists, which are the
thing most programs are actually made of, and loops get much more useful immediately.
