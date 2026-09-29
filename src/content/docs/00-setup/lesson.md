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

**Goal for the session.** They run a file they wrote themselves, see output, and read
their first error message calmly.

**Time.** 45 to 60 minutes. Most of it is the error reading at the end, and that is the
part that matters.

**Prerequisites.** A working editor with Python in it. This is set up outside the course,
by you, before the session. Nothing in this unit explains how to install anything.

---

## Before you start

Assume the editor and Python already work. That is your job rather than the course's, and
by the time the student sits down it should be done.

Check three things before you begin, and fix them quietly rather than making a lesson out
of them.

1. **The Run button works.** Open any `.py` file and click it. If nothing happens, or the
   button is not there, stop and fix that first. Everything in the next nine units
   depends on this one button, and a student who cannot run their own code has no course.
2. **The console is somewhere they can find it.** You will point at it once in section 4.
   In VS Code it is the command palette, "Python: Start REPL", or Shift and Enter on a
   selected line. Show them where it is, do not describe it.
3. **Run uses the file's own folder.** Unit 08 reads data files that sit next to the
   scripts, and it is the one unit where a wrong working directory gives a
   `FileNotFoundError`. In VS Code, `python.terminal.executeInFileDir` is the setting.

A couple of things worth knowing if a machine gives trouble, since they come up.

- **Windows.** The install has a checkbox for adding Python to `PATH`. If it is missed,
  the editor cannot find Python at all, and the fix is a reinstall with the box ticked.
- **`python` versus `python3`.** On Windows the command is `python`, on macOS and Linux
  it is usually `python3`. You will not need either in this course, but you will see both
  in error messages and in anything the student finds online.
- **No local install possible.** A Chromebook or a tablet can use an online editor, but
  the Run button is the whole foundation here, so a borrowed laptop is much better.

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

## 2. The first program

Have them make a folder called `python-work` somewhere sensible, like their home
directory or Documents. Everything from the course goes in there. Then create a new file
called `hello.py` inside it and type this, by hand, no pasting.

```python
print("Hello, world!")
```

Now they click **Run**.

That is the whole of running a program, and it is worth saying out loud that this is the
part people worry about. There is no command to type, and no folder to keep track of.
The editor knows which file they are looking at and runs that one.

If they see `Hello, world!` then the session has already succeeded. Nothing else today
matters as much as this.

Two things to point out while it is on screen.

- The output appears somewhere specific, usually a panel at the bottom. Ask them to point
  at it. That panel is where every error message in this course will also appear.
- Running again runs the whole file again, from the top, with nothing remembered from
  last time. This is the single most important fact about how programs work, and they
  will rely on it constantly.

### Things to try immediately

Have them change the message and run it again. Then ask them to add a second `print`
line and predict what the output will look like before running. The prediction matters
more than the result.

Then the punctuation experiments, one at a time, predicting first.

- What happens if you remove the closing bracket?
- What happens if you remove the closing quote?
- What happens if you remove both brackets entirely, as in `print "hello"`?
- What happens if you write `Print` with a capital P?

Each one is an error, and each error is the lesson. See section 6.

## 3. The console, and why files are different

Show them the console now, and let them play with it for two minutes. Really, as a
calculator. Let them do some arithmetic they actually need.

It shows `>>>` where they type, and it answers immediately.

```
>>> 2 + 3
5
>>> "hello" + " world"
'hello world'
>>> 7 * 6
42
```

The distinction to leave them with, in one sentence. The console is for trying something
small and getting an answer now, and a file is for anything worth keeping. The console
forgets everything when it closes, which is exactly why finished work goes in a file.

Two things to point out.

- There is no `>>>` in a file, ever. If they copy a line that starts with `>>>` into a
  file, it will be a `SyntaxError`. This happens constantly, so say it now.
- In the console, the answer appears without being asked for. In a file, nothing appears
  unless you `print` it. This is the first thing that will confuse them in unit 01, so
  plant it now.

## 4. Comments

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

## 5. Reading an error, the first time

Do not skip this step. It is the actual lesson of unit 00.

Open [`broken.py`](/code/00-setup/broken.py), which contains a mistake on purpose. Have them run it. It will
fail. Then walk through the ritual from
`src/content/docs/instructor/debugging-with-beginners.md`.

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

Then run the four punctuation experiments from section 2 with this ritual. They should
read each error out loud before fixing it. By the fourth one it will already feel
routine, and that is the whole point.

## 6. Closing

Ask them to do two things before they finish.

1. From a blank file, write a program that prints three lines. No looking at the
   old file.
2. Say out loud, in their own words, the difference between the console and a `.py`
   file.

Then ask what still feels fuzzy and write it down.

---

## Teaching notes for this unit

**Everything here rests on the Run button.** If it is broken, fix it before teaching
anything, even if that takes the whole session. Say so out loud rather than making the
student feel behind.

**Do not let them learn the habit of fighting the environment.** The reason this unit
uses the Run button rather than a command is that a beginner typing `python3 file.py`
gets a folder error sooner or later, and the error looks nothing like the mistake they
made. The editor removes that entire category of problem.

**Resist teaching `print` properly today.** They will meet the full version in unit 01
with f-strings and multiple arguments (values you pass in when calling). Today
`print("something")` is enough, and adding more now just crowds out the running and the
error reading.

**The four punctuation errors are the core content.** If you only have twenty minutes,
run `hello.py`, do the four experiments, and read `broken.py`. That is the whole unit.

**Watch for the `>>>` copy.** It is very common. They type into the console, it works,
then they copy the whole thing including the prompts into a file and it explodes with a
`SyntaxError`. Now you know why.

**Console versus file, said once and repeated.** Nothing appears in a file unless you
`print` it, and a program starts from the top every time. Those two facts explain most of
the confusion in unit 01.

**Option 3 (triple-quoted strings) is a preview, not a lesson.** Do not spend time on it now.

**Preview of next unit.** They can run a file. Next session they make it store things and
do arithmetic, and they meet the difference between showing an answer and keeping it.
