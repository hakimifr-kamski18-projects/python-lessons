---
title: Unit 05 — Exceptions
sidebar:
  hidden: true
pagefind: false
head:
  - tag: meta
    attrs:
      name: robots
      content: noindex
prev: false
next: false
---
**Files for this unit.** [`raise_demo.py`](/code/05-exceptions/raise_demo.py), [`try_except.py`](/code/05-exceptions/try_except.py), [`validation_loop.py`](/code/05-exceptions/validation_loop.py), [`what_went_wrong.py`](/code/05-exceptions/what_went_wrong.py)

These live in `public/code/05-exceptions/` in the repository, and the links above
open them as plain text. Every snippet the student needs is already inline in the
exercises, so the files are for the session itself, when you are both at the
keyboard.

**Goal for the session.** Their programs stop crashing when the user types something
silly. They can write a validation loop (a loop that asks again until the answer is
valid) without notes, they catch the one error they expect instead of every error, and
they can refuse a bad value on purpose with `raise`.

**Time.** One to two sessions. The ideas are small, but the validation loop has to be
typed several times before it sticks, and it is the pattern they will reuse in every unit
from here on.

**Prerequisites.** Unit 04. `while True` with `break`, `continue`, and the guessing game
from exercise 4.13.


---

## 0. Warm-up

Have them open their solution to exercise 4.13, the guessing game, or write the first
part again from memory. Ask them to run it and type `abc` as a guess. If they used
`.isdigit()`, it copes. Then ask them to type `-5`. Their program says it is not a
number, which is wrong, because it is a number. It is just a silly guess.

Now show the version without the check.

```python
number = int(input("Pick a number: "))
print(number * 2)
```

Have them type `abc` and look at what comes out.

```
Pick a number: abc
Traceback (most recent call last):
  File "/home/ada/python/pick.py", line 1, in <module>
    number = int(input("Pick a number: "))
ValueError: invalid literal for int() with base 10: 'abc'
```

Ask them to read it from the bottom up, out loud. The last line says what went wrong,
the code line above it shows the line, and the `File` line above that gives the line
number. They have been doing this since unit 01, so it should be quick. If it is not,
spend five minutes here, because the rest of the unit leans on it.

Then ask them, and wait for the answer. "What would you like the program to do
instead?" The answer you are hoping for is something like "say it is wrong and ask
again". That is what this unit teaches.

## 1. What an exception is

Open [`what_went_wrong.py`](/code/05-exceptions/what_went_wrong.py).

Start with the new word. An exception (Python's word for an error that happens while the
program is running) is what they have been seeing every time a program stopped with a
traceback (the text Python prints when a program stops with an error). Python raises
(starts an error) an exception when a line cannot do what it was asked to do. If nothing
handles it, the program stops and prints the traceback.

The last line of a traceback has two parts.

```
ValueError: invalid literal for int() with base 10: 'abc'
```

Before the colon is the name of the error, here `ValueError`. After the colon is the
message, which says more about this particular case. Today the name matters most,
because the name is what they will write in their code.

Go through the ones they have already met. The file has one commented-out line for each.
Have them uncomment one at a time, predict the name before running, then run and check.

| Line | Error | In plain words |
| --- | --- | --- |
| `int("abc")` | `ValueError` | right type, wrong content |
| `int("")` | `ValueError` | the user pressed Enter and typed nothing |
| `10 / 0` | `ZeroDivisionError` | dividing by zero |
| `"Score: " + 10` | `TypeError` | wrong type for this operation |
| `print(totle)` | `NameError` | a name Python does not know, usually a typo |
| `"cat"[3]` | `IndexError` | a position the string does not have |

The `int("")` one deserves a moment. Pressing Enter at an `input()` gives an empty
string, and empty strings are not numbers. It is the most common crash in beginner
programs, and the student usually did not even type anything, so it feels unfair.

Point out the first line of the file, `print("The file started running.")`. It shows up
above every one of these tracebacks. The lines before the error ran, and the program
stopped at the bad line.

### SyntaxError is different

The last commented-out line in the file is `if 5 > 3` with no colon. Have them uncomment
it and run.

```
  File "/home/ada/python/what_went_wrong.py", line 60
    if 5 > 3
            ^
SyntaxError: expected ':'
```

Ask them what is missing from the output this time. The answer is everything. Even the
first `print` did not run.

