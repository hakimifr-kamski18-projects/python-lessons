---
title: Unit 05 solutions
sidebar:
  label: Solutions
---
## Warm-ups

### 5.1 Predict the output

With `text = "12"` it prints this.

```
A
13
C
```

`int("12")` works, so every line in the `try` block runs. The `except` block is skipped,
because nothing went wrong. Then the program carries on to `print("C")`.

With `text = "twelve"` it prints this.

```
B
C
```

`int("twelve")` raises (starts an error) a `ValueError` on the first line of the `try`.
The rest of the `try` block is skipped at once, so neither `A` nor the number is printed.
Python jumps to the `except` block, which prints `B`, and then carries on after it as
normal, so `C` still prints.

If you wrote `A` for the second run, you were imagining that Python runs the `try` lines
until one fails and keeps what came before. That part is right. But `print("A")` comes
after the failing line, not before it, so it never runs.

### 5.2 Which error?

| Line | Result |
| --- | --- |
| `int("3.5")` | `ValueError: invalid literal for int() with base 10: '3.5'` |
| `float("3.5")` | no error, it gives `3.5` |
| `int(" 8 ")` | no error, it gives `8` |
| `10 / 0` | `ZeroDivisionError: division by zero` |
| `"Score: " + 10` | `TypeError: can only concatenate str (not "int") to str` |
| `"cat"[3]` | `IndexError: string index out of range` |
| `int("")` | `ValueError: invalid literal for int() with base 10: ''` |
| `prnt("hello")` | `NameError: name 'prnt' is not defined. Did you mean: 'print'?` |
| `int("-5")` | no error, it gives `-5` |

The surprising ones are usually these.

`int("3.5")` fails. `int()` does not round and does not drop the decimal part of a
string. It wants a whole number written as text, and `3.5` is not one. Use `float()` for
decimals.

`int(" 8 ")` works. `int()` ignores spaces at the start and the end, so you do not even
need `.strip()` before it.

`int("")` fails. The two quotes at the end of the message with nothing between them are
the empty text. This is what you get when the user presses Enter without typing anything.

`int("-5")` works. A minus sign in front is part of a whole number. Remember this one for
exercise 5.18.

The `TypeError` message says "concatenate", which is Python's word for glue together. You
cannot glue a number onto text with `+`. Use `str(10)` or an f-string.

### 5.3 Two kinds of trouble

```
3
cannot divide by zero
not a number
4
done
```

Trace it one word at a time.

```
text is "4"   -> int gives 4  -> 12 // 4 is 3    -> print 3
text is "0"   -> int gives 0  -> 12 // 0 fails   -> ZeroDivisionError block
text is "abc" -> int fails                       -> ValueError block
text is "3"   -> int gives 3  -> 12 // 3 is 4    -> print 4
loop ends -> print done
```

Each pass has its own `try`, so a failure in one pass does not stop the loop. The next
word gets a fresh start. Python checks the `except` blocks from top to bottom and runs the
first one whose name matches. Only one of them runs in each pass.

### 5.4 The except that never runs

Typing `abc` gives this.

```
Number: abc
Traceback (most recent call last):
  File "/home/ada/python/half.py", line 4, in <module>
    number = int(text)
ValueError: invalid literal for int() with base 10: 'abc'
```

The last line says `ValueError`, but the program has `except TypeError:`. An `except`
only catches (handles an error with `except`, so the program does not stop) the error it
names. A `ValueError` is not a `TypeError`, so it goes straight past and stops the
program, just as if there were no `try` at all.

The fix is to name the right error.

```python
text = input("Number: ")

try:
    number = int(text)
    print(f"Half of that is {number / 2}")
except ValueError:
    print("Please type a number")
```

When you are not sure which error to name, do what this exercise did. Run the program
without the `try` first, type the bad answer, and read the name off the last line of the
traceback (the text Python prints when a program stops with an error). That is the name
to write after `except`.

### 5.5 The hidden typo

The real problem is `catz` on the `print` line. It should be `cats`. A misspelled name is
a `NameError`, and the bare `except:` (an `except:` with no type after it) caught it and
printed a message about the user's answer. The answer was fine all along.

