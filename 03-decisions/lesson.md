# Unit 03 — Making decisions

**Goal for the session.** Their programs can choose between different paths based on the
data.

**Time.** One to two sessions. This unit introduces the largest single batch of new
syntax so far, so do not push the pace.

**Prerequisites.** Unit 02. Input, conversions, comparison of strings.

**Files used.** `code/comparisons.py`, `code/if_demo.py`, `code/logic.py`,
`code/grade.py`

---

## 0. Warm-up

Have them write, from scratch, a program that asks for a number and prints its double.
That is pure retrieval of unit 02, and it tells you whether the conversion idea has
stuck.

Then ask them what happens if the user types `hello` instead. They should be able to
predict the `ValueError` now. If they can, unit 02 is solid.

## 1. Questions with yes or no answers

Every decision in a program comes down to a question with a `True` or `False` answer.
Start with the comparisons that produce those answers.

Open `code/comparisons.py`.

```python
print(5 > 3)      # True
print(5 < 3)      # False
print(5 == 5)     # True
print(5 != 3)     # True
print(5 >= 5)     # True
print(5 <= 4)     # False
```

There are six operators (symbols that do something to values) and they are all pretty
readable. The one to stop on is `==`.

### `=` versus `==`

This is the most important thing in the unit and it costs a lot of debugging time if it
does not land.

```
=    one equals sign     put this value in that name
==   two equals signs    ask whether these two are equal
```

Have them read each one out loud as a sentence.

- `age = 25` is "age gets twenty five".
- `age == 25` is "is age equal to twenty five".

The out-loud reading is not a gimmick, it really fixes this faster than any explanation.
Do it several times over the next few sessions.

Then have them write this and run it.

```python
age = 25
print(age == 25)
print(age == 26)
```

And this, which is a `SyntaxError`.

```python
if age = 25:
```

The error message will complain about something. That is fine, it is the same mistake in
a different form.

### Comparing strings

Everything above also works on text.

```python
print("apple" == "apple")     # True
print("apple" == "Apple")     # False, case matters
print("apple" < "banana")     # True, alphabetical order
print("Zebra" < "apple")      # True, because capitals come first
```

The last one is worth a moment. Capital letters have lower character codes than
lowercase ones, so `Zebra` sorts before `apple`. This is not a bug, and it is why you
almost always compare `.lower()` versions of strings.

The comparison that matters in practice, and which they will write badly at least once.

```python
answer = input("Continue? ").strip().lower()
print(answer == "yes")      # now this works for Yes, YES, and " yes "
```

## 2. The `if` statement

Open `code/if_demo.py`.

```python
age = 20

if age >= 18:
    print("You can vote")
```

Three things about this shape, and they all matter.

1. The condition ends with a colon.
2. The body is indented.
3. The body runs only when the condition is `True`.

Have them remove the colon and run it. Then put it back and un-indent the print. Then
put it back and change `20` to `15` and run it again.

That sequence teaches the syntax better than describing it. Two of the three variations
produce errors that say exactly what to do.

### Indentation is the syntax

Python uses indentation to mean "this is inside that". Other languages use brackets.
Python uses the whitespace itself (spaces, tabs and blank lines).

The rule to give them. Four spaces, always, and never mix tabs and spaces. Let the
editor insert them with the Tab key.

The one thing to be careful about. Because indentation is invisible, a broken
indentation is hard to see. If they get an `IndentationError` and the line looks
correct, it is worth looking at whether the file has a mix of tabs and spaces, which is
usually caused by starting in one editor and finishing in another.

### `else`

```python
age = 15

if age >= 18:
    print("You can vote")
else:
    print("Too young to vote")
```

Exactly one of the two branches runs. Never both, never neither.

### `elif`

For more than two options.

```python
score = 75

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("Needs work")
```

Two things worth dwelling on, because both surprise students.

**Only the first matching branch runs.** Even if a later condition would also be true,
Python stops at the first one that matched. This is why the order matters.

**The conditions are checked top to bottom.** So this version is broken in a way that is
easy to miss.

```python
score = 95

if score >= 70:
    print("C or better")
elif score >= 90:
    print("A")
```

Ask them what this prints for 95. It prints `C or better`, and it never reaches the `A`
branch, because the first condition was already true. This is a real bug that people
write. Have them fix it by reordering, and ask them to state the rule. Specific and
strict conditions go first.

### `if` with nothing to do

Not needed yet, but they might meet it.

```python
if x > 5:
    pass
```

`pass` means "do nothing, on purpose". Worth mentioning so they recognise it, and worth
warning them not to use it to leave half-finished code lying around.

## 3. Combining conditions

Open `code/logic.py`.

```python
age = 20
has_ticket = True

if age >= 18 and has_ticket:
    print("You can enter")
```

`and` is true when both sides are true. `or` is true when at least one side is. `not`
flips a `True` to `False` and the other way round.

```python
print(True and True)      # True
print(True and False)     # False
print(True or False)      # True
print(False or False)     # False
print(not True)           # False
```