This is the difference you want them to understand. Python reads the whole file before
running any of it. A SyntaxError means the file is not valid Python, so it never starts.
Every other error today happens while the program runs, after some lines have already
worked. This matters for the rest of the unit, because `try` is a line of Python too, and
in a file with a SyntaxError it never runs. So `try` cannot catch (handle an error with
`except`, so the program does not stop) a SyntaxError. The only fix is to fix the file.

## 2. `try` and `except`

Open [`try_except.py`](/code/05-exceptions/try_except.py).

```python
text = input("Type a whole number: ")

try:
    number = int(text)
    print("The conversion worked.")
    print(f"Double that is {number * 2}")
except ValueError:
    print("That was not a whole number.")

print("The program carries on here either way.")
```

Read it out loud as a sentence. "Try these lines. If a `ValueError` happens, do this
instead."

Point out the shape. `try` and `except` both end with a colon, and the lines under them
are indented, exactly like `if` and `else`. They already know how to read that.

Have them run it twice, once with `21` and once with `abc`. Then trace both runs on
paper, writing down which lines ran.

```
Input 21
  number = int(text)          works, number is 21
  print("The conversion...")  runs
  print(f"Double ...")        runs, prints 42
  except ValueError:          skipped, nothing went wrong
  print("The program...")     runs

Input abc
  number = int(text)          ValueError
  print("The conversion...")  skipped
  print(f"Double ...")        skipped
  except ValueError:          matches, so its block runs
  print("The program...")     runs
```

Two things to say clearly, because both are surprising.

- When a line inside `try` fails, the rest of the `try` block is skipped. Python
  does not go back and does not try the next line. It jumps straight to `except`.
- After the `except` block, the program carries on as normal, from the first line
  after the whole `try` and `except`. The error is gone, as if it was never there.

Ask them, "Why did 'The conversion worked.' not appear the second time?" If they can
answer that, they have the flow.

## 3. Catch the one you expect

### Name the error

`except ValueError:` only catches a `ValueError`. Any other error passes straight
through and still crashes the program. Show it.

```python
text = input("Share 100 sweets between how many people? ")

try:
    people = int(text)
    print(f"Each person gets {100 // people}")
except ValueError:
    print("That was not a whole number.")
```

Have them type `0`. They get a `ZeroDivisionError` traceback, even though there is a
`try`. Ask them why. The `except` said `ValueError`, and this was a different error, so
the `except` did not match.

Say that this is a good thing. The `except` is a promise about which problem you expected
and planned for. Anything else is a problem you did not plan for, and you want to see it.

### Why a bare `except:` is a bad habit

You can write `except:` with no name, and it catches everything. Show why that hurts.

```python
text = input("How many cats? ")

try:
    cats = int(text)
    print(f"That is {catz * 4} legs")
except:
    print("That was not a whole number")
```

Have them type `3`, which is a perfectly good number.

```
How many cats? 3
That was not a whole number
```

There is a typo, `catz`, which is a `NameError`. The bare `except:` caught it and printed
a message about the user's input, which is a lie. The student will spend ten minutes
looking at the input, and the bug is in the code. Change it to `except ValueError:` and
run again with `3`. Now the real error shows up with its line number, and the fix takes
five seconds.

There is a second reason, and it is fun to show. A bare `except:` even catches the
`KeyboardInterrupt` that Ctrl and C sends to stop a program.

```python
while True:
    try:
        number = int(input("Number: "))
        break
    except:
        print("Try again")
```

Have them run it and press Ctrl and C. It prints "Try again" and asks again. Press it a
few more times. The program refuses to stop. Typing a real number gets them out. In some
editors the Stop button sends the same signal and is caught the same way, while in others
it kills the program outright, so the result depends on the editor.

The rule to give them is to always name the error they expect.

If they find `except Exception:` online, it is less bad than a bare `except:`, because it
lets Ctrl and C through, but it still hides typos. Do not teach it.

### Several kinds of error

Go back to the sweets. Both problems are expected now, so the program should name both,
and there are two ways to do it.

The first way is a separate `except` block for each error. Use it when each error needs
its own message.

```python
text = input("Share 100 sweets between how many people? ")

try:
    people = int(text)
    print(f"Each person gets {100 // people}")
except ValueError:
    print("That was not a whole number.")
except ZeroDivisionError:
    print("Nobody to share with.")
```

Python checks the `except` blocks from top to bottom and runs the first one that matches.
Only one of them runs. Have them run it with `abc`, `0` and `4`.

The second way is one block with both names in round brackets. Use it when the same
message fits both.

