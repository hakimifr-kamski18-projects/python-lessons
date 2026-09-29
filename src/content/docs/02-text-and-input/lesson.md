---
title: Unit 02 — Text and input
sidebar:
  hidden: true
pagefind: false
prev: false
next: false
---
**Files for this unit.** [`conversation.py`](/code/02-text-and-input/conversation.py), [`input_demo.py`](/code/02-text-and-input/input_demo.py), [`methods.py`](/code/02-text-and-input/methods.py), [`strings.py`](/code/02-text-and-input/strings.py)

These live in `public/code/02-text-and-input/` in the repository, and the links above
open them as plain text. Every snippet the student needs is already inline in the
exercises, so the files are for the session itself, when you are both at the
keyboard.

**Goal for the session.** They can ask the user a question, get an answer, convert that
answer to a number when they need to, and do basic surgery on text.

**Time.** One to two sessions. The `input()` type problem deserves its own real time and
often needs revisiting next session.

**Prerequisites.** Unit 01. Variables, types, f-strings.


---

## 0. Warm-up

Open [`fstrings.py`](/code/02-text-and-input/fstrings.py) from unit 01, or their own 1.6 solution, and have them narrate
it. Then ask them, without looking, to write a line that prints a variable inside a
sentence.

Then a quick prediction. What does `10 / 4` give, and why is it not `2.5` written as
`2`? That is a reminder about types, which is exactly today's theme.

## 1. Asking the user something

The new thing is `input()`.

```python
name = input("What is your name? ")
print(f"Hello, {name}!")
```

Note the space at the end of the prompt string. Without it, the cursor sits against the
question mark and the typing looks cramped. Small thing, they will notice it now and be
glad later.

Have them run it and type their name. Then have them read the code and say what they
think `input()` does. The answer is that it stops the program, shows the prompt, waits
for the user to type something and press Enter, and then hands back what they typed, as
a value.

Key point. It hands back a **value**, which they then store in a variable. That is why
this fails.

```python
input("What is your name? ")
```

The program asks, takes the answer, and throws it away, because there is no variable to
put it in. Have them run it and see. Then add `name = ` in front and run again to see
the difference.

### The prompt is optional

```python
name = input()
```

That works too, and just shows an empty line. Tell them to always use a prompt, because
a program sitting silently waiting with no message is confusing for the human using it.

## 2. The big problem. `input()` always gives text

This is the most important ten minutes of the unit. Do not shortcut it.

Open [`input_demo.py`](/code/02-text-and-input/input_demo.py) and run the number example.

```python
age = input("How old are you? ")
print(f"Next year you will be {age + 1}")
```

Have them type a number and run it. It fails.

```
TypeError: can only concatenate str (not "int") to str
```

Now do the ritual. Read the last line out loud. Then ask them what they think it means.
Then, crucially, have them find out rather than being told. Add this line.

```python
print(type(age))
```

It prints `<class 'str'>`. Whatever the user typed, even if it was `25`, came back as
text.

Why this is so, and it is worth one sentence of motivation. Everything a user types is
characters. There is no concept of a number in a text field. If the user types `25`,
that is the character `2` followed by the character `5`, which is exactly what `"25"`
is.

The fix is to convert it.

```python
age = int(input("How old are you? "))
print(f"Next year you will be {age + 1}")
```

Now it works.

### The three conversions

```python
int("25")       # 25, a whole number
float("1.75")   # 1.75, a decimal number
str(25)         # "25", text
```

Have them try these in the shell, including the failures.

```python
int("hello")
int("1.75")
float("25")
```

The first fails with `ValueError`, because `hello` is not a number and there is no
sensible way to convert it. The second also fails, and this surprises people, because
`int()` does not want to guess what to do with the `.75`. It refuses to silently round.
The third succeeds and gives `25.0`.

That second one is worth dwelling on. If a user types `1.75` where a whole number was
expected, `int()` will not quietly throw away the decimal. Use `float()` when the input
might have a decimal point, and `int()` only when you are certain it does not.

### The safe pattern

Give them this shape and have them use it from now on.

```python
age_text = input("How old are you? ")
age = int(age_text)
```

Two lines rather than one, and much easier to debug. When something goes wrong, and it
will, they can print `age_text` and see exactly what the user typed, including stray
spaces, before the conversion happened.

