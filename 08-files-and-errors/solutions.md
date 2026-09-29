# Unit 08 solutions

## Warm-ups

### 8.1 Predict the output

The file contains only `two` and a newline.

Opening in `"w"` mode wipes the file immediately, before the `write` even happens. So
the first block writes `one`, and the second block empties the file and writes `two`.
The first line is gone.

This is the behaviour that surprises people, and it is worth running to see rather than
believing it.

### 8.2 Predict the output

The file contains `one` and `two`, each on its own line.

`"a"` means append, so it adds to the end without wiping. That is the difference between
8.1 and 8.2, and it is the whole reason both modes exist.

### 8.3 What error?

| Code | Error |
| --- | --- |
| opening a missing file | `FileNotFoundError` |
| `file.write(42)` | `TypeError`, you cannot write a number |
| `int("hello")` | `ValueError`, right kind of thing, wrong content |
| `100 / 0` | `ZeroDivisionError` |

The message for the first one includes the filename, which is why this error is usually
easy to fix once you have read it. Usually the file is simply not where the program is
looking.

### 8.4 Predict the output

```
B
C
```

`int("hello")` raises (signals that an error has happened) immediately, so `print("A")`
never runs. The `except` catches it (handles the error so the program does not stop) and
prints `B`. Then the `try` block is finished, and execution continues with whatever
comes after, which is `C`.

The `C` printing is the point. `try` and `except` do not stop the program, they handle
one specific problem and carry on.

### 8.5 Predict the output

```
A
C
```

No error, so the `except` block is skipped entirely and `C` still runs.

Worth comparing 8.4 and 8.5 side by side. The code after the `try` runs either way.

---

## Core

### 8.6 Count things in a file

```python
with open("sample.txt") as file:
    text = file.read

lines = text.splitlines
words = text.split

print(f"Lines: {len(lines)}")
print(f"Words: {len(words)}")
print(f"Characters: {len(text)}")
```

For `code/sample.txt`, the answers are 5 lines, 29 words and 146 characters.

The line count is worth thinking about, because it depends on how you count.

- Reading the whole file and using `splitlines` gives 5 for this file.
- Looping over the file gives 5.
- `len(text.split("\n"))` gives 6, because the file ends with a newline, which leaves
  an empty string at the end.

So the same file gives different answers depending on the method. `splitlines` and
looping both do the sensible thing. The naive `split("\n")` counts one extra because of
the trailing newline.

Check by hand. Counting the physical lines in the file is the only way to know
which answer is right, and that is a good habit to build.

The character count is also worth a look. 146 includes the newlines. Stripping the whole
text first gives 145. Both are defensible, and the difference is exactly the final
newline.

### 8.7 Write a file

```python
things = []

for i in range(5):
    things.append(input(f"Favourite thing {i + 1}: ").strip)

with open("favourites.txt", "w") as file:
    for thing in things:
        file.write(thing + "\n")

print()
with open("favourites.txt") as file:
    for i, line in enumerate(file, start=1):
        print(f"{i}. {line.strip}")
```

For the question about running it twice. With `"w"`, the second run replaces the file,
so it always contains exactly five things. That is probably what you want here, since
the user is being asked for five things again.

If you wanted to keep everything from every run, you would use `"a"` instead. Then the
file grows every time, which is the log file behaviour from exercise 8.8.

The `enumerate(file, start=1)` is a shortcut for numbering. The long form uses a counter
variable, and either is fine.

### 8.8 A log file

```python
import datetime

now = datetime.datetime.now
message = input("What happened? ").strip

with open("log.txt", "a") as file:
    file.write(f"{now} - {message}\n")

print("Logged.")
```

`"a"` is what makes this a log file. Every run adds one line and nothing is lost.

The timestamp uses `datetime.datetime.now`, which gives a full date and time object.
Turning it into a string with an f-string gives something readable like `2026-09-29
14:32:10.123456`. The microseconds are ugly, and if you want to clean it up there is a
formatting method for it, which is unit 09 material.

This is the first time your program has recorded anything about
when it ran, which is a small step toward being a real tool.

