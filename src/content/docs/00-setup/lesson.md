---
title: Unit 00 — Getting Python to say something
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
**Files for this unit.** [`broken.py`](/code/00-setup/broken.py), [`hello.py`](/code/00-setup/hello.py)

These live in `public/code/00-setup/` in the repository, and the links above
open them as plain text. Every snippet the student needs is already inline in the
exercises, so the files are for the session itself, when you are both at the
keyboard.

**Goal for the session.** They install Python and an editor, run a file they wrote
themselves, see output, and read their first error message calmly.

**Time.** 45 to 90 minutes, and most of it is installation. Do not try to teach concepts
in this session. The win is a working environment and no fear.

**Prerequisites.** None. This is the first session.


---

## Before you start, check the laptop situation

Ask them what they are working on. It changes everything about the next thirty minutes.

**Windows.** They will install from python.org. The one thing that matters is ticking
the box that says "Add python.exe to PATH" on the first installer screen. If that box is
missed, the `python` command will not be found and the fix is either reinstalling or
doing it by hand, so watch them tick it.

**macOS.** The system ships an old Python for its own use. They should install a current
one from python.org or with Homebrew. The command is `python3` in either case. `python`
on its own may not exist, or may open something they do not want.

**Linux.** Usually already installed. Check with `python3 --version` in a terminal. They
are likely the least lost of the three, since they have a terminal.

**Chromebook, tablet, phone only.** No local install. Use an online editor such as
replit.com or the Python editor at python.org/shell. Perfectly workable, but tell them
the first session is easier on a real computer if they can borrow one.

---

## 1. What is a program, in one minute

Ask them what they think a program is, and let them answer before you say anything.

Then give them this, and stop.

A program is a list of instructions that the computer follows from top to bottom. The
computer has no judgement and no common sense. It does exactly the instructions, in
order, and gets confused in exactly the ways a very literal person would.

The reason that matters today is this. When code goes wrong, the computer did what it
was told. The job is not to convince it, or to try again, or to apologise. The job is to
find which instruction says something other than what you meant.

That single framing will carry them through every error in the next nine units.

## 2. Installing Python

Do this together, on their machine, with you watching rather than doing.

**Windows**

1. Go to python.org/downloads and click the big yellow download button.
2. Run the installer.
3. Tick "Add python.exe to PATH" at the bottom of the first screen. Do not skip
   this.
4. Click "Install Now".
5. When it finishes, open the Start menu, type `cmd`, and open Command Prompt.
6. Type this and press Enter.

```
python --version
```

They should see something like `Python 3.13.1`. If instead they see an error, or the
Microsoft Store opens, the PATH box was missed. Reinstall and tick it.

**macOS**

1. Go to python.org/downloads and get the macOS installer, or use Homebrew with
   `brew install python`.
2. Run the installer through to the end.
3. Open Terminal (press Cmd and space, type `terminal`).
4. Type this and press Enter.

```
python3 --version
```

**Linux**

Open a terminal and check.

```
python3 --version
```

If it is missing, it comes from the package manager, for example `sudo apt install
python3` on Debian family systems.

### The command name, once

Explain this briefly and do not belabour it. On Windows the command is `python`. On
macOS and Linux it is usually `python3`, because `python` used to mean the old version.
Anywhere below that says `python3`, use `python` on Windows.

## 3. The two ways to run Python

This distinction is worth ten minutes because it confuses people for weeks otherwise.

### The interactive shell

Type `python3` in the terminal, with no file name, and press Enter. The prompt changes
to `>>>`. This is a live conversation. Type an expression (anything that produces a
value), press Enter, see the answer immediately.

```
>>> 2 + 3
5
>>> "hello" + " world"
'hello world'
>>> 7 * 6
42
```

Ask them to use it as a calculator for two minutes. Really, as a calculator. Let them do
some arithmetic they actually need.

Two things to point out.

- There is no `>>>` in a file, ever. If they copy a line that starts with `>>>`
  into a file, it will be a `SyntaxError`. This happens constantly, so say it now.
- To leave, type `exit()` or press Ctrl+D. On Windows, press Ctrl+Z then Enter.

### Files

A file ending in `.py` is a program. You run it with the `python3` command followed by
the file name, and Python follows the instructions from the top and finishes.

```
python3 hello.py
```

Ask them which one they think is used for real programs. It is the file. The shell is
for quick experiments, and experienced programmers use it constantly, but every program
worth keeping is a file.

## 4. Installing an editor

**If they are nervous, use Thonny.** It is designed for exactly this situation. One
download, Python bundled inside, a Run button, and a simple view. Less capable later,
but it gets a beginner writing code in five minutes instead of thirty. Switching editor
after unit 03 is painless.

**Otherwise, use VS Code.** Get it from code.visualstudio.com, then install the official
Python extension from the Extensions panel on the left. The steps.

