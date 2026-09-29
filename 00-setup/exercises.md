# Unit 00 exercises

These are mostly about your environment, not about Python. Do them in order.

---

## 1. Prove Python is installed

Open a terminal and run the version command for your system.

Windows:

```
python --version
```

macOS or Linux:

```
python3 --version
```

Write down the version number you see. If you get an error, or the Microsoft Store
opens, the install did not finish properly. Tell me before going on.

---

## 2. Use the shell as a calculator

Type `python3` (or `python` on Windows) with no file name and press Enter. You should
see `>>>`.

Work out the answers to these in the shell, and write down each answer.

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

Leave the shell with `exit()`.

---

## 3. Write your first file

Make a new file called `about_me.py`. Type this by hand, do not copy and paste.

```python
print("My name is ...")
print("I am learning Python")
print("My favourite food is ...")
```

Fill in your own answers. Run it with `python3 about_me.py` and check the three lines
appear.

---

## 4. Break it on purpose

Now, one at a time, make each of these changes, and before running it write down what
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

Open `code/broken.py` and run it. It will fail.

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

- Open a terminal, navigate to your `python-work` folder, and run a `.py` file.
- Open a blank file and write a program with three `print()` lines.
- Read an error message from the bottom up, out loud.
