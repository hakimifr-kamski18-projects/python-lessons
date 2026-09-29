---
title: Unit 08 — Files and errors
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
**Files for this unit.** [`errors.py`](/code/08-files-and-errors/errors.py), [`file_read.py`](/code/08-files-and-errors/file_read.py), [`file_write.py`](/code/08-files-and-errors/file_write.py), [`save_data.py`](/code/08-files-and-errors/save_data.py), [`validation.py`](/code/08-files-and-errors/validation.py)

These live in `public/code/08-files-and-errors/` in the repository, and the links above
open them as plain text. Every snippet the student needs is already inline in the
exercises, so the files are for the session itself, when you are both at the
keyboard.

**Goal for the session.** Their programs can save data between runs, and they can
survive bad input instead of crashing.

**Time.** Two sessions. Either half is a full session on its own.

**Prerequisites.** Unit 07. Dictionaries, `.items`, the counting pattern.


---

## 0. Warm-up

Have them write a word counting program from scratch, using the dictionary counting
pattern. That is the unit 07 retrieval check and it needs to be solid, because it comes
back today with a file as the input instead of a typed sentence.

Then run it and have them enter some text. Now ask the question. "Run it again and type
the same thing. Then close the terminal and open a new one. Where did the data go?" It
is gone. That is today's motivation.

## 1. Reading a file

Before opening anything, look at [`sample.txt`](/code/08-files-and-errors/sample.txt) so they know what is in it.

### The `with` form, which is the one to use

```python
with open("sample.txt", "r") as file:
    contents = file.read()

print(contents)
```

Explain the pieces.

- `open("sample.txt", "r")` opens the file for reading. The `"r"` is the mode and it
  is the default, so it can be left off, though writing it is clearer.
- `as file` gives the open file a name to use inside the block.
- The indented block is where you use the file.
- When the block ends, the file closes automatically.

The `with` keyword is there to make sure the file gets closed even if something goes
wrong partway through. Teach it as the only form, and mention the alternative only so
they recognise it if they see it.

```python
file = open("sample.txt")
contents = file.read()
file.close()
```

That works and it is easy to forget the `close()`. The `with` version cannot be
forgotten.

### The file path problem

The most common failure at this point is not the code. It is the file being somewhere
else.

```
FileNotFoundError: [Errno 2] No such file or directory: 'sample.txt'
```

The message names the file it was looking for. The fix is either to move the file, or to
give a full path, or to make sure the terminal is in the right folder.

Have them hit this on purpose. Rename the file and run the code, then read the error and
fix it. This is one of the errors where the message is completely clear and the mistake
is still extremely common.

### Reading in three different ways

```python
# everything at once, as one big string
with open("sample.txt") as file:
    contents = file.read()
print(contents)
```

```python
# a list of lines
with open("sample.txt") as file:
    lines = file.readlines()
print(lines)
```

```python
# line by line, in a loop
with open("sample.txt") as file:
    for line in file:
        print(line)
```

The third is the right one for almost everything, and it is what they should reach for.
It handles large files without loading everything into memory at once, and it is the
most readable.

### The newline problem

Run the loop version and look carefully at the output. There is a blank line between
each line of text. Have them notice it and work out why before you explain.

Each line from a file includes the newline character at the end. So `line` holds
`"hello\n"`, and `print` adds another newline, giving the blank line.

Two fixes.

```python
for line in file:
    print(line.strip())
```

```python
for line in file:
    print(line, end="")
```

The `end=""` stops `print` adding its own newline, so the one that came with the line is
the only one. Both work. `.strip()` is more common, and it also cleans up trailing
spaces, which `end=""` does not.

This is worth real time, because it is the cause of a lot of confusing output.

Also note that `.strip()` removes leading whitespace (spaces, tabs and blank lines) too.
If the file has indented content, `.rstrip("\n")` is more careful. Not needed here, and
worth a mention.

### Reading into a dictionary

The shape that connects to unit 07. A file of `name,score` lines.

```python
scores = {}

with open("scores.txt") as file:
    for line in file:
        line = line.strip()
        if not line:
            continue
        name, score = line.split(",")
        scores[name] = int(score)

print(scores)
```

Read it in order. Strip the newline. Skip empty lines, which are common at the end of a
file. Split on the comma. Unpack the two pieces into two variables. Convert the score,
because everything from a file is text, exactly like `input()`.

That last point is worth emphasising. File contents have the same problem as user input.
Everything is a string. The `int()` conversions are not optional.

## 2. Writing files

Open [`file_write.py`](/code/08-files-and-errors/file_write.py).

```python
with open("output.txt", "w") as file:
    file.write("Hello\n")
    file.write("Second line\n")
```

