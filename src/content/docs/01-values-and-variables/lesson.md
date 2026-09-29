---
title: Unit 01 — Values and variables
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
**Files for this unit.** [`arithmetic.py`](/code/01-values-and-variables/arithmetic.py), [`fstrings.py`](/code/01-values-and-variables/fstrings.py), [`types.py`](/code/01-values-and-variables/types.py), [`variables.py`](/code/01-values-and-variables/variables.py)

These live in `public/code/01-values-and-variables/` in the repository, and the links above
open them as plain text. Every snippet the student needs is already inline in the
exercises, so the files are for the session itself, when you are both at the
keyboard.

**Goal for the session.** They can store a value in a variable, do arithmetic with it,
and print a sentence that includes it.

**Time.** One session of 60 to 90 minutes.

**Prerequisites.** Unit 00. They can run a `.py` file and read an error message.


---

## 0. Warm-up

Open `about_me.py` from last session and have them narrate it line by line, out loud.
Then ask them what the `#` does, and what happens if you remove it.

Then open the shell (`python3`) and ask them to work out `17 * 3` in it. That is the
bridge into today, since a variable is how you keep an answer around instead of losing
it.

## 1. The problem with printing only

Start here, because it motivates everything.

```python
print("The price is 20 dollars")
print("The tax is 3 dollars")
print("The total is 23 dollars")
```

Ask them what is wrong with this. Let them say it. The answer is that the numbers are
built into the text. If the price changes, you have to edit three lines and do the
arithmetic in your head.

Then show what they will be able to do by the end of the session.

```python
price = 20
tax = 3
total = price + tax
print(f"The total is {total} dollars")
```

Change `price` to `50`, run it, and the total updates itself. That is the whole point of
variables.

## 2. Variables

A variable is a name for a value. You make one with `=`.

```python
age = 25
name = "Ada"
```

The `=` does not mean "is equal to", which is the trap. It means "put the value on the
right into the name on the left". Read it as "age gets 25", not "age equals 25".

The value goes on the right, the name goes on the left. This is always true.

```python
25 = age      # NameError, and also nonsense
```

### Naming rules

Python is strict about some things and relaxed about others.

The rules, which are enforced.

- Letters, digits and underscores only.
- Cannot start with a digit. `1st_place` is invalid, `first_place` is fine.
- Case matters. `age` and `Age` are different variables.
- Cannot be one of Python's reserved words, like `if`, `for`, `class`, `def`.

The usual ways, which are not enforced but everyone follows.

- Lowercase with underscores between words, called snake case. `total_price`
  rather than `totalPrice` or `TotalPrice`.
- Descriptive. `total_price` rather than `tp` or `x`.
- Do not use names that already mean something, like `list`, `sum`, `str`, `max`.
  Python will allow it and then behave strangely later.

Ask them to name a variable that holds a person's first name, badly, then well. Then
have them do the same for the number of minutes in an hour.

### Assignment is a moment in time

This is the idea students most often miss.

```python
score = 10
score = 20
print(score)
```

What prints? Ask them first. It prints `20`, because assignment replaces whatever was
there. The variable holds one value at a time, and it holds the most recent one.

Then this, which looks like an equation but is not.

```python
score = 10
score = score + 5
print(score)
```

In maths, `x = x + 5` is impossible. Here it means "work out `score + 5` first, then
store the result back into `score`". So it prints `15`.

Have them predict first, then run. Then ask them what would happen with `score = score +
5` written twice in a row. That is a good prediction exercise.

Shortcut for this pattern, since it comes up constantly.

```python
score = 10
score += 5     # same as score = score + 5
print(score)   # 15
```

Also `-=`, `*=`, `/=`. Show them but do not drill them.

## 3. The basic types

Open [`types.py`](/code/01-values-and-variables/types.py) and work through it. The four types they need now.

