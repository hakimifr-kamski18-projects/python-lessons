---
title: Unit 02 solutions
sidebar:
  label: Solutions
---
## Warm-ups

### 2.1 What type comes back?

```python
value = input("...") # str, always, no matter what is typed
value = int(input("...")) # int, or a crash if they typed nonsense
value = float(input("...")) # float, or a crash
value = str(input("...")) # str, still
```

The last one is the trick. `input()` already gives back a string, so wrapping it in `str()`
changes nothing at all. It is harmless and completely pointless. Run it and check with
`type()` to see this for yourself.

Whatever the user types is text, even `25`, which is the characters 2 and 5. That is why
`input()` always gives a string.

### 2.2 Predict the slicing

```python
word = "elephant" # e l e p h a n t
                       # 0 1 2 3 4 5 6 7
```

| Expression | Result | Why |
| --- | --- | --- |
| `len(word)` | `8` | eight characters |
| `word[0]` | `'e'` | first character, position zero |
| `word[-1]` | `'t'` | last character |
| `word[2:5]` | `'eph'` | positions 2, 3, 4. Stops before 5 |
| `word[:4]` | `'elep'` | positions 0 to 3 |
| `word[4:]` | `'hant'` | position 4 to the end |
| `word[100:200]` | `''` | past the end of a slice is allowed, gives empty |

If you got `'epha'` for `word[2:5]`, you are counting the end position as included.
That is the most common slicing mistake. Say the rule to yourself: the start is included
and the end is not.

### 2.3 Predict the methods

```python
text = " Hello World "
```

| Expression | Result |
| --- | --- |
| `text.strip()` | `'Hello World'` |
| `text.lower()` | `' hello world '` |
| `text.strip().lower()` | `'hello world'` |
| `text.lower().strip()` | `'hello world'` |
| `text.replace("World", "there")` | `' Hello there '` |
| `text.strip().count("l")` | `3` |

The order in the third and fourth rows does not matter here, because `strip()` only
removes spaces at the ends and `lower()` only changes letters. The order would matter for
other pairs, for example `lower()` and then `title()` gives a different result from
`title()` and then `lower()`.

`count("l")` gives 3. There is one `l` in `Hello` and two in `World`. If you got 2, you
only looked at `World`.

### 2.4 Spot the bug

```python
answer = input("Continue? ")
```

If the user types exactly `yes` and then presses Enter, the answer is `'yes'` and the
comparison works. The problem is that often they do not type exactly `yes`. They might
type `yes ` with a space at the end, or `Yes` with a capital, or ` y`. The comparison
`==` requires an exact match, character for character, and a space is a character.

The way to see it.

```python
answer = input("Continue? ")
print(repr(answer)) # 'yes ' <- the space at the end is right there
```

The fix.

```python
answer = input("Continue? ").strip().lower()
```

Then `yes`, `Yes`, `YES`, ` yes ` all work, which is what the user expects.

The `if` in the exercise is unit 03 material. If you have not met `if` yet, you can still
find the problem with `print(repr(answer))` and `print(answer == "yes")`.

---

## Core

### 2.5 Name badge

```python
first = input("First name: ").strip()
last = input("Last name: ").strip()

full_name = f"{first} {last}".upper()
email = f"{first}.{last}@example.com".lower()

print("=" * 28)
print(f"  {full_name}")
print(f"  {email}")
print("=" * 28)
```

Two useful asides here.

`"=" * 28` is string repetition. Multiplying a string by a number repeats it, which is
much nicer than typing twenty eight equals signs.

The email uses `f"{first}.{last}@example.com"` and then calls `.lower()` on the whole
thing, which is simpler than lowercasing each piece separately. Either way works.

Output for Ada Lovelace.

```
============================
  ADA LOVELACE
  ada.lovelace@example.com
============================
```

The width will not match if the name is very long. That is fine here. Making the badge
line up for any length of name is a harder problem that this exercise does not ask for.

### 2.6 Mad libs

```python
noun = input("Enter a noun: ").strip()
verb = input("Enter a verb: ").strip()
adjective = input("Enter an adjective: ").strip()

print(f"The {adjective} {noun} likes to {verb} in the rain.")
```

Simple, and the only choice to make is where to `.strip()`. Every input gets one.

Run it a few times with silly answers. Running a program again and again is how the
syntax becomes familiar.

### 2.7 Rectangle

```python
width = float(input("Width: "))
height = float(input("Height: "))

area = width * height
perimeter = 2 * (width + height)

print(f"Area: {area:.1f}")
print(f"Perimeter: {perimeter:.1f}")
```

For width 2.5 and height 4, that gives an area of `10.0` and a perimeter of `13.0`.

The thing to check is `float` rather than `int`. If you used `int` and typed `2.5`,
you get a `ValueError`, because `int()` refuses decimals. This is the same rule from the
cheat sheet, showing up on its own.

The second thing to check is `2 * (width + height)` rather than `2 * width + height`,
which is a classic precedence slip. Compute both and compare. For 2.5 and 4,
the correct answer is 13.0 and the wrong one is 9.0, so it shows up clearly.

### 2.8 Age calculator

