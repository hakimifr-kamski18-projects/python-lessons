# Unit 08 exercises

Remember: everything read from a file or from a user is text, until you convert it. And
always check the file is where you think it is before blaming the code.

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
    print(file.read)
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

Make a file with several lines of text in it. Then write a program that reports how many
lines, how many words, and how many characters it has.

Test it against `code/sample.txt` and check the answers by hand.

Careful with the line count. If a file ends with a newline, the last line is complete,
and reading it with a loop counts it correctly. Reading different ways can give
different answers, so say which way you used and why.

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
now = datetime.datetime.now
```

Then `str(now)` gives you a readable timestamp. This is a preview of unit 09.

Run it a few times and then open the file and look at what accumulated.

### 8.9 Safe number input

Write a function `get_number(prompt)` that keeps asking until the user gives a whole
number. This is the validation loop (a loop that asks again until the answer is valid)
from the lesson, so do it from memory.

Then use it to ask for two numbers and print their sum.

### 8.10 Safe division

Ask for two numbers and print the first divided by the second. If the second is zero,
print a message instead of crashing. Use `try` and `except`.

Then do the same thing without `try`, by checking the value first.

Then answer this. Which version do you prefer, and why?

### 8.11 Save and load a dictionary

Ask the user for five names and scores, store them in a dictionary (a collection you
look things up in by name), and save it with `json.dump`.

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

Test it on `code/sample.txt`.

### 8.14 Filter a file

Read a file of numbers, one per line, and write a new file containing only the even
ones.

Make sure you do not wipe the input file by accident. This is a real way to lose data,
so check which filename is in the `"w"` line (the one that wipes the file) before you
run it.

---

## Stretch

### 8.15 To-do list that remembers

Write the to-do list from the lesson yourself, without looking. It should save on every
change and load on start.

Then add marking items as done. The simplest way is to store each item as a dictionary
rather than a string.

```python
[{"text": "buy milk", "done": False}]
```

### 8.16 Grade book on disk

Ask for student names and scores, store them in a dictionary, and save to JSON.

Then add a second run mode. If the file already exists when the program starts, load it
and let the user add more students rather than starting empty.

This is the first program here that behaves differently depending on whether it has been
run before, which is what makes it feel like real software.

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
names for every line after it.

Then think about this. Should `score` be converted to a number? What happens if one row
has a missing column?

### 8.18 A calculator that does not crash

Ask for an expression in the form `number operator number`, like `7 * 3`. Support `+`,
`-`, `*` and `/`.

Handle all of these without crashing.

- Not a number
- An operator that does not exist
- Division by zero
- Malformed input like `7 *` or just `hello`

Wrap the whole calculation in a `try` and catch (handle an error so the program does not
stop) the specific errors you expect. Then answer this. What is the danger of wrapping
too much in one `try`?

### 8.19 File statistics

Write a program that takes a filename and reports the number of lines, words,
characters, the longest word, and the most common word.

Handle the file not existing, and handle the file being empty, both without crashing. An
empty file is the case people forget, and it breaks the longest-word and
most-common-word logic.

---

## Before next session

Be able to do these without notes.

- Open and read a file, line by line, with `with`.
- Write to a file, and explain the difference between `"w"` and `"a"`.
- Explain why reading a line gives you an extra newline.
- Write a `try` and `except` that handles a bad number.
- Save a dictionary with `json` and load it back.
