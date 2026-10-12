---
title: Unit 08 exercises
sidebar:
  label: Exercises
---
Remember: everything read from a file or from a user is text, until you convert it. And
always check the file is where you think it is before blaming the code.

---

## Before you start

Here is what the exercises use, in small pieces.

`open` gives you a file to work with. `with` closes the file for you when the indented
block ends. The second part of `open` is the mode: `"r"` reads (the default), `"w"`
writes and empties the file first, and `"a"` adds to the end.

```python
with open("sample.txt") as file:
    for line in file:
        print(line.strip())
```

Each line from a file ends with a newline (the invisible character that starts a new
line). `strip()` removes spaces and newlines from both ends. Give it characters and it
removes those instead: `"line.".strip(".,!?")` gives `"line"`. `file.read()` gives the
whole file as one text, `file.readline()` gives just one line, and `text.splitlines()`
cuts a text into a list of lines.

`enumerate` counts as it goes. `enumerate(items, start=1)` gives pairs of a number and an
item, so you can number a list from 1.

```python
for number, item in enumerate(["tea", "milk"], start=1):
    print(f"{number}. {item}")
```

`try` and `except` handle an error. You can add `else`, which runs only when nothing went
wrong in the `try` block.

```python
try:
    number = int(text)
except ValueError:
    print("not a number")
else:
    print("that worked")
```

To catch two kinds of error with one `except`, put them in brackets:
`except (FileNotFoundError, ValueError):`.

---

## Warm-ups

### 8.1 Predict the output

```python
with open("test.txt", "w") as file:
    file.write("one\n")

with open("test.txt", "w") as file:
    file.write("two\n")
```

What is in the file at the end?

### 8.2 Predict the output

```python
with open("test.txt", "w") as file:
    file.write("one\n")

with open("test.txt", "a") as file:
    file.write("two\n")
```

What is in the file now, and how is this different from 8.1?

### 8.3 What error?

Say which error each of these gives.

```python
with open("does_not_exist.txt") as file:
    print(file.read())
```

```python
with open("test.txt", "w") as file:
    file.write(42)
```

```python
text = "hello"
number = int(text)
```

```python
number = int("0")
print(100 / number)
```

### 8.4 Predict the output

```python
try:
    number = int("hello")
    print("A")
except ValueError:
    print("B")
print("C")
```

### 8.5 Predict the output

```python
try:
    number = int("5")
    print("A")
except ValueError:
    print("B")
print("C")
```

---

## Core

### 8.6 Count things in a file

Write a program that reports how many lines, how many words, and how many characters
[`sample.txt`](/code/08-files-and-errors/sample.txt) has. Check the answers by hand.

Save `sample.txt` in the same folder as your script, so your program can find it. If you
get a `FileNotFoundError`, the file is in a different folder than your script. Move it.

Be careful with the line count. Different ways of reading a file can give different
line counts. Write a comment in your code saying which way you counted lines and why.

### 8.7 Write a file

Ask the user for five favourite things. Write them to a file, one per line. Then read
the file back and print it numbered.

```
1. coffee
2. rain
...
```

If you run it twice, what happens? Decide what you think should happen, then make it do
that.

### 8.8 A log file

Write a program that appends a line to `log.txt` every time it runs, with the current
time and something the user typed.

For the time, you will need this.

```python
import datetime
now = datetime.datetime.now()
```

Then `str(now)` gives you a readable date and time. This is a preview of unit 09.

Run it a few times and then open the file and look at what accumulated.

### 8.9 Safe number input

Write a function `get_number(prompt)` that keeps asking until the user gives a whole
number. This is a validation loop (a loop that asks again until the answer is valid).
Loop forever, try `int(text)` and `return` it, and when you get a `ValueError`, print a
message and go round again.

Then use it to ask for two numbers and print their sum.

### 8.10 Safe division

Ask for two numbers and print the first divided by the second. If the second is zero,
print a message instead of crashing. Use `try` and `except`.