Change the `except` to name the error you expect.

```python
text = input("How many cats? ")

try:
    cats = int(text)
    print(f"That is {catz * 4} legs")
except ValueError:
    print("That was not a whole number")
```

Now typing `3` gives this.

```
How many cats? 3
Traceback (most recent call last):
  File "/home/ada/python/cats.py", line 5, in <module>
    print(f"That is {catz * 4} legs")
                     ^^^^
NameError: name 'catz' is not defined. Did you mean: 'cats'?
```

The `except ValueError` does not match a `NameError`, so the error is not hidden. The
traceback gives the line number, points at `catz`, and even suggests the right name. Fix
the typo, and the program works.

This is the whole reason to name the error. `except ValueError:` says that you expect
the user might type something that is not a number. It does not say that you expect your
own code to have mistakes in it. Mistakes in your code should stop the program loudly, so
you can find them.

### 5.6 Trace the validation loop

`Try again` prints three times, and the last line is `Got 7 after 4 attempts`.

```
pass 1: text is "ten"   -> int fails  -> print Try again
pass 2: text is ""      -> int fails  -> print Try again
pass 3: text is "4.0"   -> int fails  -> print Try again
pass 4: text is " 7 "   -> int gives 7 -> break
```

The full run looks like this.

```
Number: ten
Try again
Number: 
Try again
Number: 4.0
Try again
Number:  7 
Got 7 after 4 attempts
```

`attempts += 1` is above the `try`, so it counts every answer, bad ones too. That is why
the count is 4 and not 1. If you wanted to count only good answers, the line would have
to move.

`"4.0"` fails because `int()` wants a whole number written without a decimal point, even
when the decimal part is zero. `" 7 "` works because `int()` ignores the spaces.

### 5.7 Two broken loops

The first one asks only once, because the `input()` line is above the loop. If that one
answer is good, it works. If it is bad, the loop checks the same bad text again and again,
and prints `Not a whole number` forever, very fast. It never asks again, because the
asking happens before the loop. The fix is to move `input()` inside the loop, so every
pass asks a new question.

```python
while True:
    text = input("Number: ")
    try:
        number = int(text)
        break
    except ValueError:
        print("Not a whole number")
```

The second one has no `break`. Bad answers print the message, which is right. But a good
answer does nothing special, and the loop goes round and asks again. There is no way out,
so the program keeps asking forever. The fix is to add `break` after the line that can
fail, which gives the same program as above.

These are the two most common ways to get a validation loop (a loop that asks again
until the answer is valid) wrong. When a loop like this misbehaves, ask yourself two
questions. Where does it ask? Where does it get out?

---

## Core

### 5.8 A safe whole number

```python
while True:
    text = input("How many minutes did you exercise today? ")
    try:
        minutes = int(text)
        break
    except ValueError:
        print("Please type a whole number, like 45.")

hours = minutes // 60
left = minutes % 60

print(f"That is {hours} hours and {left} minutes.")
```

```
How many minutes did you exercise today? an hour
Please type a whole number, like 45.
How many minutes did you exercise today? 
Please type a whole number, like 45.
How many minutes did you exercise today? 135
That is 2 hours and 15 minutes.
```

This is the validation loop exactly as shown in the "Before you start" section, and it is
worth knowing by heart. Everything after the loop can trust that `minutes` is a whole
number, because the only way out of the loop is the `break`, and the `break` only runs
after `int()` worked.

The working out happens after the loop, not inside the `try`. It cannot fail, so it does
not belong there. Keeping the `try` small makes it clear which line you expect to fail.

`//` is whole number division, so `135 // 60` is 2. `%` gives what is left over, so
`135 % 60` is 15.

If you try `-5`, it is accepted, and you get `That is -1 hours and 55 minutes.` That is
what `//` and `%` really do with negative numbers, but it is not a sensible answer.
Exercise 5.10 shows how to refuse values like this with `raise`.

### 5.9 Sharing sweets