Have them fill in a truth table by hand, then check it in the shell. It takes three
minutes and removes all doubt.

### The mistake everyone makes

```python
answer = input("Continue? ")

if answer == "yes" or "y":
    print("Continuing")
```

This always prints, no matter what they type. Have them run it with `no` and watch it
print anyway. That is the "wow, what" moment.

The reason, in plain terms. `answer == "yes" or "y"` is read as `(answer == "yes") or
("y")`. The second part is just the string `"y"`, and a non-empty string counts as true,
so the whole thing is always true.

The fix.

```python
if answer == "yes" or answer == "y":
```

Which is repetitive, and there is a better way that uses `in`.

```python
if answer in ["yes", "y"]:
```

That is a list, which is unit 05, but this one use is so handy that it is worth
introducing early as a fixed pattern. "Is the answer one of these things."

### Chained comparisons

A Python nicety worth thirty seconds.

```python
age = 25

if 18 <= age < 65:
    print("Working age")

# the same as, but nicer to read than
if age >= 18 and age < 65:
    print("Working age")
```

### `in` and `not in`

```python
name = "Ada Lovelace"

if "Ada" in name:
    print("Found it")

if "xyz" not in name:
    print("Not there")
```

This reads like English, so they will like it. Note that it is case sensitive, so the
usual `.lower()` applies.

## 4. Truthiness

This is optional material. Cover it if they are moving well, or keep it for a
consolidation session.

Some values count as false even though they are not `False`.

```python
if 0:
    print("does not print")

if "":
    print("does not print either")

if []:
    print("nor this one")

if "hello":
    print("this one prints")
```

The rule. Empty things are false, and zero is false. Everything else is true.

This matters because it produces a common way of writing it.

```python
name = input("Name: ").strip()

if name:
    print(f"Hello {name}")
else:
    print("You did not enter a name")
```

That is cleaner than `if name != ""` and they will see it everywhere.

Do not teach the full truthiness table. `0`, `""`, empty collections and `None` covered
as "empty or zero means false" is enough. Be careful not to imply that `"False"` is
false, because the string `"False"` is a non-empty string, so it is true. That trap
catches people in other languages.

## 5. Nesting (put inside another one)

An `if` inside an `if`.

```python
age = 20
has_ticket = True

if age >= 18:
    if has_ticket:
        print("Welcome")
    else:
        print("Go buy a ticket")
else:
    print("Too young")
```

Show it, then show the flatter version.

```python
if age >= 18 and has_ticket:
    print("Welcome")
elif age >= 18:
    print("Go buy a ticket")
else:
    print("Too young")
```

Ask them which they find easier to read. There is no single right answer, but the
conversation is the point. Deep nesting gets very hard to follow, so a good default is
to use `and` when the conditions are about the same decision, and to nest when one
decision really depends on another.

## 6. Putting it together

Open `code/grade.py`. Build a small program with them.

```python
name = input("Name: ").strip().title()
score = int(input("Score out of 100: "))

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"{name} scored {score}, which is a {grade}")
```

Then extend it together. Some ideas, in increasing difficulty.

- Print "passed" if the grade is not F, using `or` or a list.
- Add a "merit" comment for a grade of A.
- Ask whether they attended every class, and only award a high grade if they did.
  That needs `and`.
- Print a different message for anyone scoring over 100, since that is probably a
  mistake.

The last one is worth doing, because it makes them think about where in the chain a
condition has to go, and why order matters.

---

## Teaching notes for this unit

**The colon and the indentation need to be practised on purpose.** Do not just show
correct code. Show code missing the colon, code with the wrong indentation, and code
with an extra space. Each produces a different error, and reading them is worth more
than any explanation.

**`=` versus `==` gets its own few minutes, out loud, with the sentence reading.** Every
student hits this and most hit it repeatedly. Say it again next session.

**The `or` trap is the best single lesson in this unit.** Students are convinced that
`if answer == "yes" or "y"` reads the way English does. Letting them run it with `no`
and seeing it pass anyway is more convincing than any explanation, and it teaches them
that code and English have different rules.

**Ordering of `elif` branches is a really tricky idea.** The `score >= 70` first example
above is worth actually doing rather than just reading. Reachability of branches is a
real skill and it takes a while.

**Truthiness is optional, and the empty string case is the important one.** If you skip
the section, at least mention `if name:` so the common way of writing it does not look
mysterious when they meet it in someone else's code.

**Do not teach the conditional expression yet.** `x if cond else y` on one line is a
real feature and it is really confusing to beginners. Unit 09 at the earliest.

**Exercise 3.15, the arithmetic version.** Do not teach this. The list and `.index`
are later material. If a student discovers
something like this themselves, celebrate it and move on. If you show it, show it as a
curiosity rather than a solution.

**Preview of next unit.** They can make decisions. Next session they make the computer
do the same thing many times, which is where programs stop feeling like fancy
calculators.
