# Errors, and what to do about them

Read the error from the bottom up, out loud. The last line says what went wrong. The
line above it says where. The top of the message you can ignore for now.

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

Look for a missing colon, a missing bracket or quote, or a typo in a keyword. The
caret `^` points at the exact spot, which is often not where you would guess, so
read what it says.

Common causes.

- Missing `:` at the end of an `if`, `for`, `while` or `def` line
- A bracket or quote that was never closed
- A curly quote `"` that came from a chat app or word processor
- `print "hello"` without brackets, which is Python 2 syntax

Nothing ran, which means the mistake could be anywhere in the file and you will only
see one at a time. Fix, run, look again.

---

## IndentationError

```
IndentationError: expected an indented block
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

## TypeError

```
TypeError: can only concatenate str (not "int") to str
TypeError: unsupported operand type(s) for +: 'int' and 'str'
TypeError: 'NoneType' object is not subscriptable
```

The right operation, the wrong kind of value.

- `"5" + 5` — you cannot add text to a number. Convert it with `int()` or `str()`
- `len(5)` — `len` needs something with a length
- `something[0]` where `something` is `None` — that usually means a function forgot
  its `return`

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
```

The right kind of value, but the content is wrong. `int("hello")` is a `ValueError`
because `hello` is not a number.

Common causes.

- The user typed something that is not a number
- `int("1.75")` — `int` will not silently drop the decimal, use `float`
- An empty string, usually from a blank line in a file
- `x in list` or `list.remove(x)` where `x` is not there

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

Positions start at zero, so the last valid position is `len(list) - 1`, and the last
item is `list[-1]`. An attempt to read `list[len(list)]` is one too far.

It also happens when you loop over a list and remove items as you go, because the
positions shift underneath you. Do not change a list while looping over it.

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

## RecursionError

```
RecursionError: maximum recursion depth exceeded
```

A function called itself too many times, usually because there is no case that stops
it. If you are using recursion and see this, check that your stopping condition is
reachable.

---

## The general method

1. Read the last line out loud. That is the error type and the message.
2. Read the line above it. That is the file and line number.
3. Go to that line and read it out loud.
4. Say what the message means in plain words.
5. Form a guess, then test it. Print the value. Check the type. Change one thing.
6. If the line looks fine, look at the lines above it. Errors often come from
   earlier code, and the failing line is just where it finally showed up.

And two things that are always worth trying.

```python
print(repr(value))     # see exactly what is there, including hidden spaces
print(type(value))     # check it is the kind of thing you think it is
```