```python
age = 25              # int, a whole number
height = 1.75         # float, a number with a decimal point
name = "Ada"          # str, text
is_student = True     # bool, either True or False
```

Point out that `1.75` has no units and no meaning on its own. The type is only about
what kind of value it is.

Booleans (values that are True or False) are capitalised. `true` and `false` lowercase
are `NameError`s, which catches everyone at least once.

### Checking the type

`type()` tells you what kind of value something is.

```python
age = 25
print(type(age))        # <class 'int'>
```

The output `<class 'int'>` is ugly but readable. Ask them to do this for the number `2`
and the number `2.0` and see whether they agree.

```python
print(type(2))     # int
print(type(2.0))   # float
print(type("2"))   # str
```

Those three lines are worth a minute of silence to let the distinction land. The digit
two, the decimal two, and the quoted two are three different kinds of thing.

### Mixing types

```python
print(2 + 3)        # 5, both ints, answer is int
print(2 + 3.0)      # 5.0, one float, answer is float
print("2" + "3")    # 23, both strings, they join
```

The third one is the one to spend time on. Adding two strings glues them together. It
does not do maths. This is exactly why `input()` in unit 02 will cause so much trouble.

And this, which fails.

```python
print("2" + 3)      # TypeError
```

Have them run it and read the error. It will say something like `can only concatenate
str (not "int") to str`. Ask them why Python refuses. Because it really cannot tell
whether you meant `23` or `5`, and it would rather complain than guess. That is a
reasonable design and worth saying, because it reframes the error as Python being
careful rather than Python being difficult.

## 4. Arithmetic

Open [`arithmetic.py`](/code/01-values-and-variables/arithmetic.py).

The operators (symbols that do something to values).

```python
print(10 + 3)    # 13   addition
print(10 - 3)    # 7    subtraction
print(10 * 3)    # 30   multiplication
print(10 / 3)    # 3.3333333333333335   division
print(10 // 3)   # 3    floor division, how many whole times
print(10 % 3)    # 1    remainder, what is left over
print(10 ** 3)   # 1000 ten cubed
```

Ask them to explain in English what `//` and `%` do. The honest answer. `//` asks "how
many times does 3 fit into 10, ignoring the leftover bits" and `%` asks "what is left
over after you take those out".

Have them work out `17 // 5` and `17 % 5` on paper before running. Then check on a
calculator. Then use them for something real, which is the next point.

### `%` is really useful, not just an exam topic

Two uses they will meet again in unit 04.

```python
print(10 % 2)    # 0
print(11 % 2)    # 1
```

A number is even if `n % 2` is `0`. That is how you test for even numbers, and it is the
standard exercise in every beginner course for a reason.

```python
minutes = 137
print(minutes // 60)   # 2 hours
print(minutes % 60)    # 17 minutes left
```

Splitting a total into hours and minutes, or dollars and cents, or days and hours, is
the same pattern every time. Have them do this one for `total_seconds = 5000` and check
the answer.

### Order of operations

```python
print(2 + 3 * 4)      # 14, not 20
print((2 + 3) * 4)    # 20
```

Multiplication before addition, same as maths. The advice to give them. Use brackets
whenever there is any doubt, even when they are not strictly needed. Being clear beats
being short here, and nobody has ever been criticised for too many brackets in an
expression, which just means anything that produces a value.

### Division gives a float, always

```python
print(10 / 2)     # 5.0, not 5
```

Ask them to predict this before running, and to say why they think it comes out with a
decimal point. The answer is that `/` always gives a float, even when the division is
exact, because Python does not want to surprise you with a decimal later. If you want a
whole number, use `//`.

### Very big and very small numbers

Not important, but fun and quick.

```python
print(2 ** 100)
```

Python handles huge integers that other languages would choke on. Worth ten seconds of
appreciation.

And the caution, shown once in unit 01 and never taught.

```python
print(0.1 + 0.2)     # 0.30000000000000004
```

