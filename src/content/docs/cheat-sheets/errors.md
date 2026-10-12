---
title: Errors, and what to do about them
---
Read the error from the bottom up, out loud. The last line says what went wrong.
Above it is the line of code. Above that is a line that starts with `File`, which
gives the file name and the line number, so it says where. If there are several
`File` lines, read the one nearest the bottom first.

Here is a runtime error (one that happens while the program is running).

```
Traceback (most recent call last):
  File "example.py", line 5, in <module>
    print(total + "5")
          ~~~~~~^~~~~
TypeError: unsupported operand type(s) for +: 'int' and 'str'
```

The last line is the error. The line of code is above it, and the `File` line with
`line 5` is above that. The `~` and `^` marks only underline the part of the line that
failed. The word `Traceback` at the top you can ignore for now.

---

## SyntaxError

The file is not valid Python, so nothing in it runs. Not even the lines above the
mistake.

```
  File "example.py", line 3
    if x > 5
            ^
SyntaxError: expected ':'
```

For a SyntaxError the code line and a `^` mark come right above the last line, and
the `File` line is above those. The `^` (the caret) points at the spot where Python
got confused. That is often not where you would guess, so read what the message says.

Look for a missing colon, a missing bracket or quote, or a typo in a keyword.

Common causes.

- Missing `:` at the end of an `if`, `for`, `while` or `def` line
- A bracket or quote that was never closed
- A curly quote such as `“` or `”` (the real characters, U+201C and U+201D) instead of
  a plain `"`. They come from chat apps and word processors, and they look almost the
  same as the plain one. The message says `invalid character '“' (U+201C)`
- `print "hello"` without brackets. That is Python 2 syntax. Python 2 is a very old
  version of Python, and you will see it in old tutorials

Nothing ran, which means the mistake could be anywhere in the file and you will only
see one at a time. Fix, run, look again.

---

## IndentationError

```
IndentationError: expected an indented block after 'if' statement on line 2
IndentationError: unexpected indent
```

The spacing at the start of a line is wrong.

- `expected an indented block` means the line after a `:` is not indented
- `unexpected indent` means a line is indented when it should not be

Fix it by making the indentation match the structure. Four spaces per level, and if
you see a `TabError` instead, the file has a mix of tabs and spaces, which usually
means it was edited in two different editors.

---

## NameError

```
NameError: name 'totle' is not defined
```

You used a name that does not exist, at least not with that spelling.

Check these in order.

1. Is it a typo? Compare the definition and the use, character by character.
2. Is the capitalisation right? `Print` and `print` are different names.
3. Was it ever assigned? Using a variable before creating it is a `NameError`.
4. Is it inside a function that cannot see it? Variables inside a function are local.

---

## UnboundLocalError

```
UnboundLocalError: cannot access local variable 'x' where it is not associated with a value
```

Inside a function you used a variable before giving it a value. This also happens when
you assign to a name inside a function, because then Python treats that name as local
for the whole function, even on the lines above the assignment.

Give the variable a value before the line that reads it, or pass it in as a parameter.

---

## TypeError

```
TypeError: can only concatenate str (not "int") to str
TypeError: unsupported operand type(s) for +: 'int' and 'str'
TypeError: 'NoneType' object is not subscriptable
TypeError: 'int' object is not iterable
TypeError: greet() takes 1 positional argument but 2 were given
TypeError: greet() missing 1 required positional argument: 'name'
```

The right operation, the wrong kind of value.

- `"5" + 5`: you cannot add text to a number. Convert it with `int()` or `str()`
- `len(5)`: `len` needs something with a length
- `something[0]` where `something` is `None`: that usually means a function forgot
  its `return`
- `for n in 5:`: a loop needs something it can walk through, like a list or a
  string. Did you mean `range(5)`?
- `takes 1 positional argument but 2 were given` (or `missing 1 required`): the number
  of values you passed does not match the number of parameters. Count the values in
  the call and the names in the `def` line

The first thing to do with a `TypeError` is print the types.

```python
print(type(a), type(b))
```

Almost every time, one of them is a string when you expected a number. `input()`
gives text, and so does everything read from a file.

---

## ValueError

```
ValueError: invalid literal for int() with base 10: 'hello'
ValueError: could not convert string to float: '1,5'
ValueError: list.remove(x): x not in list
```

The right kind of value, but the content is wrong. `int("hello")` is a `ValueError`
because `hello` is not a number.

Common causes.

- The user typed something that is not a number
- `int("1.75")`: `int` will not silently drop the decimal, use `float`
- An empty string, usually from a blank line in a file
- `items.remove(x)` or `items.index(x)` where `x` is not in the list. (Plain `x in items`
  does not fail. It just gives `False`)

This is the one to handle with `try` and `except`, because bad input from a user is
expected rather than a bug.