```python
while True:
    text = input("How many sweets? ")
    try:
        sweets = int(text)
        break
    except ValueError:
        print("Please type a whole number.")

while True:
    text = input("How many people? ")
    try:
        people = int(text)
        break
    except ValueError:
        print("Please type a whole number.")

try:
    each = sweets // people
    left = sweets % people
    print(f"Each person gets {each} sweets, and {left} is left over.")
except ZeroDivisionError:
    print(f"Nobody to share with, so you keep all {sweets} sweets.")
```

```
How many sweets? lots
Please type a whole number.
How many sweets? 25
How many people? 4
Each person gets 6 sweets, and 1 is left over.
```

```
How many sweets? 25
How many people? 0
Nobody to share with, so you keep all 25 sweets.
```

There are three `try` blocks, and each one expects a different problem. The two loops
expect a `ValueError` from `int()`. The last one expects a `ZeroDivisionError` from `//`.
Each `except` names only the error that can really happen in its own `try`.

The two loops look almost the same, and typing the same shape twice is a little boring. In
unit 07 you will learn to write it once and use it as often as you like.

There is another way to handle zero. You could refuse it inside the second loop, the way
exercise 5.10 refuses negative ages, and then the division could never fail. Both are
fine. Unit 09 comes back to this choice in exercise 9.10.

Negative numbers are not refused here, and `25 // -4` is `-7`, which makes no sense for
sweets. Refusing them is a good thing to add once you have done 5.10.

### 5.10 Age checker

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

print(f"In 10 years you will be {age + 10}.")
```

```
How old are you? abc
Not accepted: invalid literal for int() with base 10: 'abc'
How old are you? -3
Not accepted: age cannot be negative
How old are you? 200
Not accepted: nobody has lived that long
How old are you? 34
In 10 years you will be 44.
```

`int()` checks that the answer is a whole number, but it has no idea what an age is.
`-3` and `200` are perfectly good whole numbers. The two `if` lines add the checks that
only your program knows about, and `raise` turns a bad value into a `ValueError`, exactly
like the one `int()` gives for `abc`.

`raise` works like a failing line. The rest of the `try` is skipped, which skips the
`break`, and Python jumps to `except`. That is why one `except` can handle all three
problems.

`as error` puts the error in a variable, and `print(error)` shows its message. For `-3`
and `200` the message is yours. For `abc` it is Python's, which is written for
programmers rather than for normal users. If you prefer a friendly message for every case,
leave out `as error` and print one fixed message, such as `Please type a whole number
from 0 to 130.` Both are fine.

`ValueError` is the right name to raise, because it means "the right type, but the wrong
content". An age of 200 is exactly that.

### 5.11 A menu that does not crash

```python
import random

while True:
    print("-----")
    print("1. Say hello")
    print("2. Roll a dice")
    print("3. Count down from 5")
    print("4. Quit")

    try:
        choice = int(input("Your choice: "))
        if choice < 1 or choice > 4:
            raise ValueError("that is not on the menu")
    except ValueError:
        print("Please choose 1, 2, 3 or 4.")
        continue

    if choice == 1:
        print("Hello!")
    elif choice == 2:
        print(f"You rolled a {random.randint(1, 6)}")
    elif choice == 3:
        for number in range(5, 0, -1):
            print(number)
    else:
        print("Goodbye")
        break
```

A short run.

```
-----
1. Say hello
2. Roll a dice
3. Count down from 5
4. Quit
Your choice: abc
Please choose 1, 2, 3 or 4.
-----
1. Say hello
2. Roll a dice
3. Count down from 5
4. Quit
Your choice: 7
Please choose 1, 2, 3 or 4.
-----
1. Say hello
2. Roll a dice
3. Count down from 5
4. Quit
Your choice: 3
5
4
3
2
1
-----
1. Say hello
2. Roll a dice
3. Count down from 5
4. Quit
Your choice: 4
Goodbye
```

Here the `try` sits inside a loop that has its own job, which is to show the menu again
and again. So a bad answer uses `continue` instead of `break`. It skips the rest of the
pass, and the next pass shows the menu again. Only choice 4 leaves the loop.

`abc` and an empty answer fail inside `int()`. `7` and `0` get past `int()`, and the
`raise` refuses them. Both land in the same `except`, which is why one message covers all
of them.

After the `try`, `choice` is always 1, 2, 3 or 4. That is why the last branch can be a
plain `else`. Nothing else can reach it.

There is another way that needs no `try`. Keep the answer as text and check it with
`if text in ["1", "2", "3", "4"]:`. For a short menu, that is just as good. The `try`
version is worth knowing because it works the same way for a menu of 50 choices.

### 5.12 Guess the number, properly

```python
import random