Then do the same thing without `try`, by checking the value first.

Then answer this. Which version do you prefer, and why?

### 8.11 Save and load a dictionary

Ask the user for five names and scores, store them in a dictionary (a collection you
look things up in by name), and save it with `json.dump`. If the user types the same
name twice, the second score replaces the first, so you may end up with fewer than five
entries. That is fine.

Then write a second program that loads the file and prints the names and scores sorted
by score, highest first.

Run the second program in a fresh terminal to prove it does not depend on the first one
still running.

### 8.12 Biggest number in a file

Write a file with several numbers in it, one per line. Write a program that reads the
file and prints the biggest and smallest.

Remember that everything from a file is text, so you need `int`.

### 8.13 Word count from a file

Read a file and count how many times each word appears, using the dictionary counting
pattern from unit 07. Print the ten most common words.

Ignore capital letters, so `The` and `the` count as the same word, and remove `.,!?`
from both ends of each word (`word.strip(".,!?")` does this). Words with the same count
can come out in any order.

Test it on [`sample.txt`](/code/08-files-and-errors/sample.txt).

### 8.14 Filter a file

Read a file of numbers, one per line, and write a new file containing only the even
ones.

Make sure you do not wipe the input file by accident. This is a real way to lose data,
so check which filename is in the `"w"` line (the one that wipes the file) before you
run it.

---

## Stretch

### 8.15 To-do list that remembers

Write a to-do list program that remembers its items between runs.

- Show the items numbered from 1, or `(nothing to do)` if there are none.
- Show a menu with Add, Remove and Quit, and repeat until the user quits.
- Write a function `load_todos()` that reads `todos.json` and gives back the list. If
  the file does not exist, it gives back an empty list.
- Write a function `save_todos(todos)` and call it after every change.

Then add marking items as done. The simplest way is to store each item as a dictionary
rather than a string.

```python
[{"text": "buy milk", "done": False}]
```

When you change the shape of the data like this, delete your old `todos.json` first.
The old file holds plain strings, and the new code cannot read them.

### 8.16 Grade book on disk

Ask for student names and scores, store them in a dictionary, and save to JSON.

Then add a second run mode. If the file already exists when the program starts, load it
and let the user add more students rather than starting empty. A name typed twice
replaces the earlier score.

Like 8.15, this program loads what was saved earlier, which is what makes it feel like
real software.

### 8.17 A small CSV reader

A CSV file is comma separated values, one record per line.

```
name,score,subject
Ada,88,maths
Grace,95,english
```

The first line is the header, which names the columns. Write a program that reads this
and prints each record as a dictionary.

```python
{"name": "Ada", "score": "88", "subject": "maths"}
```

The trick is to read the first line separately to get the column names, then use those
names for every line after it. `file.readline()` reads just one line, and a loop over
`file` after that carries on from the second line.

Then think about this. Should `score` be converted to a number? What happens if one row
has a missing column?

### 8.18 A calculator that does not crash

Ask for an expression in the form `number operator number`, like `7 * 3`. Support `+`,
`-`, `*` and `/`.

Handle all of these without crashing.

- Not a number
- An operator that does not exist
- Division by zero
- Badly written input like `7 *` or just `hello`

Use `try` and `except` around the part that can fail, and catch (handle an error so the
program does not stop) the specific errors you expect. Then answer this. What is the
danger of wrapping too much in one `try`?

### 8.19 File statistics

Write a program that asks the user for a filename and reports the number of lines, words,
characters, the longest word, and the most common word.

Handle the file not existing, and handle the file being empty, both without crashing. An
empty file is the case people forget, and it breaks the longest-word and
most-common-word logic.

---

## Check yourself

Try to do these without notes.

- Open and read a file, line by line, with `with`.
- Write to a file, and explain the difference between `"w"` and `"a"`.
- Explain why reading a line gives you an extra newline.
- Write a `try` and `except` that handles a bad number.
- Save a dictionary with `json` and load it back.
