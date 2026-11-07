---
title: Unit 05 exercises
sidebar:
  label: Exercises
---
Every exercise in this unit is about what happens when something goes wrong. So for every
program you write, run it with bad answers on purpose. Type letters where a number should
go, type a decimal, type nothing and press Enter. A program that only works with good
answers is not finished.

---

## Before you start

You have seen this many times by now. A program asks for a number, you type `abc`, and it
stops.

```
How old are you? abc
Traceback (most recent call last):
  File "/home/ada/python/age.py", line 1, in <module>
    age = int(input("How old are you? "))
ValueError: invalid literal for int() with base 10: 'abc'
```

This text is a traceback (the text Python prints when a program stops with an error).
Read it from the bottom up. The last line says what went wrong. Above it is the line of
code, and above that the `File` line says where, with the line number. On your computer
the `File` line shows the full folder path of your file.

The last line has two parts. Before the colon is the name of the error, `ValueError`.
After the colon is a message about this case. An error like this one is called an
exception (Python's word for an error that happens while the program is running). When a
line cannot do its job, Python raises (starts an error) an exception, and if nothing
handles it, the program stops.

You have met these already.

- `ValueError`. The right type of value, but the wrong content, like `int("abc")`.
  Pressing Enter without typing gives `""`, and `int("")` is a `ValueError` too.
- `ZeroDivisionError`. Dividing by zero, like `10 / 0`.
- `TypeError`. The wrong type for the job, like `"Score: " + 10`.
- `NameError`. A name Python does not know, usually a typo.
- `IndexError`. A position a string does not have, like `"cat"[3]`.

A `SyntaxError` is different. It means the file is not valid Python, so Python refuses to
start it at all, and not even the first line runs. Nothing in this unit can catch a
`SyntaxError`. You have to fix the file.

### `try` and `except`

To catch (handle an error with `except`, so the program does not stop) an exception, put
the line that can fail inside `try`, and say what to do instead under `except`.

```python
text = input("Type a whole number: ")

try:
    number = int(text)
    print(f"Double that is {number * 2}")
except ValueError:
    print("That was not a whole number.")

print("The program carries on.")
```

Python runs the lines inside `try` one by one. If they all work, it skips the `except`
block. If one line fails, Python skips the rest of the `try` block at once and runs the
`except` block. After that, the program carries on from the first line after the whole
`try` and `except`, as normal. With `21` you see `Double that is 42`. With `abc` you see
`That was not a whole number.` In both cases the last line prints.

### Name the error you expect

`except ValueError:` catches only a `ValueError`. Any other error still stops the
program. That is good, because it means you only hide the problem you planned for.

You can write `except:` with no name, and it catches every error. Do not do this. It also
catches your own typos, so a misspelled variable name prints "That was not a whole
number" and you look for the bug in the wrong place. It even catches Ctrl and C, so you
cannot stop the program. Always name the error.

To handle two errors in two ways, write two `except` blocks. Python runs the first one
that matches, and only that one.

```python
try:
    people = int(input("How many people? "))
    print(f"Each person gets {100 // people} sweets")
except ValueError:
    print("That was not a whole number.")
except ZeroDivisionError:
    print("Nobody to share with.")
```

When one message fits both, put the names in round brackets, as in
`except (ValueError, ZeroDivisionError):`.

Keep the `try` small. Put in it only the line that can fail and the lines that need its
result.

### The validation loop

A validation loop (a loop that asks again until the answer is valid) joins `while True`
and `break` from unit 04 with `try`.

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

The `break` comes right after `int()`, inside the `try`. If `int()` fails, the `break` is
skipped, the message prints, and the loop asks again. Only a good answer reaches the
`break`. The `input()` line must be inside the loop, or the loop checks the same bad text
forever.

### Seeing the message, and refusing on purpose

`except ValueError as error:` puts the error in a variable called `error`, and
`print(error)` shows Python's message, such as `invalid literal for int() with base 10:
'abc'`.

`int()` accepts `-5` and `999`, because they are whole numbers, even though they are not
real ages. Your program can refuse them with `raise`.

```python
while True:
    try:
        age = int(input("How old are you? "))
        if age < 0:
            raise ValueError("age cannot be negative")
        break
    except ValueError as error:
        print(f"Not accepted: {error}")
```

`raise ValueError("...")` starts a `ValueError` with your message. It jumps to the
`except` just as a failing `int()` does, so one `except` handles both problems.

There are two more words you may meet. An `else:` block after the `except` runs only when
there was no error. A `finally:` block runs every time, error or not. You will rarely
need them.

---

## Warm-ups

### 5.1 Predict the output

Do not run it yet. Write down what this prints.

```python
text = "12"

try:
    number = int(text)
    print("A")
    print(number + 1)
except ValueError:
    print("B")

print("C")
```

Now change the first line to `text = "twelve"` and predict again. Then run both and
check.

### 5.2 Which error?

For each line, say which error it gives, or say "no error". Think of each line as a
program on its own. Then check your answers by running them one at a time.

```python
int("3.5")
float("3.5")
int(" 8 ")
10 / 0
"Score: " + 10
"cat"[3]
int("")
prnt("hello")
int("-5")
```

### 5.3 Two kinds of trouble

Predict the output, line by line. Remember that `split()` gives back the words, and the
`for` loop takes them one at a time.

```python
for text in "4 0 abc 3".split():
    try:
        print(12 // int(text))
    except ValueError:
        print("not a number")
    except ZeroDivisionError:
        print("cannot divide by zero")

print("done")
```

### 5.4 The except that never runs

This program is meant to print a friendly message when the user types something that is
not a number. Run it and type `abc`. It crashes anyway. Why? Fix it.

```python
text = input("Number: ")

try:
    number = int(text)
    print(f"Half of that is {number / 2}")
except TypeError:
    print("Please type a number")
```

### 5.5 The hidden typo

Run this and type `3`. That is a whole number, but the program says it is not. Find the
real problem. Then explain how naming the error in the `except` would have shown you the
problem straight away.

```python
text = input("How many cats? ")

try:
    cats = int(text)
    print(f"That is {catz * 4} legs")
except:
    print("That was not a whole number")
```

### 5.6 Trace the validation loop

Do not run it yet. The user types these four answers, in this order: `ten`, then nothing
(just Enter), then `4.0`, then ` 7 ` with a space on each side. How many times does `Try
again` print, and what is the last line?

```python
attempts = 0

while True:
    text = input("Number: ")
    attempts += 1
    try:
        number = int(text)
        break
    except ValueError:
        print("Try again")

print(f"Got {number} after {attempts} attempts")
```

### 5.7 Two broken loops

Both of these are meant to keep asking until the user types a whole number. Each one has a
different bug. Say what each one does wrong when you run it, then fix it. If one of them
runs forever, press Ctrl and C to stop it.

```python
text = input("Number: ")

while True:
    try:
        number = int(text)
        break
    except ValueError:
        print("Not a whole number")
```

```python
while True:
    text = input("Number: ")
    try:
        number = int(text)
    except ValueError:
        print("Not a whole number")
```

---

## Core

### 5.8 A safe whole number

Ask "How many minutes did you exercise today?" and keep asking until the answer is a whole
number. Then print it as hours and minutes, like this.

```
How many minutes did you exercise today? an hour
Please type a whole number, like 45.
How many minutes did you exercise today? 135
That is 2 hours and 15 minutes.
```

`//` and `%` from unit 01 do the hours and minutes. Do not worry about negative numbers
yet. Exercise 5.10 shows how to refuse them.

### 5.9 Sharing sweets

Ask how many sweets there are, and then how many people will share them. Each answer must
be a whole number, so give each question its own validation loop.

Then print how many sweets each person gets and how many are left over, using `//` and
`%`. If the number of people is 0, the division fails. Catch that with `try` and `except
ZeroDivisionError`, and print `Nobody to share with, so you keep all 25 sweets.` (with the
real number of sweets).

```
How many sweets? 25
How many people? 4
Each person gets 6 sweets, and 1 is left over.
```

Unit 09 comes back to division with exercise 9.10, where you compare `try` with checking
first.

### 5.10 Age checker

Ask for an age, and keep asking until it is acceptable. An acceptable age is a whole
number from 0 to 130.

- If the answer is not a whole number, `int()` raises the error for you.
- If it is below 0, raise `ValueError("age cannot be negative")` yourself.
- If it is above 130, raise `ValueError("nobody has lived that long")`.

Use one `except ValueError as error:` for all three cases, and print `Not accepted:`
followed by the message. When the age is acceptable, print how old the user will be in 10
years.

```
How old are you? -3
Not accepted: age cannot be negative
How old are you? 200
Not accepted: nobody has lived that long
How old are you? 34
In 10 years you will be 44.
```

### 5.11 A menu that does not crash

Show this menu and ask for a choice.

```
1. Say hello
2. Roll a dice
3. Count down from 5
4. Quit
```

Do what the user chose, then show the menu again. Keep going until they choose 4. Rolling
a dice means printing `random.randint(1, 6)`.

Anything that is not 1, 2, 3 or 4, such as `abc`, `7`, `0` or just Enter, should print
`Please choose 1, 2, 3 or 4.` and show the menu again. Use `int()` with `try`, and use
`raise` for whole numbers that are not on the menu.

### 5.12 Guess the number, properly

This is exercise 4.13 again, done the proper way. Here is the full description.

- The program picks a secret whole number from 1 to 100. Put `import random` at the
  top, and `random.randint(1, 100)` gives the number. Both 1 and 100 can come up.
- It asks the user for a guess, again and again.
- If the guess is too low, print `Too low`. If it is too high, print `Too high`.
- It counts the guesses.
- When the guess is right, print how many guesses it took, and stop.

These are the new rules for bad answers.

- If the answer is not a whole number, such as `abc`, `4.5` or nothing at all,
  print `That is not a whole number.` and ask again.
- If it is a whole number outside 1 to 100, such as `0`, `-5` or `250`, print
  `Please guess from 1 to 100.` and ask again.
- Neither of these counts as a guess.

Use `try` and `except` this time, not `.isdigit()`. Use `raise` for the numbers outside 1
to 100. To test it quickly, add `print(secret)` near the top while you work, and remove it
when you are done.

### 5.13 Add up, skip the bad ones

Ask for numbers one at a time, and add them up, until the user types `done`. Decimals are
allowed, so use `float()`. Anything that is not a number is skipped with a message, and
the program counts how many it skipped.

At the end, print the total, how many numbers were added, and how many entries were
skipped.

```
Number, or done to finish: 4
Number, or done to finish: 2.5
Number, or done to finish: four
Skipped 'four', it is not a number.
Number, or done to finish: 
Skipped '', it is not a number.
Number, or done to finish: 10
Number, or done to finish: done
Total: 16.5
Numbers added: 3
Entries skipped: 2
```

To show the empty answer as `''`, print `repr(text)` instead of `text`.

### 5.14 Temperature converter

Ask whether the user wants to convert from Celsius or from Fahrenheit. Accept `c` or `f`,
in small or capital letters, and keep asking until you get one of them.

Then ask for the temperature, which may have decimals, and keep asking until it is a
number. Then print the converted temperature to one decimal place.

- Celsius to Fahrenheit is `celsius * 9 / 5 + 32`.
- Fahrenheit to Celsius is `(fahrenheit - 32) * 5 / 9`.

Nothing can be colder than absolute zero, which is -273.15 in Celsius and -459.67 in
Fahrenheit. Use `raise` to refuse temperatures below that, with a message that says so.

```
Convert from C or F? k
Please type C or F.
Convert from C or F? c
Temperature in Celsius: twenty
Not accepted: could not convert string to float: 'twenty'
Temperature in Celsius: -300
Not accepted: that is colder than absolute zero
Temperature in Celsius: 21.5
21.5 C is 70.7 F
```

---

## Stretch

### 5.15 Three tries and then give up

Ask how many tickets the user wants, from 1 to 10. Allow at most three tries. If one of the
three is a good answer, print `Booked 4 tickets.` (with the real number). If all three are
bad, print `Too many bad answers. Goodbye.` and stop.

```
How many tickets (1 to 10)? lots
Please type a whole number from 1 to 10.
How many tickets (1 to 10)? 12
Please type a whole number from 1 to 10.
How many tickets (1 to 10)? 0
Please type a whole number from 1 to 10.
Too many bad answers. Goodbye.
```

A `for attempt in range(3):` loop gives you the three tries. You also need a way to know,
after the loop, whether a good answer arrived. A variable that starts as `False` and
becomes `True` is one way.

### 5.16 Read a time

Ask for a time written as hours and minutes, like `14:30`, and keep asking until it is a
real time. Then print how many minutes it is after midnight. `14:30` is 870 minutes after
midnight.

A real time has exactly one `:`, hours from 0 to 23, and minutes from 0 to 59 written with
two digits. So `9:05` is fine, but `9:5` is not. Raise a `ValueError` with a clear message
for each problem, catch them all with one `except ValueError as error:`, and print `Not a
valid time:` followed by the message.

Try at least these: `14:30`, `1430`, `25:00`, `12:60`, `12:5`, `ab:cd`, `9:05`.

`text.count(":")` counts the colons. `text.split(":")` cuts the text at the colon, and
`parts[0]` and `parts[1]` are the two pieces. `len()` gives the length of a piece.

### 5.17 Add up a messy line

Someone has typed a line of numbers with commas between them, but not very carefully.

```python
data = "12,abc,7,,3"
```

Go through the items you get from `data.split(",")`. Add up the ones that are whole
numbers, and skip the others. For each skipped item, print it with `repr()` so you can see
empty ones. At the end, print the total and how many items were skipped. For this line the
total is 22, and two items are skipped.

Then change the program to ask the user for the line instead. Try `5, 6 ,x, 7`. Are the
spaces a problem?

### 5.18 Check first, or try?

Here are two ways to read a whole number.

```python
text = input("Number: ")

if text.isdigit():
    print(f"Accepted {int(text)}")
else:
    print("Refused")
```

```python
text = input("Number: ")

try:
    print(f"Accepted {int(text)}")
except ValueError:
    print("Refused")
```

Copy this table and fill in what each version does with each answer, then run both to
check.

| Answer | `.isdigit()` version | `try` version |
| --- | --- | --- |
| `42` | | |
| ` 42 ` (spaces around it) | | |
| `-5` | | |
| `4.5` | | |
| nothing, just Enter | | |
| `007` | | |

Then write three or four sentences. Where do the two versions disagree? Which one would
you use for an age, and which for a temperature that can be below zero? Why is there no
`.isdigit()` style check that would work for `float()`?

---

## Check yourself

Try to do these without notes.

- Read a traceback and say the name of the error and the line it happened on.
- Explain why the rest of a `try` block is skipped when one line fails.
- Write a validation loop that keeps asking until it gets a whole number.
- Say why `except ValueError:` is better than `except:`.
- Use `raise ValueError("...")` to refuse a value that `int()` would accept.
- Say one reason to use `try` instead of `.isdigit()`.