secret = random.randint(1, 100)
guesses = 0

while True:
    text = input("Guess a number from 1 to 100: ")

    try:
        guess = int(text)
        if guess < 1 or guess > 100:
            raise ValueError("the guess is outside 1 to 100")
    except ValueError:
        print("Please type a whole number from 1 to 100.")
        continue

    guesses += 1

    if guess < secret:
        print("Too low")
    elif guess > secret:
        print("Too high")
    else:
        print(f"Correct! You took {guesses} guesses.")
        break
```

One run, where the secret was 18.

```
Guess a number from 1 to 100: fifty
Please type a whole number from 1 to 100.
Guess a number from 1 to 100: 50
Too high
Guess a number from 1 to 100: -5
Please type a whole number from 1 to 100.
Guess a number from 1 to 100: 25
Too high
Guess a number from 1 to 100: 12
Too low
Guess a number from 1 to 100: 18
Correct! You took 4 guesses.
```

The bad answers do not count, because the `continue` in the `except` block skips the
rest of the pass, and `guesses += 1` is in the part that gets skipped. If you put
`guesses += 1` above the `try`, every bad answer would count as a guess. Try it and see.

Compare this with the `.isdigit()` version from 4.13. That one said `-5` was "not a
number", which was not true. Here `int()` accepts `-5`, because it is a whole number, and
your own `raise` refuses it because it is outside the game. That is a more honest program.

If you want two different messages, one for "not a whole number" and one for "outside 1
to 100", one `except` cannot tell them apart without `as error`. The simplest way is to
take the range check out of the `try` and give it its own `if` and `continue`.

```python
import random

secret = random.randint(1, 100)
guesses = 0

while True:
    text = input("Guess a number from 1 to 100: ")

    try:
        guess = int(text)
    except ValueError:
        print("That is not a whole number.")
        continue

    if guess < 1 or guess > 100:
        print("Please guess from 1 to 100.")
        continue

    guesses += 1

    if guess < secret:
        print("Too low")
    elif guess > secret:
        print("Too high")
    else:
        print(f"Correct! You took {guesses} guesses.")
        break
```

Both versions are correct. The first is shorter, and the second gives more helpful
messages.

### 5.13 Add up, skip the bad ones

```python
total = 0
added = 0
skipped = 0

while True:
    text = input("Number, or done to finish: ")

    if text.strip().lower() == "done":
        break

    try:
        number = float(text)
    except ValueError:
        print(f"Skipped {repr(text)}, it is not a number.")
        skipped += 1
        continue

    total += number
    added += 1

print(f"Total: {total}")
print(f"Numbers added: {added}")
print(f"Entries skipped: {skipped}")
```

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

There are three accumulators (a variable you add to on every pass) here, and each one is
changed in a different place. `skipped` grows in the `except` block. `total` and `added`
grow after the `try`, in the part that a bad answer skips with `continue`.

The check for `done` comes before `float()`. If it came after, `float("done")` would fail,
and `done` would be counted as a skipped entry instead of ending the loop. The order of
the checks matters, just as it did for FizzBuzz in unit 04.

`.strip().lower()` means that `Done` and ` done ` also end the loop.

`repr(text)` shows the text with quotes around it. Without it, the empty answer would print
as `Skipped , it is not a number.`, which is hard to read.

### 5.14 Temperature converter

```python
while True:
    scale = input("Convert from C or F? ").strip().upper()
    if scale in ["C", "F"]:
        break
    print("Please type C or F.")

if scale == "C":
    name = "Celsius"
    lowest = -273.15
else:
    name = "Fahrenheit"
    lowest = -459.67

