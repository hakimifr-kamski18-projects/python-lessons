---
title: Unit 02 exercises
sidebar:
  label: Exercises
---
Predict before you run. Convert before you calculate.

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

The last one is a trick question. Think about why before you answer.

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

- `text.strip`
- `text.lower`
- `text.strip.lower`
- `text.lower.strip`
- `text.replace("World", "there")`
- `text.strip.count("l")`

### 2.4 Spot the bug

This is meant to check whether the user typed `yes`. It never works, even when they type
`yes` correctly. Why?

```python
answer = input("Continue? ")
if answer == "yes":
    print("Continuing")
```

Hint, use `repr` to look at what `answer` actually contains.

---

## Core

### 2.5 Name badge

Ask for a first name and a last name, then print a badge.

```
============================
  ADAMARI LOVELACE
  ada.lovelace@example.com
============================
```

The top and bottom lines are twenty eight equals signs, which you can just type out. The
name should be in capitals, and the email should be lowercase first name, a dot,
lowercase last name, then `@example.com`.

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

Ask for a name and a birth year. Print how old they will be in 2030, and how old they
turned in 2020.

Check the arithmetic carefully. Both answers come from the birth year, so you should be
able to change one number in the code and have everything follow.

### 2.9 Initials

Ask for a full name, like `ada lovelace`. Print just the initials in capitals, so `A.L.`

You will need `split()` to get the pieces apart. The number of names could be two or
three, so test both.

### 2.10 Word count

Ask for a sentence. Print how many characters it has, how many words it has, and what it
looks like in title case.

Run it on this exact sentence to check.

```
the quick brown fox jumps over the lazy dog
```

### 2.11 Username generator

Ask for a full name. Generate a username made of the first letter of the first name, the
whole last name, and a random-ish number the user gives, all in lowercase. So for `Anna
Smith` and `42`, the answer is `asmith42`.

---

## Stretch

### 2.12 Sentence surgery

Ask for a sentence. Print it with all the spaces replaced by underscores, then print it
again with only the first letter of each word capitalised, then print how many times the
letter `e` appears.

### 2.13 Acronym

Ask for an organisation name, like `North Atlantic Treaty Organization`, and print the
acronym, `NATO`.

`split()` and a loop would do it, but you do not have loops yet. See if you can do it with
just indexing, if the input always has three or four words.

### 2.14 Palindrome check

Ask for a word. Print whether it reads the same backwards. `racecar` and `level` do.
`hello` does not.

You will need to know how to reverse a string, which you have not been taught. Try
searching for it, or experiment with slicing and negative numbers until something works.
Then explain out loud why it works.

### 2.15 The invisible bug

Write a program that asks two questions, the second of which is "Type the word magic".
Compare the answer to `"magic"` and print whether they got it right.

Now run it and type `magic` with two spaces after it, without pressing backspace. It
says wrong. Fix the program so it says right.

Then explain, in one sentence, why this class of bug is nastier than a crash.

---

## Before next session

Be able to do these without notes.

- Get a number from the user and use it in arithmetic.
- Explain why `input()` needs converting and what `type()` shows you.
- Take the first three characters of a string.
- Clean up messy input with `strip()` and `lower()`.
- Split a sentence into words and rejoin them with a different separator.
