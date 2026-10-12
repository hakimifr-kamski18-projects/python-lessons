---
title: Unit 00 exercises
sidebar:
  label: Exercises
---
These are about getting a file to run and reading your first errors, rather than about
Python itself. Do them in order.

---

## Before you start

Three small facts will help you in the exercises below.

A **comment** (a note for humans, starting with `#`) is ignored by Python. The first
line below is a comment, so only the second line does anything.

```python
# This is a comment. Python will not run this line.
print("But this line runs.")
```

The **console** shows `>>>` where you type. You never type the `>>>` yourself, and a
line that starts with `>>>` is a `SyntaxError` (a mistake in how the code is written)
if you put it in a file. In the console the answer appears by itself. In a file,
nothing appears unless you use `print()`.

When Python finds an error, it shows several lines. Read them like this.

- The last line says what went wrong.
- The line that starts with `File` has the file name and the line number.
- Below it, Python shows your line of code. A caret (the `^` mark) points at the place
  it is complaining about. The caret can sit in a slightly different place in different
  Python versions, so trust the last line most.

---

## 1. Get a program to run

You should already have an editor open with Python working in it. If the Run button
does nothing, or you cannot find it, fix that first. Look at the help pages of your
editor, or ask whoever set it up for you.

Make a new file called `hello.py` and type this, by hand, no copying. The name must
end in `.py`. Save the file in a folder you can find again, for example a folder called
`python-work`.

```python
print("Hello, world!")
```

Now click the **Run** button. Do not type any commands anywhere. The editor runs the
file for you, and uses the folder the file is in.

Say each answer to yourself, or write it down.

1. Where did the output appear? Point at it.
2. Click Run again. What happens the second time?
3. Change the message to your own name and run it again.

If you see your message printed, you have already done the hardest part.

---

## 2. Use the Python console as a calculator

Your editor has a second place to type Python, separate from a file. It is called the
console, and it shows `>>>` where you type. It is a live conversation. Type something,
press Enter, see the answer immediately.

To open it in VS Code, press Ctrl+Shift+P, type `Python: Start REPL`, and press Enter.
In other editors, look for a tab or panel called Console, Shell or REPL.

Work out these answers there. Do not type the `>>>`. Write each answer down.

```
12 + 30
100 - 45
7 * 8
10 / 4
2 ** 10
```

Then answer these two questions in your own words.

- What did `10 / 4` give you, and did it surprise you?
- What do you think `**` does?

There is nothing to save and nothing to run. The console forgets everything when you
close it, which is exactly why finished work goes in a file. In a file, the answer to
a sum does not show unless you `print()` it.

---

## 3. Write your first file

Make a new file called `about_me.py`. Type this by hand, do not copy and paste.

```python
print("My name is ...")
print("I am learning Python")
print("My favourite food is ...")
```

Fill in your own answers. Click Run, and check that the three lines appear.

---

## 4. Break it on purpose

Make each of these changes in `about_me.py`, one at a time. Undo each change before you
try the next one. Before clicking Run, write down what you think will happen.

| Change | Your prediction | What actually happened |
| --- | --- | --- |
| Delete the closing `)` on the second print | | |
| Delete the closing `"` on the second print | | |
| Remove the parentheses (the round brackets) so it reads `print "hello"` | | |
| Capitalise the P, so it reads `Print` | | |

For each error, before fixing it, read the last line of the error and write down what
it said.

---

## 5. Read an error without panicking

Create a file called `broken.py`. Copy the text from [`broken.py`](/code/00-setup/broken.py)
into it, save it, and click Run. This is the one file where copying is fine. It will
fail.

Say or write your answers.

1. What is the last line of the error, exactly?
2. Which file and line number does it point at?
3. Look at that line in the file. What is missing?
4. Why did "Line one" never get printed?

Fix it and run it again.

---

## 6. The comment test

A comment is a line that starts with `#`. Python ignores it. Add a comment to
`about_me.py` that explains why you chose your favourite food, for example
`# I like noodles because they are quick`. Then delete the `#` at the start of that
line and run the file again.

- What happened, and why?

Put the `#` back.

---

## 7. From scratch, no notes

Close every file you have open. Without looking at anything, make a new file called
`three_lines.py` that prints three different lines. Run it.

If you had to look something up, that is completely fine, but write down what you had to
look up. Practise that.

---

## Stretch (only if the rest was easy)

Make a file called `shout.py` that uses several `print()` lines to draw a picture made
of keyboard characters, for example a small house or a face. It must run without errors.

Then try to make Python print a sentence containing a double quote inside the quotes,
such as `She said "hello"`. It will not work the way you expect. See if you can work out
how to do it. Hint: think about what character you might use to wrap the text instead.

---

## Check yourself

Be able to do these without help.

- Open a blank file, write a program, and run it with the Run button.
- Say to yourself what the console is for, and why it is not where finished work goes.
- Read an error message from the bottom up.