### 8.9 Safe number input

```python
def get_number(prompt):
    while True:
        text = input(prompt).strip
        try:
            return int(text)
        except ValueError:
            print("That is not a whole number, try again")

a = get_number("First number: ")
b = get_number("Second number: ")
print(f"Sum: {a + b}")
```

The key detail is that `return` is inside the `try`. If the conversion succeeds the
function returns, which ends the loop. If it fails, the loop goes round and asks again.

Some students write the `return` outside the `try`, which either crashes or returns the
wrong thing.

Test cases worth running. `hello` a few times then `5`, and also an empty line, and also
`5.5` which is a `ValueError` because `int` will not take a decimal.

### 8.10 Safe division

With `try`.

```python
a = int(input("First: "))
b = int(input("Second: "))

try:
    print(a / b)
except ZeroDivisionError:
    print("Cannot divide by zero")
```

Without `try`.

```python
a = int(input("First: "))
b = int(input("Second: "))

if b == 0:
    print("Cannot divide by zero")
else:
    print(a / b)
```

The answer to the question. Most people prefer the `if` version here, because the check
is simple and the code reads more directly. The `try` version is better when the check
is awkward or impossible, like reading a file.

There is a third position worth mentioning. Some programmers argue for `try` even here,
on the grounds that the check and the operation should not be separate, since they can
disagree if the code changes later. That is a real argument and it is why Python style
generally leans toward `try`. The point is that you can see
both and explain a preference.

### 8.11 Save and load a dictionary

Saving.

```python
import json

scores = {}

for i in range(5):
    name = input(f"Name {i + 1}: ").strip
    score = int(input(f"Score {i + 1}: "))
    scores[name] = score

with open("scores.json", "w") as file:
    json.dump(scores, file, indent=2)

print("Saved.")
```

Loading and printing sorted.

```python
import json

with open("scores.json") as file:
    scores = json.load(file)

pairs = []
for name, score in scores.items:
    pairs.append([score, name])

pairs.sort(reverse=True)

for score, name in pairs:
    print(f"{name}: {score}")
```

The sort by score uses the pair trick from unit 07. Everything here is material you
already have, which is the point. This exercise is practice, not new material.

The instruction to run it in a fresh terminal matters. It proves the data is really on
disk rather than still in memory from the first program.

If `json.load` fails with a `JSONDecodeError`, the usual cause is an empty file, which
happens if the writing program was interrupted before it wrote anything.

### 8.12 Biggest number in a file

```python
numbers = []

with open("numbers.txt") as file:
    for line in file:
        line = line.strip
        if line:
            numbers.append(int(line))

if numbers:
    print(f"Biggest: {max(numbers)}")
    print(f"Smallest: {min(numbers)}")
else:
    print("The file has no numbers in it")
```

The `if line:` guard skips blank lines, which are extremely common at the end of a file.
Without it, `int("")` is a `ValueError`.

The `if numbers:` guard handles the empty file. Without it, `max([])` is a `ValueError`.
That is the same class of problem as the `average of nothing` case from unit 04, and it
is a habit worth having.

An alternative that avoids storing everything.

```python
biggest = None
for line in file:
    ...
```

But `None` comparisons are unit 09, so the list version is fine here.

### 8.13 Word count from a file

```python
counts = {}

with open("sample.txt") as file:
    for line in file:
        for word in line.split:
            word = word.strip(".,!?").lower
            if word:
                counts[word] = counts.get(word, 0) + 1

pairs = []
for word, count in counts.items:
    pairs.append([count, word])

pairs.sort(reverse=True)

for count, word in pairs[:10]:
    print(f"{word}: {count}")
```

For `code/sample.txt`, the top two are `the` with 4 and `line` with 4, then `this` and
`is` with 2 each.

The `strip(".,!?")` matters. Without it, `line.` and `line` are different words, so the
count for `line` would be split across two keys (the names you look things up by). That
is a good thing to notice by looking at the output and asking why a word seems
to be missing.

`pairs[:10]` is a slice, from unit 02, taking the first ten. That is the neat way to do
"top ten".