Do not explain floating point. Just say decimals are not stored exactly, so do not be
surprised by a tiny tail of digits, and do not compare decimal numbers for exact
equality. Move on.

## 5. f-strings

Open [`fstrings.py`](/code/01-values-and-variables/fstrings.py). This is the bit they will use every single session from now on,
so give it proper time.

Putting a variable into text. First the painful way, so they appreciate the good one.

```python
name = "Ada"
age = 36
print("My name is " + name + " and I am " + str(age))
```

That works, and it is awful. The `str()` is needed because you cannot glue a number onto
a string, and the quotes and plus signs get tangled as soon as there is more than one
variable.

Now the good way.

```python
name = "Ada"
age = 36
print(f"My name is {name} and I am {age}")
```

One `f` before the opening quote, and braces around the variable names. That is the
whole syntax.

Have them retype the painful version as an f-string themselves. Comparing the two side
by side is the lesson.

### Braces contain expressions, not just names

This is the part that makes f-strings powerful.

```python
price = 20
quantity = 3
print(f"{quantity} items at {price} dollars each is {price * quantity} dollars")
```

Anything inside the braces gets calculated. So this works.

```python
print(f"Half of 100 is {100 / 2}")
```

### Formatting decimals

Useful and short.

```python
price = 19.9876
print(f"{price:.2f}")
```

That prints `19.99`, rounded to two decimal places. The `.2f` means "two digits after
the point, as a fixed point number". Have them try `.0f`, `.1f`, `.4f` and predict each.
They will use this the moment they do anything with money.

### Things to warn them about

The `f` must be right before the quote, touching it. `f "hello"` with a space is a
`SyntaxError`. And a quote without the `f` is just text, so `"{name}"` prints the braces
literally. Both are instant feedback, so let them hit them.

Missing braces is the silent one.

```python
print(f"My name is name")
```

This prints `My name is name`. No error, just wrong. Worth doing on purpose once so they
know what it looks like.

## 6. Putting it together

Build this live with them, not for them. A small receipt.

```python
item = "coffee"
price = 4.5
quantity = 3
total = price * quantity

print(f"{quantity} x {item}")
print(f"Total: {total:.2f}")
```

Then change `quantity` and rerun, and note that only one number changed in the code and
everything else followed.

Then ask them to add a `tax` variable of 0.15 and print the total with tax. Let them
struggle with it for a moment before helping. The multiplication is the easy part. The
interesting decision is whether to overwrite `total` or make a new variable, and either
answer is fine, so ask them which they prefer and why.

---

## Teaching notes for this unit

**Do not rush variables, even though it looks easy.** Everything for the next eight
units rests on the idea that a name points at a value and the value can be replaced.
Students who are shaky here will be shaky everywhere.

**The `=` versus `==` distinction belongs in unit 03,** but if they ask now, say "two
equals signs asks a question, one gives an answer", and move on.

**Types are the thing to over-invest in.** The `int` versus `float` versus `str`
distinction, and specifically that `"2"` is not `2`, is the root cause of a large
fraction of beginner bugs. Give `type()` a lot of time. From now on, whenever something
confusing happens, the first question is "what type is it, and how could you check?"

**`%` deserves real time.** It looks like a useless bit of arithmetic trivia and it is
actually the tool for even and odd, for hours and minutes, for every "every nth item"
pattern, and for the classic beginner exercise of converting a number of seconds into
hours, minutes and seconds.

**Float formatting with `.2f` is worth it immediately.** If they are going to do
anything with money in their exercises, teach it here so their answers look like `19.99`
rather than `19.987600000000001`.

**If they are finding it easy, skip ahead to unit 02 quickly** and let them do the
stretch exercises in their own time. Do not add new material to unit 01 to fill time.

**Preview of next unit.** They can store values and print them. Next session they get
values from the user, which means meeting text as something you can inspect and take
apart, and meeting the single most common beginner bug in Python.