The one-liner `int(input("..."))` is fine once they are comfortable, and it is what
everyone writes eventually. Introduce it as a shorthand, not as the default.

### Worth showing, because it will cause problems for them

Conversions do not always go the way they expect.

```python
print(int("25"))       # 25
print(int(" 25 "))     # 25, Python is forgiving about surrounding spaces
print(int("25abc"))    # ValueError
print(int("2.0"))      # ValueError, no, really
print(int("-25"))      # -25
print(int(""))         # ValueError, empty text is not a number
```

## 3. Text as a thing you can inspect

Open [`strings.py`](/code/02-text-and-input/strings.py).

A string is a sequence (something with items in an order) of characters, and Python lets
you count and pick them out.

```python
word = "Python"
print(len(word))       # 6
print(word[0])         # P
print(word[5])         # n
print(word[-1])        # n, counting from the end
```

Ask them to predict `word[6]` before running it. It is an `IndexError`, because
positions start at zero and go up to `len - 1`. Then ask what `word[-1]` is, and show
that negative positions count backwards from the end. `word[-2]` is `o`.

The sentence to repeat. The first character is at position zero. Not one.

### Slicing (a piece cut out)

Taking a piece of a string.

```python
word = "Python"
print(word[0:3])     # Pyt, positions 0, 1, 2
print(word[2:5])     # tho
print(word[:3])      # Pyt, from the start
print(word[3:])      # hon, to the end
```

The rule, and it is the thing that trips everyone. Slicing includes the start position
and stops **before** the end position. So `word[0:3]` gives three characters, positions
0, 1 and 2.

Ask them to predict `word[1:1]` (empty) and `word[0:100]` (the whole thing, no error).
That second one is really useful, since going past the end of a slice is allowed and
going past the end of an index (a position, starting at 0) is not.

### Strings cannot be changed in place (changed directly, without a copy)

```python
word = "Python"
word[0] = "J"        # TypeError
```

Have them run it. The message says something about `'str' object does not support item
assignment`. Strings are immutable (cannot be changed), meaning once made, they do not
change. You make a new one instead.

```python
word = "J" + word[1:]
print(word)          # Jython
```

That is enough for now. The deeper consequences come up with lists in unit 05, where
they will find that lists can be changed in place and strings cannot.

## 4. The methods

Open [`methods.py`](/code/02-text-and-input/methods.py). This is a big block of new material, so go slowly and let them
try each one rather than reading them all.

A method is a function that belongs to a particular value. You call it with a dot.

```python
name = "ada lovelace"
print(name.upper())        # ADA LOVELACE
print(name.title())        # Ada Lovelace
print(name.capitalize())   # Ada lovelace
```

Now the crucial thing, which is the same lesson as the immutability point above.

```python
name = "ada lovelace"
name.upper()
print(name)                # still "ada lovelace"
```

Nothing happened. `upper()` gives you back a **new** string and leaves the original
alone. Have them predict the second print before running it, because the surprise is the
lesson.

```python
name = name.upper()
print(name)                # ADA LOVELACE
```

Assign it back if you want to keep the change. This pattern, where a method returns a
new value instead of modifying the original, is everywhere in Python, and students who
miss it will spend a lot of time confused about why "nothing happened".

### The ones they will actually use

```python
text = "  Hello World  "

text.strip()               # "Hello World"  removes spaces from both ends
text.lower()               # "  hello world  "
text.upper()               # "  HELLO WORLD  "
text.replace("World", "Python")   # "  Hello Python  "
```

`strip()` is the one to emphasise, because it pairs with `input()`. Users accidentally
type trailing spaces constantly, and a name with a trailing space will fail an equality
check in unit 03 in a way that is almost impossible to see.

```python
answer = input("Continue? ")     # user types "yes "
if answer == "yes":              # False! there is a space on the end
```

Show them the fix.

```python
answer = input("Continue? ").strip()
```

`repr()` is the tool for seeing this, and they met it in the debugging guide.

```python
answer = input("Continue? ")
print(repr(answer))     # 'yes '   <- the space is now visible
```

### Splitting and joining

