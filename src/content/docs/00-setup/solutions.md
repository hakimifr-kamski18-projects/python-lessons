---
title: Unit 00 solutions
sidebar:
  label: Solutions
---
## 1. Get a program to run

There is nothing to get right here. The point of the exercise is that the whole loop
works: you type a file, you click Run, you see output.

Where the output appears depends on your editor. Most put it in a panel at the bottom of
the window, sometimes called Output, sometimes Terminal. Clicking Run a second time does
it all again and prints your message again. The program starts fresh every single time
you run it.

If Run did nothing, or you could not find it, that is an editor problem rather than a
Python one. Fix it before you go on, by reading the help pages of your editor or asking
whoever set it up for you. Everything in the next nine units depends on this one button.

## 2. Python console arithmetic

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
made on purpose and it will come back in unit 01, where you meet the two different
division operators.

`**` means "to the power of", so `2 ** 10` is two to the tenth, which is 1024. It is
written with two asterisks because `^` already means something else in Python.

The console is for exactly this, trying something small and seeing the answer straight
away. The moment you want to keep it, it goes in a file instead.

## 3. about_me.py

Anything that runs and prints three lines is correct. There is no right answer, the
point is producing a working file from scratch.

```python
print("My name is Ada")
print("I am learning Python")
print("My favourite food is noodles")
```

The one thing to check is that you saved the file with a `.py` extension. An editor will
happily let you type a whole program into a file called `about_me` with no ending at all,
and then Run will do nothing useful with it.

You do not have to think about which folder the file is in. That is the Run button's job,
and it is one of the main reasons to use it. If you ever see a message about not being
able to open or find a file, the editor is looking in a different folder from the one
your file is in. Find out which folder your file is in, and open that folder in your
editor, rather than trying to work around the message.

## 4. Breaking it on purpose

Here is what each change produces. Read your own predictions first, since comparing a
prediction with reality is the exercise.

Your Python version may draw the `^` mark (the caret) a little differently from the
examples here. The last line of each error is the part to trust.

**Delete the closing parenthesis on `print()`**

```
  File "about_me.py", line 2
    print("I am learning Python"
         ^
SyntaxError: '(' was never closed
```

The caret points at the opening parenthesis `(`, not at the end of the line. Python is
telling you which parenthesis it lost track of, which is the useful piece of
information. You might expect the caret to point at the place where the problem "is",
but here it points at where the unfinished part began.

**Delete the closing quote**

```
  File "about_me.py", line 2
    print("I am learning Python)
          ^
SyntaxError: unterminated string literal (detected at line 2)
```

The caret points at the opening quote, the one that was never closed. "Unterminated
string literal" means a piece of text in quotes that never ends. Python treats
everything after an opening quote as text, right up to the end of the line, so it
reached the end and still had not found the closing quote.

**Remove the parentheses, `print "hello"`**

```
    print "hello"
    ^^^^^^^^^^^^^
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
```

This error is unusually helpful. It means Python understood you wanted to print, and is
telling you the modern way to write it. Older tutorials and code from before 2008 use
the form without parentheses. If you see it anywhere, the code is old.

**Capitalise the P, `Print("hello")`**

```
Traceback (most recent call last):
  File "about_me.py", line 2, in <module>
    Print("hello")
    ^^^^^
NameError: name 'Print' is not defined. Did you mean: 'print'?
```

The important detail is that this is a `NameError`, not a `SyntaxError`. The code is
valid Python, it is asking for a thing called `Print` that does not exist. Python
treats capital and small letters as different, so `print` and `Print` are entirely
different names as far as it is concerned. Your Python version may leave out the
"Did you mean" part.

This will cause problems for you again and again. Get in the habit of reading names
character by character when a `NameError` appears.

## 5. broken.py

The output is this, and nothing else. The file name on the first line will show the
folder where you saved your copy.

```
  File "broken.py", line 10
    print("Line two)
          ^
SyntaxError: unterminated string literal (detected at line 10)
```

The caret position can differ between Python versions, so the last line is the part to
trust.

The missing thing is the closing double quote on the second print.

The important question is number four. "Line one" is never printed, because the program
never started. When Python cannot understand the file, it refuses to run any of it. Not
even the lines above the mistake.

This is a useful difference to keep in mind.

- A `SyntaxError` means nothing ran at all. The mistake could be anywhere.
- An error that happens while the program runs, such as `NameError` or `TypeError`,
  means the program started and got partway through before hitting trouble.

That is why reading the error type first is worth doing. It tells you whether you are
looking at a broken file or a working file that failed partway through.

(The line number above assumes the file is unchanged. If you edited it, the line number
will differ, and the correct answer is whatever your error actually said.)

## 6. The comment test

With the `#`, this line is a comment and Python skips it.

```python
# I like noodles because they are quick
```

Without the `#`, it is a real line of code.

```python
I like noodles because they are quick
```

Python cannot understand it, so you get `SyntaxError: invalid syntax`. Because it is a
syntax error, nothing runs, so the print lines above it do not appear either. This is
the same rule as `broken.py` in exercise 5.

If your comment was a single word, such as `# noodles`, you get a `NameError` instead.
A single word is valid Python, it names something, but nothing called `noodles` exists.
That error happens while the program runs, so the lines above it do print first.

The point is that `#` is not decoration. It is the thing that tells Python to skip the
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
because a single backslash is special. It starts an escape sequence (a backslash plus a
letter or mark that stands for one special character). For example, `\n` means a new
line. So `"\\"` prints a single `\`.

For the quote question, there are two answers and both are useful to know.

```python
# Option 1: wrap in single quotes
print('She said "hello"')

# Option 2: escape the inner quotes
print("She said \"hello\"")
```

Option 2 is the general technique and the one to learn, because it works everywhere and
in any combination. A backslash means "the next character is just a character, do not
treat it as special". This works the same way as `\\` in the house drawing.