### 8.14 Filter a file

```python
evens = []

with open("numbers.txt") as file:
    for line in file:
        line = line.strip
        if line and int(line) % 2 == 0:
            evens.append(line)

with open("even_numbers.txt", "w") as file:
    for number in evens:
        file.write(number + "\n")

print(f"Found {len(evens)} even numbers")
```

The warning in the exercise is the real lesson. If you wrote `"w"` on the *input*
filename by accident, the input file is wiped before a single line is read, and the data
is gone. Opening for writing truncates (cuts off the end) the file at the moment of
opening, not at the moment of writing.

Reading the whole file into a list first, then writing, is the safe habit. Doing both in
one pass with the same file would be a disaster.

Overwriting a file is one of the few ways a
beginner can really destroy work, and checking the filename on the `"w"` line (the
one that wipes the file) before running is worth the two seconds.

---

## Stretch

### 8.15 To-do list that remembers

```python
import json

def load_todos:
    try:
        with open("todos.json") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except ValueError:
        print("The save file is damaged, starting fresh")
        return []

def save_todos(todos):
    with open("todos.json", "w") as file:
        json.dump(todos, file, indent=2)

def get_number(prompt):
    while True:
        text = input(prompt).strip
        try:
            return int(text)
        except ValueError:
            print("Please enter a number")

todos = load_todos

while True:
    print()
    if todos:
        for i, todo in enumerate(todos, start=1):
            print(f"{i}. {todo}")
    else:
        print("(nothing to do)")

    print("\n1. Add 2. Remove 3. Quit")
    choice = input("Choose: ").strip

    if choice == "1":
        todos.append(input("What? ").strip)
        save_todos(todos)
    elif choice == "2":
        index = get_number("Which number? ")
        if 1 <= index <= len(todos):
            print(f"Removed: {todos.pop(index - 1)}")
            save_todos(todos)
        else:
            print("No such item")
    elif choice == "3":
        break
```

For the "mark as done" extension, the data shape changes.

```python
todos = [
    {"text": "buy milk", "done": False},
]
```

And the display becomes.

```python
for i, todo in enumerate(todos, start=1):
    mark = "x" if todo["done"] else " "
    print(f"{i}. [{mark}] {todo['text']}")
```

The `"x" if todo["done"] else " "` is a conditional expression (anything that produces a
value), which is unit 09 material. The long form works just as well.

```python
if todo["done"]:
    mark = "x"
else:
    mark = " "
```

The important part of the extension is that the data shape changed and everything else
had to change with it. That is a real lesson about how data structures drive programs.

### 8.16 Grade book on disk

```python
import json

def load_grades:
    try:
        with open("grades.json") as file:
            return json.load(file)
    except (FileNotFoundError, ValueError):
        return {}

def save_grades(grades):
    with open("grades.json", "w") as file:
        json.dump(grades, file, indent=2)

grades = load_grades

if grades:
    print(f"Loaded {len(grades)} students")
else:
    print("Starting with an empty grade book")

while True:
    name = input("Name (or 'done'): ").strip
    if name.lower == "done":
        break

    score = int(input("Score: "))
    grades[name] = score

save_grades(grades)

print("\nEveryone:")
for name in sorted(grades):
    print(f"{name}: {grades[name]}")
```

Note the `except (FileNotFoundError, ValueError)` form, which catches two types with one
block. That syntax is worth knowing, since it is common.

The behaviour difference based on whether the file exists is what makes this feel like
real software, and it is worth noticing. The first run starts fresh, every run
after that continues from where it left off.

### 8.17 A small CSV reader

```python
records = []

with open("data.csv") as file:
    header_line = file.readline.strip
    columns = header_line.split(",")

    for line in file:
        line = line.strip
        if not line:
            continue

        values = line.split(",")
        record = {}
        for i in range(len(columns)):
            record[columns[i]] = values[i]
        records.append(record)

for record in records:
    print(record)
```

The key idea is that `readline` reads one line and leaves the file positioned at the
next one, so the loop over `file` afterwards starts from the second line. That shows
nicely that the file keeps track of where you are.