1. Open VS Code.
2. Click the Extensions icon in the left sidebar, the one made of four squares.
3. Search for `python`.
4. Install the one published by Microsoft.
5. Open the Terminal in VS Code with Ctrl and backtick, and check
   `python3 --version` works there too.

Two settings worth changing now. Turn on "Format On Save" and set the tab size to four
spaces. Both live in the settings search box.

Warn them about one thing. VS Code will offer to autocomplete and auto-import things
they have never heard of. Tell them to ignore all suggestions for now and type
everything by hand. Autocomplete is wonderful and it will hide exactly the syntax they
need to learn.

## 5. The first program

Have them make a folder called `python-work` somewhere sensible, like their home
directory or Documents. Everything from the course goes in there. Then create a new file
called `hello.py` inside it and type this, by hand, no pasting.

```python
print("Hello, world!")
```

Then, in the terminal, making sure they are in that folder, run it.

```
python3 hello.py
```

If they see `Hello, world!` then the whole session has succeeded. Nothing else today
matters as much as this.

### Things to try immediately

Have them change the message and run it again. Then ask them to add a second `print`
line and predict what the output will look like before running. The prediction matters
more than the result.

Then the punctuation experiments, one at a time, predicting first.

- What happens if you remove the closing bracket?
- What happens if you remove the closing quote?
- What happens if you remove both brackets entirely, as in `print "hello"`?
- What happens if you write `Print` with a capital P?

Each one is an error, and each error is the lesson. See step 7.

## 6. Comments

A comment is a note for humans. Python ignores it completely.

```python
# This is a comment. Python will not run this line.
print("But this line runs.")
```

In VS Code you can comment or uncomment a line with Ctrl and forward slash. On a Mac it
is Cmd and forward slash.

Why comments exist, in one sentence. Code says what happens, comments say why it
happens, and the why is the part that is invisible six months later.

Two warnings, because beginners overdo this in both directions.

```python
# this prints hello
print("hello")
```

That comment is noise. The code already said it. Do not write comments that repeat the
code.

```python
print("hello")
```

And this needs no comment either. The rule of thumb to give them. Comment when the
reason is not clear from reading it, for example when a number is odd on purpose for a
real reason.

```python
# Prices are in cents to avoid rounding errors with decimals
price = 1999
```

## 7. Reading an error, the first time

Do not skip this step. It is the actual lesson of unit 00.

Open [`broken.py`](/code/00-setup/broken.py), which contains a mistake on purpose. Have them run it. It will
fail. Then walk through the ritual from `instructor/debugging-with-beginners.md`.

1. Read the last line out loud. It names the error type and says what is wrong.
2. Read the line above it. It gives the file name and the line number.
3. Look at the caret `^` if there is one. It points at the exact column.
4. Go to that line in the code and read it aloud.
5. Form a guess.
6. Test the guess by fixing it and running again.

The specific wording to install. The bottom of the message tells you what, the middle
tells you where, and the top you can ignore for now.

Then point out something surprising about `broken.py`. The first line of it, the one
that prints "Line one", never runs. Not one instruction in the file runs, even though
the mistake is on the second line. A `SyntaxError` means Python read the whole file,
could not understand it, and refused to start. Compare that to a `NameError` later,
where the program starts and gets some of the way through. The error type tells you
which situation you are in, which is a large part of why reading the type first is worth
doing.

Then run the four punctuation experiments from step 5 with this ritual. They should read
each error out loud before fixing it. By the fourth one it will already feel routine,
and that is the whole point.

## 8. Closing

Ask them to do two things before they finish.

1. From a blank file, write a program that prints three lines. No looking at the
   old file.
2. Say out loud, in their own words, the difference between the `>>>` shell and a
   `.py` file.

Then ask what still feels fuzzy and write it down.

---

## Teaching notes for this unit

**If installation fights you, stop and fix it properly.** Do not move on with a
half-working environment because you are behind schedule. A student who cannot run their
own code has no course. If it takes the entire session, that is a successful session.
The concepts can wait a week.

**Resist teaching `print` properly today.** They will meet the full version in unit 01
with f-strings and multiple arguments (values you pass in when calling). Today
`print("something")` is enough, and adding more now just crowds out the installation.

**The four punctuation errors are the core content.** If you only have twenty minutes,
do the install, run `hello.py`, and do the error reading. That is the whole unit.

**Watch for the `>>>` copy.** It is very common. They type into the REPL, it works, then
they copy the whole thing including the prompts into a file and it explodes with a
`SyntaxError`. Now you know why.

**Let them keep the terminal open.** Beginners close it constantly and then cannot find
their folder again. Show them how to check where they are with `pwd` (Linux and macOS)
or `cd` with no arguments (Windows), and how to change directory with `cd foldername`.
Ten seconds, saves a lot of future confusion.

**Option 3 (triple-quoted strings) is a preview, not a lesson.** Do not spend time on it now.

**Preview of next unit.** They now have a way to run code. Next session they make it
store things and do arithmetic.