while True:
    text = input(f"Temperature in {name}: ")
    try:
        temperature = float(text)
        if temperature < lowest:
            raise ValueError("that is colder than absolute zero")
        break
    except ValueError as error:
        print(f"Not accepted: {error}")

if scale == "C":
    result = temperature * 9 / 5 + 32
    print(f"{temperature} C is {result:.1f} F")
else:
    result = (temperature - 32) * 5 / 9
    print(f"{temperature} F is {result:.1f} C")
```

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

```
Convert from C or F? F
Temperature in Fahrenheit: 98.6
98.6 F is 37.0 C
```

The first loop has no `try`, because nothing in it can fail. `.upper()` never raises an
error, and the `if` simply checks the answer. Not every validation loop needs `try`. You
need it when the check is "can this be turned into a number", because the simplest way to
find out is to let `float()` try.

The second loop is the age checker shape from 5.10, with `float()` instead of `int()`.
Because the lowest value depends on the scale, it is chosen before the loop and kept in
`lowest`, so the loop itself is the same for both scales.

`float()` accepts `-300` and `21.5`, and it accepts ` 21.5 ` with spaces too. It does not
accept `21,5` with a comma. Python always writes decimals with a dot, wherever you live.

### 5.15 Three tries and then give up

```python
booked = False

for attempt in range(3):
    text = input("How many tickets (1 to 10)? ")
    try:
        tickets = int(text)
        if tickets < 1 or tickets > 10:
            raise ValueError("tickets must be from 1 to 10")
        booked = True
        break
    except ValueError:
        print("Please type a whole number from 1 to 10.")

if booked:
    print(f"Booked {tickets} tickets.")
else:
    print("Too many bad answers. Goodbye.")
```

```
How many tickets (1 to 10)? lots
Please type a whole number from 1 to 10.
How many tickets (1 to 10)? 4
Booked 4 tickets.
```

```
How many tickets (1 to 10)? lots
Please type a whole number from 1 to 10.
How many tickets (1 to 10)? 12
Please type a whole number from 1 to 10.
How many tickets (1 to 10)? 0
Please type a whole number from 1 to 10.
Too many bad answers. Goodbye.
```

This is the validation loop with a `for` instead of `while True`, so it can only go round
three times. There are two ways out of the loop. A good answer leaves early with `break`.
Three bad answers leave because the `range(3)` has run out.

After the loop, the program has to know which of the two happened, and that is the job of
`booked`. It starts as `False`, and only the line before `break` sets it to `True`. That
line is reached only when `int()` worked and the `raise` did not happen.

You cannot just check `tickets` after the loop. If the first answer was `12`, then
`tickets` is 12 even though it was refused. And if every answer was like `lots`, then
`tickets` was never given a value at all, and using it would be a `NameError`.

### 5.16 Read a time

```python
while True:
    text = input("Time (hh:mm): ").strip()
    try:
        if text.count(":") != 1:
            raise ValueError("use one colon, like 14:30")
        parts = text.split(":")
        hours = int(parts[0])
        minutes = int(parts[1])
        if len(parts[1]) != 2:
            raise ValueError("minutes need two digits, like 9:05")
        if hours < 0 or hours > 23:
            raise ValueError("hours must be from 0 to 23")
        if minutes < 0 or minutes > 59:
            raise ValueError("minutes must be from 0 to 59")
        break
    except ValueError as error:
        print(f"Not a valid time: {error}")

