---
title: Unit 00 exercises
sidebar:
  label: Exercises
---
These are about getting a file to run and reading your first errors, rather than about
Python itself. Do them in order.

---

## 1. Get a program to run

You should already have an editor open with Python working in it. If the Run button
does nothing, or you cannot find it, stop and tell me rather than guessing.

Make a new file called `hello.py` and type this, by hand, no copying.

```python
print("Hello, world!")
```

Now click the **Run** button. Do not type any commands anywhere. The editor runs the
file for you, and figures out which folder it is in.

Answer these out loud.

1. Where did the output appear? Point at it.
2. Click Run again. What happens the second time?
3. Change the message to your own name and run it again.

If you see your message printed, the whole of today has already worked.

---

## 2. Use the Python console as a calculator

Your editor has a second place to type Python, separate from a file. It is called the
console, and it shows `>>>` where you type. It is a live conversation. Type something,
press Enter, see the answer immediately.

Find the console in your editor and work out these answers there. Write each one down.

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
close it, which is exactly why finished work goes in a file.

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

Now, one at a time, make each of these changes, and before clicking Run write down what
you think will happen.

| Change | Your prediction | What actually happened |
| --- | --- | --- |
| Delete the closing `)` on the second print | | |
| Delete the closing `"` on the second print | | |
| Remove the brackets so it reads `print "hello"` | | |
| Capitalise the P, so it reads `Print` | | |

For each error, before fixing it, read the last line of the error out loud and write
down what it said.

---

## 5. Read an error without panicking

Open [`broken.py`](/code/00-setup/broken.py) and click Run. It will fail.

Answer these out loud, not on paper.

1. What is the last line of the error, exactly?
2. Which file and line number does it point at?
3. Look at that line in the file. What is missing?
4. Why did "Line one" never get printed?

Fix it and run it again.

---

## 6. The comment test

Add a comment to `about_me.py` that explains why you chose your favourite food. Then
delete the `#` at the start of the line and run it again.

- What happened, and why?

Put the `#` back.

---

## 7. From scratch, no notes

Close every file you have open. Without looking at anything, make a new file called
`three_lines.py` that prints three different lines. Run it.

If you had to look something up, that is completely fine, but write down what you had to
look up. That is the thing to practise before next time.

---

## Stretch (only if the rest was easy)

Make a file called `shout.py` that uses four separate `print()` lines to draw an ASCII
picture, for example a small house or a face. It must run without errors.

Then try to make Python print a sentence containing a double quote inside the quotes,
such as `She said "hello"`. It will not work the way you expect. See if you can work out
how to do it. Hint, think about what character you might use to wrap the text instead.

---

## Before next session

Be able to do these without help.

- Open a blank file, write a program, and run it with the Run button.
- Say out loud what the console is for, and why it is not where finished work goes.
- Read an error message from the bottom up, out loud.