```python
text = input("Share 100 sweets between how many people? ")

try:
    people = int(text)
    print(f"Each person gets {100 // people}")
except (ValueError, ZeroDivisionError):
    print("Please type a whole number bigger than 0.")
```

The round brackets with a comma make a tuple. Do not explain tuples yet, because unit 08
does that. For today it is just "a group of error names".

### Keep the `try` small

Put only the line that can fail inside `try`, plus the lines that only make sense if it
worked. Ask them, "If the whole program was inside one `try`, and the `except` said 'not
a number', what would happen with a typo on line 30?" They have just seen the answer with
the cats.

## 4. The validation loop

Open [`validation_loop.py`](/code/05-exceptions/validation_loop.py). This is the most
important section of the unit. It combines `while True` and `break` from unit 04 with
today's `try`, and from now on it is how every program in the course asks for a number.

```python
while True:
    text = input("How old are you? ")
    try:
        age = int(text)
        break
    except ValueError:
        print("Please type a whole number, like 25.")

print(f"Next year you will be {age + 1}.")
```

Trace it with the inputs `abc`, then nothing (just Enter), then `30`.

```
pass 1: text is "abc" -> int fails -> break skipped -> print message
pass 2: text is ""    -> int fails -> break skipped -> print message
pass 3: text is "30"  -> int works, age is 30 -> break -> loop ends
after the loop: prints "Next year you will be 31."
```

Show them where the `break` is. It sits inside the `try`, on the line right after
`int()`, so it can only be reached if `int()` worked, because a failure skips the rest of
the `try`. That means the only way out of the loop is a good answer.

Have them type it from scratch, not copy it. Then have them change the question to "How
many pets do you have?" and type it again. Typing it twice is what makes them remember
it.

Then have them break it on purpose, in two ways.

- Move the `input()` line above `while True`. Type `abc`. The message prints forever,
  because the loop keeps checking the same bad text and never asks again. Stop it with
  Ctrl and C.
- Remove the `break`. Type `30`. It asks again, and again. A good answer no longer gets
  out.

### Fixing the guessing game properly

Now the guessing game from 4.13, with `try` instead of `.isdigit()`.

```python
import random

secret = random.randint(1, 100)
attempts = 0

while True:
    text = input("Guess a number between 1 and 100: ")

    try:
        guess = int(text)
    except ValueError:
        print("That is not a whole number, try again.")
        continue

    attempts += 1

    if guess < secret:
        print("Too low")
    elif guess > secret:
        print("Too high")
    else:
        print(f"Correct! You took {attempts} attempts")
        break
```

This is the same idea in a different shape, and it is worth pointing that out. Here the
`try` sits inside a loop that already exists for another reason. So a bad answer uses
`continue` to skip the rest of the pass, which means it does not count as an attempt. A
good answer carries on to the game code, and `break` is kept for the right guess.

So there are two shapes, and they will use both. When the program asks one question,
`break` goes inside the `try` and runs when the conversion worked. When the `try` sits
inside a bigger loop, `continue` goes inside the `except` and runs when the conversion
failed.

Have them type `-5` now. It is accepted as a guess and gives "Too low". That is fair,
since it is a whole number, but it is a silly guess. Section 7 deals with it.

Mention that this loop has to be typed out again every time they need a number. In unit
07 they will put it in a function and write it once. Do not show that today.

## 5. Looking at the message

Sometimes they want to see what Python said, especially while they are looking for a
bug. `as` gives the error a name.

```python
text = input("Type a decimal number: ")

try:
    value = float(text)
    print(f"Half of that is {value / 2}")
except ValueError as error:
    print("Python says:", error)
```

```
Type a decimal number: 1,5
Python says: could not convert string to float: '1,5'
```

`error` is just a variable name. Online they will see `e` and `err` too. Printing it shows
the message from the last line of the traceback, without the name in front.

The `1,5` example is worth using on purpose if your student comes from a country that
writes decimals with a comma. Python always wants a dot.

Also tell them that Python's messages are written for programmers, and that "invalid
literal for int() with base 10" means nothing to a normal user. For the user, write your
own message. For yourself, while fixing a bug, print Python's.

## 6. `else` and `finally`, lightly

Mention them, do not drill them.

```python
text = input("One more whole number: ")

try:
    number = int(text)
except ValueError:
    print("Not a whole number.")
else:
    print(f"else runs only when there was no error. You typed {number}.")
finally:
    print("finally runs every time, error or not.")
```