Three things.

**`"w"` means write, and it wipes the file.** If the file already exists, opening it in
write mode empties it immediately. Have them run the program twice and see that the file
has two lines, not four. This surprises people.

**`write()` does not add a newline.** Unlike `print`, which adds one automatically,
`write()` writes exactly what you give it. So `"\n"` has to be written out, or
everything ends up on one line.

**You cannot write whitespace-free numbers.** `file.write(42)` is a `TypeError`.
Everything written to a file has to be a string.

```python
with open("output.txt", "w") as file:
    file.write(str(42) + "\n")
```

### Appending

```python
with open("log.txt", "a") as file:
    file.write("Something happened\n")
```

`"a"` means append. It adds to the end instead of wiping. Have them run this program
three times and see the file grow, then change it to `"w"` and see it stop growing.

That comparison is the whole lesson. `"w"` replaces, `"a"` adds.

A common mistake to show. Using `"w"` inside a loop, which wipes the file on every pass
and leaves only the last line. Have them write a loop that writes 1 to 5 and use `"w"`
inside the loop rather than opening the file once outside it. Then look at the file.

```python
# WRONG. Opens and wipes the file on every pass.
for i in range(1, 6):
    with open("numbers.txt", "w") as file:
        file.write(f"{i}\n")
```

That leaves a file containing only `5`. The fix is to open the file once, outside the
loop.

```python
with open("numbers.txt", "w") as file:
    for i in range(1, 6):
        file.write(f"{i}\n")
```

This is a good one to have them actually do, because the mistake is easy to make and the
symptom is confusing.

### A summary of the modes

```
"r"   read          the file must exist
"w"   write         wipes the file, or creates it
"a"   append        adds to the end, or creates it
```

There are others, and these three are all they need.

## 3. Errors, and handling them

Open [`errors.py`](/code/08-files-and-errors/errors.py).

They have been reading errors for eight units. Now they learn to handle them.

The shape.

```python
try:
    number = int(input("Number: "))
    print(f"Double: {number * 2}")
except ValueError:
    print("That was not a number")
```

Read it out loud. "Try to do this. If this particular kind of error happens, do this
instead."

Two things to be clear about.

**Specific error types.** `except ValueError` catches (handles an error so the program
does not stop) only `ValueError`. A `ZeroDivisionError` in the same block still crashes.
That is good, because it means the except only hides the errors you planned for.

**Bare `except:` is a bad habit.** Show them that `except:` with nothing catches
everything, including typos in their own code and things they never intended to handle.
It makes bugs invisible. Name the error type instead.

**Do not use try/except as a substitute for thinking.** If you can check something
before doing it, checking is usually clearer.

```python
# checking first
if text.isdigit():
    number = int(text)

# asking for forgiveness
try:
    number = int(text)
except ValueError:
    ...
```

Both are legitimate. The first is clearer when the check is simple. The second is
necessary when there is no simple check, like reading a file that may not exist.

### Catching several types

```python
try:
    number = int(input("Number: "))
    result = 100 / number
    print(result)
except ValueError:
    print("That was not a number")
except ZeroDivisionError:
    print("Cannot divide by zero")
```

Have them run it with `hello` and then with `0`, and see the two different messages.

### The validation loop

Open [`validation.py`](/code/08-files-and-errors/validation.py). This is the pattern they will use constantly, and it combines
a loop from unit 04 with `try` from today.

```python
def get_number(prompt):
    while True:
        text = input(prompt).strip()
        try:
            return int(text)
        except ValueError:
            print("That is not a whole number, try again")

age = get_number("Your age: ")
print(f"Next year you will be {age + 1}")
```

Trace the two cases. Valid input returns immediately, which ends the function and so
ends the loop. Invalid input prints a message and the loop goes round again.

The clever part is that the `return` is inside the `try`. If the conversion works, the
function is done. This is the first place where a `return` inside a loop inside a `try`
all work together, and it is worth tracing carefully.

Have them write this function and then reuse it for several different questions.

### `else` and `finally`

Mention them, do not drill them.

```python
try:
    number = int(text)
except ValueError:
    print("not a number")
else:
    print("that worked")      # runs only if no error
finally:
    print("this always runs")
```

`finally` is mostly used for cleanup, and the `with` statement (one complete
instruction) already handles the file case. Skip in practice.

## 4. Saving structured data

Open [`save_data.py`](/code/08-files-and-errors/save_data.py). This is the section that makes files actually useful.

Saving a dictionary to a file by hand is fiddly, because everything has to be text and
you have to read it back. Python has a format for this.