---

## KeyError

```
KeyError: 'colour'
```

A dictionary key that is not there. The message names the key, which makes this one
of the easier errors to fix.

Check the spelling, and check whether the key was ever added. If a missing key is a
normal situation rather than a mistake, use `.get()` with a default instead of
square brackets.

---

## IndexError

```
IndexError: list index out of range
```

You asked for a position the list does not have.

Positions start at zero, so the last valid position is `len(items) - 1`, and the last
item is `items[-1]`. An attempt to read `items[len(items)]` is one too far.

It can also happen in a `for i in range(len(items))` loop if the loop removes items
as it goes, because the list gets shorter while `i` keeps growing.

A plain `for item in items` loop that removes items does not give an error. It
quietly skips some of the items, because the positions shift underneath it. Either way,
do not change a list while looping over it.

---

## AttributeError

```
AttributeError: 'str' object has no attribute 'append'
AttributeError: 'NoneType' object has no attribute 'lower'
```

You asked a value to do something it cannot do.

The first example means you called a list method on a string. The second usually
means a variable is `None`, often because a function forgot to return something.

Print the value and its type, and check the method name is spelt right.

---

## ModuleNotFoundError

```
ModuleNotFoundError: No module named 'randon'
```

Python could not find the module you asked to `import`. Check the spelling first. If
the name is your own file, check that the file is in the same folder as the program,
that its name ends in `.py`, and that you wrote the name without the `.py`.

---

## FileNotFoundError

```
FileNotFoundError: [Errno 2] No such file or directory: 'data.txt'
```

The file is not where the program is looking. This is almost never a code problem.

The message gives the exact path that was tried. Either the file is somewhere else,
or the program is running from a different folder than you think. Check where the
file actually is, and either move it or give the full path.

---

## ZeroDivisionError

```
ZeroDivisionError: division by zero
```

Something divided by zero. This is often a value you did not expect to be zero, so
print the divisor right before the division rather than assuming.

Very common in an average calculation where the count turns out to be zero.

---

## JSONDecodeError

```
json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
```

You tried to load something that is not valid JSON. In practice this is almost always
an empty file, usually because a program was interrupted before it wrote anything.

`JSONDecodeError` is a kind of `ValueError`, so `except ValueError` catches it too.

---

## EOFError

```
EOFError: EOF when reading a line
```

`input()` was called, but there was nothing to read. This happens when a program that
asks questions is run somewhere that cannot take typing, or when the input has ended.
Run the program with the Run button in your editor, where you can type an answer.

---

## KeyboardInterrupt

```
KeyboardInterrupt
```

This is not a mistake in your code. It is what you see after you stop a running
program with the Stop button or with `Ctrl` and `C`. If your program never stopped on
its own, look for a `while` loop whose condition never becomes false.

---

## RecursionError

```
RecursionError: maximum recursion depth exceeded
```

A function called itself too many times, usually because there is no case that stops
it. You will only meet this if you try the optional exercise 6.19. Check that the
stopping condition can be reached.

---

## The general method

1. Read the last line out loud. That is the error type and the message.
2. Read the line of code above it, then the `File ... line N` line above that. The
   `File` line says where. With several `File` lines, start with the one nearest the
   bottom.
3. Go to that line in your file and read it out loud.
4. Say what the message means in plain words.
5. Form a guess, then test it. Print the value. Check the type. Change one thing.
6. If the line looks fine, look at the lines above it. Errors often come from
   earlier code, and the failing line is just where it finally showed up.

And two things that are always worth trying.

```python
print(repr(value))     # see exactly what is there, including hidden spaces
print(type(value))     # check it is the kind of thing you think it is
```

---

## When you are stuck

Three ways to print, which find most problems.

```python
print("value is", repr(value), "and its type is", type(value))   # look at one value
print("A: before the loop")                                      # which line did run?
print("B: inside the loop, i is", i)
```

For a long loop, print only a few passes, so the screen stays readable.

```python
for i in range(1000):
    if i < 5 or i > 995:
        print("i is", i)
```

Cut it down. If a big program is broken and you cannot see why, copy it into a new
file. Delete lines that have nothing to do with the problem, one at a time, and run
it after each one. Stop when deleting one more line makes the problem go away. What
is left is the real problem, and it is often only three or four lines. Finding it
there is faster than staring at forty lines.

Do not run the program again without changing anything. It will do the same thing
again. Change one thing first, and say what you expect to be different.

Know when to stop. If you have been stuck on the same thing for about ten minutes
and have no new idea to try, take a break or look for help. Search for the exact last
line of the error, in quotes, plus the word `python`. Read the answer, then close it
and type the fix yourself. If you are close to deciding that you are bad at this,
that is a good moment to stop for the day. The problem will look smaller tomorrow.