Answers to the questions.

Should `score` be a number? It depends what you want to do with it. If you are going to
do arithmetic, yes, and you would convert it with `int`. But you cannot convert every
column, because the names are text. So the conversion has to be per column, or done at
the point of use.

What if a row has a missing column? The index loop would raise an `IndexError`, since
`values[i]` would not exist. The fix is to check the length first, or use `values[i] if
i < len(values) else ""`, which is a conditional expression. This is exactly the kind of
thing that makes real CSV reading fiddly, and it is why the `csv` module exists in the
standard library. It is worth knowing that it exists.

### 8.18 A calculator that does not crash

```python
def calculate(text):
    parts = text.split

    if len(parts)!= 3:
        return "Please write it as: number operator number"

    left_text, operator, right_text = parts

    try:
        left = float(left_text)
        right = float(right_text)
    except ValueError:
        return "Those were not numbers"

    if operator == "+":
        return left + right
    elif operator == "-":
        return left - right
    elif operator == "*":
        return left * right
    elif operator == "/":
        try:
            return left / right
        except ZeroDivisionError:
            return "Cannot divide by zero"
    else:
        return f"I do not know the operator {operator}"

while True:
    text = input("Calculate (or 'quit'): ").strip
    if text.lower == "quit":
        break
    print(calculate(text))
```

The `len(parts)!= 3` check handles malformed input like `7 *` or just `hello` before
anything else, which is cleaner than trying to unpack (take apart into separate
variables) and catching the failure.

`float` rather than `int`, so decimals work.

The answer to the question about wrapping too much in one `try`. If the whole
calculation were inside a single `try` with `except ValueError`, then a bug elsewhere in
the calculation would be silently reported as "those were not numbers", which is
misleading. Worse, if you used a bare `except:`, a typo in your own code would be
swallowed and reported as a user error.

The general principle. Put as little as possible inside the `try`, and only the part
that can actually raise the error you are catching. Here, only the conversions can raise
a `ValueError`, so only they are inside that `try`.

That is a really important habit and it is worth the extra time.

One more detail. Returning strings like `"Cannot divide by zero"` from a function that
otherwise returns numbers is a design smell (a sign of a problem in the design), since
the caller cannot tell what it got. A cleaner design would raise, or return a pair of
success and value.

### 8.19 File statistics

```python
filename = input("Filename: ").strip

try:
    with open(filename) as file:
        text = file.read
except FileNotFoundError:
    print(f"There is no file called {filename}")
else:
    lines = text.splitlines
    words = text.split

    print(f"Lines: {len(lines)}")
    print(f"Words: {len(words)}")
    print(f"Characters: {len(text)}")

    if not words:
        print("The file is empty, so there is nothing else to report")
    else:
        longest = words[0]
        for word in words:
            if len(word) > len(longest):
                longest = word
        print(f"Longest word: {longest}")

        counts = {}
        for word in words:
            word = word.strip(".,!?").lower
            if word:
                counts[word] = counts.get(word, 0) + 1

        top = None
        for word, count in counts.items:
            if top is None or count > top[1]:
                top = [word, count]

        print(f"Most common: {top[0]} ({top[1]} times)")
```

The `else` on the `try` is doing real work here. It runs only when the file was opened
successfully, which means the whole analysis is skipped cleanly when the file is
missing, without needing to indent everything inside the `try`. This is exactly what
`else` is for, and this is the best example of it in the course.

The empty file case is handled by `if not words`. Without it, `words[0]` is an
`IndexError`, and the loop would find nothing. That is the case people forget, and it is
the reason the exercise asks about it.

`top = None` followed by `top is not None` is `None` comparison, which is unit 09. The
long way round with a `found` flag works if you prefer.

There is a much shorter version of the most-common-word logic using the pair sorting
from unit 07.

```python
pairs = sorted([[count, word] for word, count in counts.items], reverse=True)
top = pairs[0]
```

That uses a list comprehension, which is not taught on purpose. If you write it, good
for you, but the loop version is what the course wants.