```python
name = input("Name: ").strip()
birth_year = int(input("Birth year: "))

age_2030 = 2030 - birth_year
age_2020 = 2020 - birth_year

print(f"{name.title()}, in 2030 you will be {age_2030}.")
print(f"In 2020 you turned {age_2020}.")
```

Nothing tricky, and that is the point. It is a practice exercise for the `int`
conversion. If you wrote `int(input(...))` on one line, that is fine now.

### 2.9 Initials

For two names.

```python
full_name = input("Full name: ").strip()
parts = full_name.split()

first_initial = parts[0][0].upper()
last_initial = parts[1][0].upper()

print(f"{first_initial}.{last_initial}.")
```

The double indexing `parts[0][0]` is the interesting part. Read it from left to right.
Take the first item of the list, which is a string, then take the first character of
that string. Say it to yourself. This idea of reaching inside something that is inside
something else comes back often later.

For three names, add a middle line.

```python
middle_initial = parts[1][0].upper()
last_initial = parts[2][0].upper()
```

Each version only works for its own number of names. With one name, the three name
version stops with an `IndexError`. Handling any number of names needs a loop, which you
will meet in unit 04.

### 2.10 Word count

```python
sentence = input("Enter a sentence: ").strip()

print(f"Characters: {len(sentence)}")
print(f"Words: {len(sentence.split())}")
print(f"Title case: {sentence.title()}")
```

For `the quick brown fox jumps over the lazy dog`, the answers are 43 characters and 9
words.

Check the count by hand. The character
count is 43 because it counts the eight spaces as well as the letters. If you guessed
35, you forgot the spaces.

`len(sentence.split())` does two steps in one line. Write it in two lines if
you find it hard to read.

```python
words = sentence.split()
print(f"Words: {len(words)}")
```

That is the better habit at this stage. The all-in-one-line version can come later.

### 2.11 Username generator

```python
full_name = input("Full name: ").strip()
number = input("Favourite number: ").strip()

parts = full_name.split()
first_initial = parts[0][0]
last_name = parts[1]

username = f"{first_initial}{last_name}{number}".lower()

print(f"Your username is {username}")
```

For `Anna Smith` and `42`, this gives `asmith42`.

`number` is left as a string on purpose here, because it is glued onto other text and
never used in arithmetic. The exercise is testing this choice. Ask "does this need to be
a number?" The answer is no, because it is pasted into a name.

If you converted it to `int` and then got a `TypeError` when gluing it into the username,
that is a useful mistake. You can fix it by converting it back with `str()`, or better,
by not converting it in the first place. Try `str(number)` to see that it works, then
decide which version you prefer and why.

---

## Stretch

### 2.12 Sentence surgery

```python
sentence = input("Enter a sentence: ").strip()

print(sentence.replace(" ", "_"))
print(sentence.title())
print(f"e appears: {sentence.count('e')}")
```

For `the quick brown fox`, the three outputs are `the_quick_brown_fox`, `The Quick Brown
Fox`, and `e appears: 1`.

The interesting bit is `count('e')`. It is case sensitive, so it does not count `E`.
Try it with a sentence containing a capital `E`. To count both kinds, call `.lower()` on
the sentence first, as in `sentence.lower().count('e')`.

### 2.13 Acronym

For a four-word name, without a loop.

```python
org = input("Organisation: ").strip()
parts = org.split()

acronym = parts[0][0] + parts[1][0] + parts[2][0] + parts[3][0]
print(acronym.upper())
```

For `North Atlantic Treaty Organization` this gives `NATO`.

This only works for exactly four words. It is the best you can do without a loop. A loop
(unit 04) will fix that.

### 2.14 Palindrome check

```python
word = input("Enter a word: ").strip().lower()
reversed_word = word[::-1]

print(f"{word} backwards is {reversed_word}")
if reversed_word == word:
    print("That is a palindrome")
else:
    print("That is not a palindrome")
```

(Again, `if` is unit 03. If you have not got there, just print both words and compare
them by eye, or print `reversed_word == word`.)

The key part is `word[::-1]`, which this course did not teach before. Start with the
slices you already know, then extend.

```
word[0:3] start at 0, stop before 3, step forward by 1
word[::2] start at the beginning, go to the end, step 2 (every other character)
word[::-1] step backwards by 1, so the whole thing reversed
```

An empty start means "the beginning", an empty end means "the end", and `-1` as the step
means "go backwards". So `[::-1]` is "the whole string, backwards".

This is a common way to reverse a string in Python.

The `.lower()` matters, so that `Racecar` also works. Try it without the `.lower()` and see.

### 2.15 The invisible bug

```python
answer = input("Type the word magic: ")

if answer.strip().lower() == "magic":
    print("Correct!")
else:
    print("Wrong, try again")
```

A bug like this is worse than a crash because the program keeps running and there is no
error message telling you what went wrong.

Ask yourself how you would have found this bug if you had not been told where it was.
Here are three ways. Print
`repr(answer)` to see the hidden character. Print `len(answer)` and compare with
`len("magic")`. Compare character by character. All three work.

Finally, `.strip()` on every single `input()` you ever write is a very cheap
and very effective habit.