total = hours * 60 + minutes
print(f"That is {total} minutes after midnight.")
```

A run with all the test answers, ending with a good one.

```
Time (hh:mm): 1430
Not a valid time: use one colon, like 14:30
Time (hh:mm): 25:00
Not a valid time: hours must be from 0 to 23
Time (hh:mm): 12:60
Not a valid time: minutes must be from 0 to 59
Time (hh:mm): 12:5
Not a valid time: minutes need two digits, like 9:05
Time (hh:mm): ab:cd
Not a valid time: invalid literal for int() with base 10: 'ab'
Time (hh:mm): 14:30
That is 870 minutes after midnight.
```

And `9:05` gives `That is 545 minutes after midnight.`

The colon check has to come first. With no colon, `split(":")` gives back only one piece,
and `parts[1]` would be an `IndexError`, which the `except ValueError` does not catch. So
the program refuses that case before it can happen. This is a good example of choosing
the order of checks so that each one can trust the ones above it.

All the problems are `ValueError`s, the ones from `int()` and the ones you raised, so one
`except` handles them all, and `as error` shows which problem it was. For `ab:cd`, the
message comes from `int()`. If you want your own message there too, you can check
`parts[0].isdigit()` first, but then `-1:30` would get the "not a number" message
instead of the "hours" one. That is a choice, and either is fine.

`int()` accepts `"05"` and gives 5, so the minutes `05` work without any extra effort.

### 5.17 Add up a messy line

```python
data = "12,abc,7,,3"

total = 0
skipped = 0

for item in data.split(","):
    try:
        total += int(item)
    except ValueError:
        print(f"Skipped {repr(item)}")
        skipped += 1

print(f"Total: {total}")
print(f"Skipped: {skipped}")
```

```
Skipped 'abc'
Skipped ''
Total: 22
Skipped: 2
```

`data.split(",")` cuts the text at every comma, which gives five pieces: `'12'`, `'abc'`,
`'7'`, `''` and `'3'`. The empty one comes from the two commas next to each other, with
nothing between them. `repr()` is what makes it visible in the output.

`total += int(item)` is inside the `try`. If `int()` fails, the adding never happens, so a
bad item cannot spoil the total. There is no `continue` here, because nothing comes after
the `try` in the loop.

The version that asks the user only changes the first line.

```python
data = input("Numbers with commas between them: ")

total = 0
skipped = 0

for item in data.split(","):
    try:
        total += int(item)
    except ValueError:
        print(f"Skipped {repr(item)}")
        skipped += 1

print(f"Total: {total}")
print(f"Skipped: {skipped}")
```

```
Numbers with commas between them: 5, 6 ,x, 7
Skipped 'x'
Total: 18
Skipped: 1
```

The spaces are not a problem. The pieces are `'5'`, `' 6 '`, `'x'` and `' 7'`, and `int()`
ignores spaces at the start and the end, so `' 6 '` gives 6. Only `'x'` is skipped. With
`.isdigit()` instead of `try`, `' 6 '` and `' 7'` would have been skipped as well, which
is exactly the subject of the next exercise.

### 5.18 Check first, or try?

| Answer | `.isdigit()` version | `try` version |
| --- | --- | --- |
| `42` | Accepted 42 | Accepted 42 |
| ` 42 ` (spaces around it) | Refused | Accepted 42 |
| `-5` | Refused | Accepted -5 |
| `4.5` | Refused | Refused |
| nothing, just Enter | Refused | Refused |
| `007` | Accepted 7 | Accepted 7 |

They disagree on ` 42 ` and `-5`. `.isdigit()` says `True` only when every character is a
digit, and a space or a minus sign is not a digit. `int()` is more forgiving. It ignores
spaces at the start and the end, and it allows a minus sign in front. Adding `.strip()`
before `.isdigit()` fixes the spaces, but not the minus sign.

Here is a sample answer for the sentences.

The two versions disagree on spaces and on negative numbers, because `.isdigit()` is a
stricter test than `int()`. For an age, either is fine, because an age is never negative,
and refusing `-5` is what you want anyway. For a temperature that can be below zero, the
`try` version is the one to use, because `.isdigit()` would refuse every negative
temperature. There is no simple check for `float()`, because a decimal number can have a
minus sign, a dot and spaces, and no single string method says yes to all of those, so
the easiest way to know whether `float()` will work is to let it try.

There is one more reason to prefer `try`, and it is a strange one. Some characters count
as digits for `.isdigit()` that `int()` will not accept. The small raised two, `²`, is one
of them.

```python
print("²".isdigit())
```

This prints `True`, but `int("²")` is a `ValueError`. So the check-first version would
say yes and then crash. The `try` version asks `int()` itself, so the check and the
conversion can never disagree. That is why `try` is the usual way in Python. Checking
first is still fine when the check is simple and says exactly what you want.