- `else` runs only when the `try` had no error. It is a place for the lines that
  need the value but cannot fail themselves, which keeps the `try` small.
- `finally` runs every time, whatever happened. It is for tidying up, and they will
  rarely need it. Unit 09 uses `with` for files, which does that tidying by itself.

The validation loop can be written with `else: break` instead of `break` inside `try`.
Both are correct. Do not make them choose.

## 7. Raising your own

Open [`raise_demo.py`](/code/05-exceptions/raise_demo.py).

`int()` refuses `abc` by itself. It does not refuse `-5` or `999` as an age, because those
are real whole numbers. They are just not real ages. The program has to refuse them
itself, and `raise` is how.

```python
raise ValueError("age cannot be negative")
```

Have them run that one line on its own.

```
Traceback (most recent call last):
  File "/home/ada/python/raise_demo.py", line 9, in <module>
    raise ValueError("age cannot be negative")
ValueError: age cannot be negative
```

It looks exactly like an error Python found by itself, with their message after the
colon. Ask them, "Who decided this was an error?" They did.

A program should refuse a value when it has the right type but makes no sense for the
job, such as a negative age, a 25th month or a tip of 400 percent. Carrying on with a
value like that gives a wrong answer later, far away from the real problem. Refusing at
once, with a clear message, is kinder to whoever reads the traceback.

`ValueError` is the right name here, because it means "right type, wrong content", which
is exactly the situation.

### Raise and catch in the same loop

The nice part is that the same `except` catches it.

```python
while True:
    text = input("How old are you? ")
    try:
        age = int(text)
        if age < 0:
            raise ValueError("age cannot be negative")
        if age > 130:
            raise ValueError("nobody has lived that long")
        break
    except ValueError as error:
        print(f"Not accepted: {error}")

print(f"In ten years you will be {age + 10}.")
```

Trace it with `abc`, `-5`, `999` and `30`.

```
How old are you? abc
Not accepted: invalid literal for int() with base 10: 'abc'
How old are you? -5
Not accepted: age cannot be negative
How old are you? 999
Not accepted: nobody has lived that long
How old are you? 30
In ten years you will be 40.
```

There are three different problems here, and one `except` handles all of them. The
`raise` jumps to `except` just as a failing `int()` does, so the `break` is skipped and
the loop goes round.

Ask them what they think of the first message. It is Python's, and it is ugly for a user.
If they want a friendly message for every case, the `except` can print a fixed message
and ignore `error`. Either is fine. Section 9 uses the fixed message.

Now have them go back to the guessing game and refuse guesses outside 1 to 100 with a
`raise`, without counting them. That is exercise 5.12, so let them try it alone if time
is short.

## 8. Check first, or try?

They already know one way to avoid the crash, `.isdigit()` from 4.13. Put the two side
by side.

```python
text = input("Number: ")

# checking first
if text.isdigit():
    number = int(text)
    print(f"Got {number}")
else:
    print("Not a number")

# trying
try:
    number = int(text)
    print(f"Got {number}")
except ValueError:
    print("Not a number")
```

Then run the last part of `raise_demo.py`, which tests both on several inputs.

```
'42'    isdigit: True   int works: True
' 42 '  isdigit: False  int works: True
'-5'    isdigit: False  int works: True
'4.5'   isdigit: False  int works: False
''      isdigit: False  int works: False
'abc'   isdigit: False  int works: False
```

They disagree on `" 42 "` and `"-5"`. `int()` allows spaces around the number and a minus
sign in front. `.isdigit()` wants every character to be a digit, so it says no to both.
Adding `.strip()` fixes the spaces but not the minus sign.

The message to give them is that both are fine. Checking first is clear when the check is
simple and says exactly what you want. `try` is the usual Python way, because it asks
`int()` itself, so the check and the conversion can never disagree. And for `float()`
there is no simple check at all. `"3.5"`, `"-0.5"` and `" 2 "` are all fine for
`float()`, and no single string method says yes to all of them.

## 9. Putting it together

Build a tip calculator together. It uses everything in the unit, and it never crashes.