```python
sentence = "the quick brown fox"
words = sentence.split()
print(words)               # ['the', 'quick', 'brown', 'fox']
print(len(words))          # 4
```

`split()` with nothing in the brackets splits on any whitespace (spaces, tabs and blank
lines). With a character in the brackets, it splits on that.

```python
data = "10,20,30"
print(data.split(","))     # ['10', '20', '30']
```

Tell them what the square brackets mean, briefly. That is a list, and it is unit
05. For now, just know that `split()` gives you several values at once in a box,
and `len()` counts them.

And the reverse.

```python
words = ["the", "quick", "brown", "fox"]
print(" ".join(words))            # the quick brown fox
print("-".join(words))            # the-quick-brown-fox
print(", ".join(words))           # the, quick, brown, fox
```

`join()` is the one that looks backwards at first. The separator goes before the dot,
and the list goes inside. Say this out loud twice. It is a common sticking point.

### Asking questions about a string

```python
text = "hello world"

print(text.startswith("hello"))   # True
print(text.endswith("world"))     # True
print(text.count("l"))            # 3
print(text.find("world"))         # 6
print("world" in text)            # True
print("xyz" in text)              # False
```

`find()` gives the position, or `-1` if it is not there, which is a quietly annoying
design decision since `-1` is a valid position from the end. Tell them to prefer `in`
when they only want to know whether something is there.

`in` is worth highlighting. It reads like English and they will use it constantly.

### Methods return new strings, so you can chain

```python
messy = "  HELLO world  "
print(messy.strip().lower().title())     # Hello World
```

Each method hands back a string, so you can call the next method on the result
immediately. Ask them to trace this one left to right out loud. Strip first, then lower,
then title. The order matters, and swapping `lower` and `title` changes the result.

## 5. Putting it together

Open [`conversation.py`](/code/02-text-and-input/conversation.py). Build it with them, line by line, not as a block.

A small program that asks for a name and a birth year and says something back.

```python
name = input("What is your name? ").strip()
birth_year = int(input("What year were you born? "))

age = 2026 - birth_year

print(f"Hello {name.title()}!")
print(f"You will turn {age} this year.")
```

Then have them extend it. Ask for a favourite colour and include it. Ask for two numbers
and print the sum. Each addition is a chance to decide whether the answer needs
converting, which is the judgement call this unit is really about.

The question to ask repeatedly. "Is this a number or is this text, and what does it need
to be?" That question is worth more than any amount of explanation.

---

## Teaching notes for this unit

**The `input()` type problem is the whole unit.** Everything else is useful, but this is
the thing they will trip over for weeks if it does not land. Spend the time. Make them
find `type(age)` themselves rather than telling them.

**Do not introduce `try` and `except` here.** When `int()` fails on `"hello"`, the
correct move is to let it crash and read the `ValueError`, and to say "we will learn how
to handle this gracefully in unit 08". Handling bad input properly is a unit 08 topic
and doing it now would bury the important `input()` lesson.

**`strip()` pairs with `input()` and saves enormous pain later.** If they learn one
thing from the string methods, make it `strip()` on input. Almost every mysterious "but
it should be equal" bug in unit 03 comes from an invisible trailing space.

**Methods returning new values is a transferable idea.** It comes up again with lists
and dictionaries (a collection you look things up in by name). Plant it clearly here
with the `name.upper()` example, where they can see the string not change, and it will
be much easier when the same shape appears with list methods later. Note that list
methods mostly do modify in place, which is really inconsistent, so flag it now as
something interesting rather than pretending the language is uniform.

**The `join` syntax is backwards and needs repetition.** Separator first, then the list
inside the brackets. Say it, have them type it, say it again next session.

**Slicing only needs the basic form here.** `word[1:4]` and `word[:3]` and `word[3:]`
are enough. Skipping the step `word[::2]` entirely, and negative steps, which are really
confusing and rarely needed.

**Exercise 2.7, the wrong conversion.** The correct response is to ask what type
they need rather than to fix it for them.

**Exercise 2.13, the generator expression.** Do not teach this now. Show it for ten
seconds as a curiosity if they are curious, then say "this is a unit ten thing, do
not use it in exercises".

**Preview of next unit.** They can get information into the program. Next session the
program starts making decisions, and they meet `==` for the first time.
