# Unit 00 solutions

## 1. Version check

Anything from `Python 3.8` upwards is fine for this course. Modern systems give 3.10 or
newer. If you see `Python 2.7`, that is the old version and nothing in this course will
work, so install a current one.

## 2. Shell arithmetic

```
12 + 30 -> 42
100 - 45 -> 55
7 * 8 -> 56
10 / 4 -> 2.5
2 ** 10 -> 1024
```

Answers to the two questions.

`10 / 4` gives `2.5`, not `2`. Division in Python 3 always gives a decimal result, even
when it divides evenly. `10 / 2` gives `5.0`, with the point. This is a design choice
made on purpose and it will come back in unit 01 when we meet the two different division
operators.

`**` means "to the power of", so `2 ** 10` is two to the tenth, which is 1024. It is
written with two asterisks because `^` already means something else in Python, a bitwise
operation you do not need to know about.

If you guessed that `*` repeated a string, that is also correct and worth remembering,
since `"ab" * 3` gives `"ababab"`. You will meet it again.

## 3. about_me.py

Anything that runs and prints three lines is correct. There is no right answer, the
point is producing a working file from scratch.

```python
print("My name is Ada")
print("I am learning Python")
print("My favourite food is noodles")
```

The one thing to check is that you typed the file in an editor and saved it with a
`.py` extension, in the folder you are running the command from. A very common early
failure is running `python3 about_me.py` from the wrong directory, which gives `can't
open file 'about_me.py': [Errno 2] No such file or directory`. That message means the
file is not where the terminal is looking, not that the file does not exist.

## 4. Breaking it on purpose

Here is what each change produces. Read your own predictions first,
since comparing a prediction with reality is the exercise.

**Delete the closing bracket on `print()`**

```
  File "about_me.py", line 2
    print("I am learning Python"
         ^
SyntaxError: '(' was never closed
```

The caret points at the opening bracket, not at the end of the line. That is because
Python is telling you which bracket it lost track of, which is the useful piece of
information. This is worth noticing, since students expect the caret to point at where the
problem "is".

**Delete the closing quote**

```
  File "about_me.py", line 3
    print("My favourite food is noodles)
                                        ^
SyntaxError: unterminated string literal (detected at line 3)
```

The caret sits at the end of the line, at the point where Python gave up looking for the
missing quote. Python treats everything after an opening quote as text,
right up to the end of the line, so it reached the end and still had not found the
closing one.

**Remove the brackets, `print "hello"`**

```
    print "hello"
    ^^^^^^^^^^^^^
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
```

This error is unusually helpful. It means Python understood you wanted to print, and is
telling you the modern syntax. Note that older tutorials and code from before 2008 use
the bracketless form. If you see it anywhere, the code is old.

**Capitalise the P, `Print("hello")`**

```
    Print("hello")
    ^^^^^
NameError: name 'Print' is not defined
```

The important detail is that this is a `NameError`, not a `SyntaxError`. The code is
valid Python, it is asking for a thing called `Print` that does not exist. Python is
case sensitive, so `print` and `Print` are entirely different names as far as it is
concerned.

This is worth dwelling on. Case sensitivity will cause problems for you repeatedly.
Get in the habit of reading names character by character when a `NameError`
appears.

## 5. broken.py

The output is this, and nothing else.

```
  File "broken.py", line 15
    print("Line two)
                   ^
SyntaxError: unterminated string literal (detected at line 15)
```

The missing thing is the closing double quote on the second print.

The important question is number four. "Line one" is never printed, because the program
never started. When Python cannot understand the file, it refuses to run any of it. Not
even the lines above the mistake.

This is a really useful distinction and worth keeping in mind.

- A `SyntaxError` means nothing ran at all. The mistake could be anywhere.
- An error at runtime, such as `NameError` or `TypeError`, means the program
  started and got partway through before hitting trouble.

That is why reading the error type first is worth doing. It tells you whether you are
looking at a broken file or a working file that misbehaved at line 15.

(Line numbers above assume the file is unchanged. If you edited it, the line number
will differ, and the correct answer is whatever your error actually said.)

## 6. The comment test

```python
print("My favourite food is noodles")
```

without the `#` is now a real line of code, and it fails with a `SyntaxError` or a
`NameError`, depending on what words followed.

If your comment was something like `# because noodles are perfect`, then removing the
`#` leaves this.

```
print("My favourite food is noodles")
because noodles are perfect
```

The first line runs fine, then Python hits `because noodles are perfect`, which is not
valid Python, and refuses to run the file at all. Since it is a syntax error, nothing
runs, so the first print does not appear either. A nice echo of question 5.

The lesson is that `#` is not decoration. It is the thing that tells Python to skip the
rest of the line.

## 7. three_lines.py

```python
print("First line")
print("Second line")
print("Third line")
```

There is no expected content. What matters is that you can produce a running
file from a blank page without help, and that you noticed what you had to look up.

## Stretch

A house, for example.

```python
print(" /\\ ")
print(" / \\ ")
print(" /____\\ ")
print(" | | ")
print(" |____| ")
```

The double backslash is the interesting part. `\\` in a string means one backslash,
because a single backslash is special and starts an escape sequence, like the `\n` for a
new line you may have already met. So `"\\"` prints a single `\`.

For the quote question, there are three answers and all of them are useful to know.

```python
# Option 1: wrap in single quotes
print('She said "hello"')

# Option 2: escape the inner quotes
print("She said \"hello\"")

# Option 3: use a triple-quoted string
print("""She said "hello" """)
```

Option 2 is the general technique and the one to learn, because it works everywhere and
in any combination. Backslash means "the next character is literal, do not treat it as
special". This works the same way as `\\` from the house drawing.

Option 3 is a preview rather than a lesson. Triple quotes make a multi-line string, and
you will meet it properly later.

Once you get this, be amused by `print("She said \"\\\"hello\\\"\"")` for a
moment and then move on.