```python
print("Tip calculator")

while True:
    text = input("Bill amount: ")
    try:
        bill = float(text)
        if bill <= 0:
            raise ValueError("the bill must be more than 0")
        break
    except ValueError:
        print("Please type an amount bigger than 0, like 42.50")

while True:
    text = input("Tip in percent (0 to 30): ")
    try:
        percent = int(text)
        if percent < 0 or percent > 30:
            raise ValueError("the tip must be from 0 to 30 percent")
        break
    except ValueError:
        print("Please type a whole number from 0 to 30")

while True:
    text = input("How many people are paying? ")
    try:
        people = int(text)
        if people < 1:
            raise ValueError("at least one person has to pay")
        break
    except ValueError:
        print("Please type a whole number, 1 or more")

tip = bill * percent / 100
total = bill + tip
each = total / people

print(f"Tip: {tip:.2f}")
print(f"Total: {total:.2f}")
print(f"Each person pays: {each:.2f}")
```

A run.

```
Tip calculator
Bill amount: forty
Please type an amount bigger than 0, like 42.50
Bill amount: 84.50
Tip in percent (0 to 30): 15%
Please type a whole number from 0 to 30
Tip in percent (0 to 30): 15
How many people are paying? 0
Please type a whole number, 1 or more
How many people are paying? 3
Tip: 12.68
Total: 97.17
Each person pays: 32.39
```

Things to point out as you build it.

- Build one loop, run it, then copy its shape for the next one. Do not type all
  three before running anything.
- The `people < 1` check means the division at the end can never be by zero. Refusing
  a bad value early is often better than catching the crash later.
- The text inside each `raise` is not printed, because the `except` prints its own
  message. It still tells a reader why the value is refused, and it is what the
  traceback would show if the `try` were ever removed.
- The three loops look almost the same. Ask them if that bothers them. It should bother
  them a little, and unit 07 fixes it.

Some ways to extend it, if there is time.

- Ask for the tip as a choice from a menu of 10, 15 or 20, and refuse anything else.
- Show what each person pays without the tip as well.
- Ask at the end whether to work out another bill, which needs a loop around
  everything.

---

## Teaching notes for this unit

**The whole program in one `try`.** This is the most common way to misuse `try`. A
student who has just learned `try` wraps everything in it, and then every bug in the
program prints "not a number". When you see it, do not fix it. Make a typo on purpose
somewhere in their `try` and ask them to run it and find the problem.

**Catching everything.** This comes from the same habit as the one above. It shows up as
a bare `except:`, or as a long list of error names they do not expect. Ask "Which line
can fail, and how?" and have them name only that.

**Forgetting `break`.** The loop works perfectly for bad answers and then refuses to
accept a good one. Students often think the program is broken in some deep way. Ask "What
line gets you out of this loop?"

**`input()` above the loop.** The message prints forever, very fast. It looks dramatic.
Ask "When does the program ask the question again?" The answer is never.

**`int()` on an empty string.** Pressing Enter gives `""`, which is a `ValueError` with
the message `invalid literal for int() with base 10: ''`. The two quotes at the end with
nothing between them confuse people. Point at them and say "that is the empty text you
typed".

**`int("3.5")` is a `ValueError`.** They often expect `int()` to round, or to drop the
decimal part. It refuses. `int(3.5)`, with a number and not a string, gives 3. Do not go
into that unless they ask.

**Using a variable that the `try` never made.** Outside a loop, this shape crashes.

```python
text = input("Number: ")
try:
    number = int(text)
except ValueError:
    print("Not a number")
print(number * 2)
```

With bad input, `number` was never given a value, so the last line is a `NameError`.
This is one of the reasons the validation loop is the right shape. After the loop,
`number` always has a value.

**A misspelled error name.** `except Valueerror:` is not a SyntaxError, so the file runs
fine with good input. With bad input, Python goes to check which error the `except`
names, cannot find `Valueerror`, and stops with a `NameError` on the `except` line. The
output shows two tracebacks joined by "During handling of the above exception, another
exception occurred". Tell them to read the bottom one first, as always. It points at the
`except` line and even suggests `ValueError`. It is confusing the first time, and worth
knowing about before it happens.

**Do not use `try` to avoid thinking.** The opposite mistake from catching everything is
wrapping lines that cannot fail in a `try` "just in case". Ask "What error could this line
raise?" If the answer is none, it does not need a `try`.

**What the student pages say.** The exercises page teaches the unit on its own, for
students who study alone. If your student has worked through it already, use this lesson
for the questions and the break-it-on-purpose demos rather than the explanations.

**Preview of next unit.** They can now keep a program alive when the user types
nonsense. Next they meet lists, which hold many values at once. Every list exercise that
asks the user for numbers can use the validation loop from today.
