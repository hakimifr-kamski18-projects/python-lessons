---
title: Unit 02 exercises
sidebar:
  label: Exercises
---
Predict before you run. Convert before you calculate.

---

## Before you start

A few small tools that the exercises below use.

`repr(x)` gives `x` as Python would write it, with quotes around text. It makes hidden
spaces visible. `print("hi ")` shows `hi`, but `print(repr("hi "))` shows `'hi '`, and
now you can see the space at the end.

A slice can leave out its start or its end. `name[:2]` means "from the beginning to
position 2" and `name[2:]` means "from position 2 to the end". A slice that goes past the
end does not give an error. It gives whatever is there, so `"cat"[0:100]` is `"cat"`.

You can put methods (commands that belong to a value) one after another. Python runs them
from left to right, and each one works on the result of the one before it.

```python
text = "  Ada  "
print(text.strip().lower())   # first strip, then lower: ada
print("hello".count("l"))     # how many times "l" appears: 2
```

`split()` cuts text into a list, which is several values kept in order. Square brackets
pick one value out of it, starting at 0.

```python
parts = "ada lovelace".split()
print(parts[0])      # ada
print(parts[1][0])   # l  (the first letter of the second value)
```

Multiplying text by a number repeats it, so `"=" * 3` is `"==="`.

Two exercises use `if` and `==`, which you will learn properly in unit 03. For now, copy
the `if` lines as they are and put your attention on the text.

---

## Warm-ups

### 2.1 What type comes back?

For each line, write down whether `value` is a `str`, `int` or `float`. Then check with
`type()`.

```python
value = input("Type something: ")
```

```python
value = int(input("Type something: "))
```

```python
value = float(input("Type something: "))
```

```python
value = str(input("Type something: "))
```

The last one is a trick question. Think about why before you answer. Whatever the user
types is text, even `25`, which is the characters 2 and 5.

### 2.2 Predict the slicing

```python
word = "elephant"
```

Write down what each of these gives.

- `len(word)`
- `word[0]`
- `word[-1]`
- `word[2:5]`
- `word[:4]`
- `word[4:]`
- `word[100:200]`

### 2.3 Predict the methods

```python
text = " Hello World "
```

Write down what each of these gives, and note which ones include spaces.

- `text.strip()`
- `text.lower()`
- `text.strip().lower()`
- `text.lower().strip()`
- `text.replace("World", "there")`
- `text.strip().count("l")`

### 2.4 Spot the bug

This is meant to check whether the user typed `yes`. It sometimes fails even though the
user thinks they typed `yes`. Why? (`if` is unit 03, so copy the `if` lines for now.)

```python
answer = input("Continue? ")
if answer == "yes":
    print("Continuing")
```

Hint: `print(repr(answer))` shows the text with quotes, so any spaces become visible.

---

## Core

### 2.5 Name badge

Ask for a first name and a last name, then print a badge.

```
============================
  ADA LOVELACE
  ada.lovelace@example.com
============================
```

The top and bottom lines are twenty eight equals signs, which you can just type out. The
name should be in capitals, and the email should be the first name in lowercase, a dot,
the last name in lowercase, then `@example.com`. Test it with `Ada` and `Lovelace`.

### 2.6 Mad libs

Ask for a noun, a verb and an adjective. Then print a silly sentence using all three.

Example.

```
Enter a noun: bicycle
Enter a verb: dance
Enter an adjective: sleepy
The sleepy bicycle likes to dance in the rain.
```

### 2.7 Rectangle

Ask for the width and the height of a rectangle. Print the area and the perimeter, each
rounded to one decimal place, and each labelled.

Test it with `2.5` and `4` to make sure decimals work.

### 2.8 Age calculator

Ask for a name and a birth year. Print how old they will be in 2030, and also how old
they turned in 2020.

Both ages are the year minus the birth year. Ignore birthdays. Check the arithmetic
carefully. The birth year is the only number you should have to change to get new answers.

### 2.9 Initials

Ask for a full name, like `ada lovelace`. Print just the initials in capitals, so `A.L.`

You will need `split()` to get the pieces apart. It gives a list, which is several values
in order, and `parts[0]` is the first one.

Write a version for two names. Then change it so that it works for three names, like
`ada king lovelace`.

### 2.10 Word count

Ask for a sentence. Print how many characters it has, how many words it has, and what it
looks like in title case (every word starts with a capital letter).

Run it on this exact sentence to check.

```
the quick brown fox jumps over the lazy dog
```

### 2.11 Username generator

Ask for a full name. Generate a username made of the first letter of the first name, the
whole last name, and a number the user types, all in lowercase. So for `Anna
Smith` and `42`, the answer is `asmith42`.

---

## Stretch

### 2.12 Sentence surgery

Ask for a sentence. Print it with all the spaces replaced by underscores, then print it
again in title case (use `title()`), then print how many times the letter `e` appears.

### 2.13 Acronym

Ask for an organisation name, like `North Atlantic Treaty Organization`, and print the
acronym, `NATO`.

`split()` and a loop would do it, but you do not have loops yet. See if you can do it with
just indexing, if the input always has three or four words.

### 2.14 Palindrome check

Ask for a word. Print whether it reads the same backwards. `racecar` and `level` do.
`hello` does not.

You will need to reverse a string, which you have not been taught. Here is a hint: a
slice can have a third number, the step. `word[::2]` takes every second character. Try a
negative step and see what happens. Then write down in your own words why it works.
(`if` is unit 03, so copy the `if` lines for now, or print `reversed_word == word`.)

### 2.15 The invisible bug

Write a program that asks two questions, the second of which is "Type the word magic".
Compare the answer to `"magic"` and print whether it is right. You can use
`print(answer == "magic")`, or an `if` and `else` (unit 03) that you copy for now.

Now run it and type `magic` with two spaces after it. It says wrong. Fix the program so
it says right.

Then write down, in one sentence, why this kind of bug is worse than a crash.

---

## Check yourself

Before you start unit 03, make sure you can do these without notes.

- Get a number from the user and use it in arithmetic.
- Explain why `input()` needs converting and what `type()` shows you.
- Take the first three characters of a string.
- Clean up messy input with `strip()` and `lower()`.
- Split a sentence into words and rejoin them with a different separator.