```python
import json

scores = {"Ada": 88, "Grace": 95}

with open("scores.json", "w") as file:
    json.dump(scores, file)

with open("scores.json") as file:
    loaded = json.load(file)

print(loaded)                # {'Ada': 88, 'Grace': 95}
print(type(loaded))          # dict
```

Two functions. `json.dump` writes a structure to a file. `json.load` reads one back.

Have them open `scores.json` in a text editor and look at it. It is readable, which is
the point.

```json
{"Ada": 88, "Grace": 95}
```

The round trip is worth showing clearly. Write a dictionary, read it back, and print
both. The fact that the types survive, that numbers come back as numbers and not
strings, is a really nice thing that the manual version does not give you.

And with a list of dictionaries, which is the shape from unit 07.

```python
students = [
    {"name": "Ada", "score": 88},
    {"name": "Grace", "score": 95},
]

with open("students.json", "w") as file:
    json.dump(students, file, indent=2)
```

The `indent=2` makes it readable rather than one long line. Have them try with and
without.

A warning worth giving. `json.load` on a file that is empty or contains something that
is not valid JSON gives a `JSONDecodeError`, which is another error to catch. That error
type is a subclass of `ValueError`, so `except ValueError` catches it too. That is a
slightly surprising detail and it is worth knowing.

## 5. Putting it together

Build a persistent to-do list together.

```python
import json

def load_todos():
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
        text = input(prompt).strip()
        try:
            return int(text)
        except ValueError:
            print("Please enter a number")

todos = load_todos()

while True:
    print()
    if todos:
        for i, todo in enumerate(todos, start=1):
            print(f"{i}. {todo}")
    else:
        print("(nothing to do)")

    print("\n1. Add  2. Remove  3. Quit")
    choice = input("Choose: ").strip()

    if choice == "1":
        todos.append(input("What? ").strip())
        save_todos(todos)

    elif choice == "2":
        index = get_number("Which number? ")
        if 1 <= index <= len(todos):
            removed = todos.pop(index - 1)
            print(f"Removed: {removed}")
            save_todos(todos)
        else:
            print("No such item")

    elif choice == "3":
        break
```

Note the `enumerate(todos, start=1)`, which is a shortcut for keeping a count while
looping. It is the answer to "how do I print numbered items" and it is worth introducing
here even though it is technically unit 09 material. If you would rather not, use a
counter.

```python
number = 1
for todo in todos:
    print(f"{number}. {todo}")
    number += 1
```

Either way, the important bits of this program are the two functions at the top.
`load_todos` handles the file not existing yet, which is the normal first run, and
handles a damaged file without crashing. `save_todos` is called every time something
changes, so nothing is lost if the program closes.

Have them run it, add two items, quit, and run it again. The items are still there. That
is the moment this unit is for.

Then extend it.

- Mark items as done, which needs a list of dictionaries rather than strings.
- Add a "clear all" option.
- Store the date each item was added.

---

## Teaching notes for this unit

**Hit `FileNotFoundError` on purpose.** It is the most common problem beginners have
with files, and it is almost never a code problem. Naming it directly, and showing that
the error message tells you the exact filename, saves a lot of confused afternoons.

**The newline problem needs to be discovered, not announced.** Run the read loop, let
them see the blank lines, and ask why. The answer, that the file gives you the newline
as part of the line, is much more memorable when they have had to account for the
evidence.

**The `"w"` wipes the file behaviour is really surprising.** Show it by running a
program twice and showing the file did not grow. Then change to `"a"` and show that it
does.

**The `"w"` inside a loop is the classic bug of this unit.** Have them write it, look at
the file, and find the fix themselves.

**`try` and `except` should not be taught as a way to make errors go away.** If a
student starts wrapping everything in `try`, that is a warning sign. The good use is the
validation loop (a loop that asks again until the answer is valid), where a bad value is
an expected part of the interaction. The bad use is hiding bugs. Say so.

**Never use a bare `except:`.** Show them once how it swallows a typo in their own code,
and explain that catching everything is usually a mistake.

**`json` is the payoff for the whole unit.** Saving a dictionary across runs is the
thing that makes a program feel real, and it is also the thing that means they no longer
need to retype test data every time they run something. Expect them to start using it in
every exercise from now on, which is exactly right.

**The to-do list is the best exercise in the course so far.** It uses every single unit,
it persists, and it is a program they might really use. Give it the time it needs.

**Exercise 8.9, the `return` inside `try`.** Trace it carefully with them if that
happens.

**Exercise 8.10, the two versions.** Do not push either way.

**Exercise 8.18, returning strings from the calculator.** Do not push this, but if a
student spots it, that is a very good sign.

**Preview of next unit.** They have everything they need to write a real program. Next
session is about the standard library, which is where they find out that most of the
work has already been done by somebody else.
