---
title: Debugging with beginners
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
The goal is not that your students avoid errors. It is that they stop being afraid of
them. That happens through repetition, in every session, from the first one.

## The ritual

Do this every time any code fails, without exception, and make it the student's job
rather than yours.

1. **Read the last line out loud.** That is the error type and the message. For
   example, `NameError: name 'total' is not defined`.
2. **Read the second to last line out loud.** That is where it happened. File name
   and line number.
3. **Go to that line.** Read it out loud too.
4. **Look at the top of the traceback only if the last lines were not enough.**
   Ignore it otherwise. Beginners who read the top first get lost in frames they
   did not write.
5. **Say what the message means in plain words.** "It does not know what `total`
   is. So I must not have created it, or I spelled it differently."
6. **Form a hypothesis, then test it.** Print the thing. Check the spelling. Make
   the smallest change that would prove or disprove the idea.

Enforce the order. If they jump to guessing before reading the message, make them go
back and read it out loud. It feels pedantic for two sessions and then it is automatic
for life.

## The `^` marker

Modern Python points at the exact column with a caret in syntax errors.

```
  File "example.py", line 3
    if x > 5
            ^
SyntaxError: expected ':'
```

That caret is free information. Teach them to look for it, and to count it as part of
step 3.

## The error type is a category, not a sentence

Help them build a small mental table of the errors they will actually meet. Write this
on paper together in unit 03 or 04 and stick it next to the laptop. It is worth updating
by hand as new errors appear.

```
SyntaxError        I typed something that is not valid Python at all
IndentationError   The spacing at the start of a line is wrong
NameError          I used a name that does not exist
TypeError          I used a value of the wrong kind for this operation
ValueError         The kind is right but the content is wrong
IndexError         I asked for a position that the list does not have
KeyError           I asked for a dictionary key that is not there
AttributeError     I asked a value to do something it cannot do
ZeroDivisionError  I divided by zero
```

The distinction between `TypeError` and `ValueError` confuses people. Useful framing.
`int("five")` fails because the content is wrong, and the content is a `ValueError`.
`"a" + 5` fails because the kinds do not match, and that is a `TypeError`.

## Print debugging, the honest version

`print()` is the right tool for most of the first nine units. Teach it properly rather
than apologetically.

Three patterns to install.

**Print the value before the line that fails.**

```python
value = input("Number: ")
print("value is", repr(value), "and its type is", type(value))
number = int(value)
```

`repr()` is the secret weapon here, because it shows you the invisible. Wrapping a value
in it reveals stray spaces and hidden newlines that `print` hides.

```python
print(repr("hello "))     # 'hello '  <- trailing space is now visible
```

**Print a label so you can tell which print fired.**

```python
print("A: starting")
print("B: inside the loop, i is", i)
print("C: finished")
```

When only `A` appears, you have just located the problem.

**Print inside a loop, but not too much.**

```python
for i in range(1000):
    if i < 5 or i > 995:
        print("i is", i)
```

## The smallest failing example

When something is broken inside a big program, help them cut it down. This is the skill
that separates people who stay stuck from people who get unstuck, and it has to be
taught explicitly.

The method. Copy the broken part into a fresh file. Delete everything unrelated. Delete
lines one at a time until removing one more would make the problem disappear. What is
left is the real problem. Then work on that.

Do this once, together, in unit 05 or 06. Students are often reluctant, because it feels
like going backwards. Point out that finding the problem in three lines is faster than
staring at forty.

## Rubbery duck debugging, but with you as the duck

When they ask you a question, make them explain the code first. Say "walk me through
what this does, line by line" and stay quiet.

A surprising amount of the time they answer their own question halfway through, which is
the ideal outcome. When they do not, their narration usually tells you precisely which
part of the model is wrong, which is much better than you guessing from the symptom.

## The questions to ask instead of giving the answer

Keep these loaded and rotate them.

- "What did you expect to happen, and what actually happened?"
- "What is in that variable right now? How could you find out in one line?"
- "Read me the error, out loud, bottom up."
- "Which line do you believe is the problem, and why that one?"
- "What is the smallest change that would tell us something?"
- "Has this worked before? What changed between then and now?"
- "Say that bit in English, forget the code, just describe it."

Note that none of these is "have you tried". "Have you tried" invites guessing. "What
did you expect" invites thinking.

## When to just tell them

There is a point past which not answering is unkind. Give the answer directly when any
of these is true.

- They have been stuck on the same thing for more than about ten minutes with no
  new hypothesis.
- The blocker is environmental rather than conceptual. A missing file, a wrong
  path, a typo in a filename that is genuinely hard to see.
- The concept pops up again later anyway and they will get more chances at it.
- They are visibly frustrated and close to deciding they are bad at this. That
  moment does real damage and is not worth any amount of discovery learning.

When you do tell them, do not simply fix it. Say what the problem was, why the message
pointed there, and what they could have checked. Then have them retype the fix
themselves.

## Deliberate error exercises

The most efficient way to remove error fear. Hand them working code with one change that
breaks it, and ask them to read the error and fix it without your help.

Good ones, roughly in order of difficulty.

1. Remove a closing bracket.
2. Change `==` to `=`.
3. Misspell a variable name on one line only, so the definition and use disagree.
4. Pass a string where a number is expected, as in `int("hello")`.
5. Use `range(5)` where the intended output was 1 through 5.
6. Delete a `return` and watch the caller receive `None`.
7. Indent a line one level too far.

There is a set of ready-made broken files for exactly this.

- `05-lists/code/list_traps.py` — five list mistakes, commented out one section at a
  time so the file still runs.
- `06-functions/code/broken_functions.py` — six function mistakes, including the one
  that produces no error at all.

Each is written to be worked through rather than read. Have them uncomment one section,
run it, read the error out loud, and predict the fix before making it.

## Do not let them restart the program to "see if it works now"

Running it again without changing anything teaches nothing and quietly reinforces the
idea that program behaviour is random. If they run it twice, ask what they expect to be
different on the second run. Usually the answer is nothing, which is the point.
