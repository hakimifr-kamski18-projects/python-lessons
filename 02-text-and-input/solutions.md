# Unit 02 solutions

## Warm-ups

### 2.1 What type comes back?

```python
value = input("...") # str, always, no matter what is typed
value = int(input("...")) # int, or a crash if they typed nonsense
value = float(input("...")) # float, or a crash
value = str(input("...")) # str, still
```

The last one is the trick. `input()` already gives back a string, so wrapping it in `str()`
changes nothing at all. It is harmless and completely pointless. It is worth running
it and checking with `type()` yourself rather than taking my word for it.

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
That is the single most common slicing mistake, and the fix is to say the rule out loud.
Start is included, end is not.

### 2.3 Predict the methods

```python
text = " Hello World "
```

| Expression | Result |
| --- | --- |
| `text.strip` | `'Hello World'` |
| `text.lower` | `' hello world '` |
| `text.strip.lower` | `'hello world'` |
| `text.lower.strip` | `'hello world'` |
| `text.replace("World", "there")` | `' Hello there '` |
| `text.strip.count("l")` | `3` |

Note that the order in the third and fourth rows does not matter here, because `strip()`
only touches the ends and `lower()` only changes letters in the middle. It is worth asking
yourself whether there is any input where the order would matter. There is not, for these two,
and thinking about why is a good exercise.

`count("l")` gives 3. There is one `l` in `Hello` and two in `World`. Careful students
sometimes get 2, from only looking at `World`.

### 2.4 Spot the bug

```python
answer = input("Continue? ")
```

If the user types `yes` and then presses Enter, the answer is `'yes'` and the comparison
works. So why does it fail?

Because very often they do not type exactly `yes`. They might type `yes ` with a
trailing space, or `Yes` with a capital, or ` y`. The comparison `==` requires an exact
match, character for character, and a trailing space is a character.

The way to see it.

```python
answer = input("Continue? ")
print(repr(answer)) # 'yes ' <- the space is right there
```

The fix.

```python
answer = input("Continue? ").strip.lower
```

Then `yes`, `Yes`, `YES`, ` yes ` all work, which is what the user expects.

A note on the exercise as written. The `if` on the next line is unit 03 material, so
this is a peek ahead. If you have not met `if` yet, you can still do the detective
work with `print(repr(answer))` and `print(answer == "yes")`.

---

## Core

### 2.5 Name badge

```python
first = input("First name: ").strip
last = input("Last name: ").strip

full_name = f"{first} {last}".upper
email = f"{first}.{last}@example.com".lower

print("=" * 28)
print(f" {full_name}")
print(f" {email}")
print("=" * 28)
```

Two useful asides here.

`"=" * 28` is string repetition. Multiplying a string by a number repeats it, which is
much nicer than typing twenty eight equals signs. You met this in unit 01 if you did
the stretch exercises.

The email uses `f"{first}.{last}@example.com"` and then calls `.lower` on the whole
thing, which is simpler than lowercasing each piece separately. Either way works.

Output for Adamari Lovelace.

```
============================
  ADAMARI LOVELACE
  ada.lovelace@example.com
============================
```

Note that the width will not match if the name is very long. That is fine. Getting the
badge to line up for any length of name is a real problem and it is not worth solving
today.

### 2.6 Mad libs

```python
noun = input("Enter a noun: ").strip
verb = input("Enter a verb: ").strip
adjective = input("Enter an adjective: ").strip

print(f"The {adjective} {noun} likes to {verb} in the rain.")
```

Simple, and the only judgement call is where to `.strip`. Every input gets one.

Worth running it a few times with silly answers. Small programs that are fun to
run get run more, and running things is how the syntax settles.

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
you get a `ValueError`, which is the lesson from the lesson file arriving on its own.

The second thing to check is `2 * (width + height)` rather than `2 * width + height`,
which is a classic precedence slip. Compute both and compare. For 2.5 and 4,
the correct answer is 13.0 and the wrong one is 9.0, so it shows up clearly.

### 2.8 Age calculator

```python
name = input("Name: ").strip
birth_year = int(input("Birth year: "))

age_2030 = 2030 - birth_year
age_2020 = 2020 - birth_year

print(f"{name.title}, in 2030 you will be {age_2030}.")
print(f"In 2020 you turned {age_2020}.")
```

Nothing tricky, and that is the point. It is a consolidation exercise for the `int`
conversion. If you wrote `int(input(...))` on one line, that is fine now.

### 2.9 Initials

For two names.

```python
full_name = input("Full name: ").strip
parts = full_name.split

first_initial = parts[0][0].upper
last_initial = parts[1][0].upper

print(f"{first_initial}.{last_initial}.")
```

The double indexing `parts[0][0]` is the interesting part. Read it inside out. Take the
first item of the list, which is a string, then take the first character of that string.
Say that out loud. It is your first taste of reaching inside something that
is inside something else, and it comes back constantly later with dictionaries.

For three names, add a middle line.

```python
middle_initial = parts[1][0].upper
last_initial = parts[2][0].upper
```

Note that this breaks completely if there is only one name, with an `IndexError`. That
is correct behaviour and a good thing to notice, because handling a variable number
of names properly needs a loop (unit 04).

A cleaner general version, once you have loops, will be three lines instead of however
many names there are. It is worth seeing where this is heading.

### 2.10 Word count

```python
sentence = input("Enter a sentence: ").strip

print(f"Characters: {len(sentence)}")
print(f"Words: {len(sentence.split)}")
print(f"Title case: {sentence.title}")
```

For `the quick brown fox jumps over the lazy dog`, the answers are 43 characters and 9
words.

Check the word count by hand. There is a real lesson here. The character
count is 43 because it counts the eight spaces as well as the letters. If you guessed
35, you forgot the spaces.

`len(sentence.split)` is neat but it hides a step. Write it in two lines if
you find it hard to read.

```python
words = sentence.split
print(f"Words: {len(words)}")
```

That is the better habit at this stage, and the nested version can come later.

### 2.11 Username generator

```python
full_name = input("Full name: ").strip
number = input("Favourite number: ").strip

parts = full_name.split
first_initial = parts[0][0]
last_name = parts[1]

username = f"{first_initial}{last_name}{number}".lower

print(f"Your username is {username}")
```

For `Anna Smith` and `42`, this gives `asmith42`.

Note that `number` is left as a string on purpose here, because it is being glued onto
other text and never used in arithmetic. That is the judgement call the exercise is
testing. Asking "does this need to be a number?" and answering "no, it is being pasted
into a name" is the right reasoning.

If you converted it to `int` and then hit a `TypeError` gluing it into the username,
that is a very useful mistake, and the fix is either to convert it back with `str` or,
better, to not convert it in the first place. Try `str(number)` and see that
it works, then ask yourself which version you prefer and why.

---

## Stretch

### 2.12 Sentence surgery

```python
sentence = input("Enter a sentence: ").strip

print(sentence.replace(" ", "_"))
print(sentence.title)
print(f"The letter e appears {sentence.count('e')} times")
```

For `the quick brown fox`, the three outputs are `the_quick_brown_fox`, `The Quick Brown
Fox`, and 1.

The interesting bit is `count('e')`. It is case sensitive, so it does not count `E`.
Try it with a sentence containing a capital and then decide whether to fix it
with `.lower` first.

### 2.13 Acronym

For a four-word name, without a loop.

```python
org = input("Organisation: ").strip
parts = org.split

acronym = parts[0][0] + parts[1][0] + parts[2][0] + parts[3][0]
print(acronym.upper)
```

For `North Atlantic Treaty Organization` this gives `NATO`.

It is worth being clear about this. This is a terrible way to write this program, because it
only works for exactly four words. It is here because it is the best you can do without
a loop, and it makes a good advertisement for unit 04. When you meet loops, this whole
exercise collapses into three lines.

There is a neat trick that works for any number of words, using the tools you already
have.

```python
print("".join(part[0] for part in parts).upper)
```

It uses a generator expression, which is a comprehension, which
is not in this course on purpose.

### 2.14 Palindrome check

```python
word = input("Enter a word: ").strip.lower
reversed_word = word[::-1]

print(f"{word} backwards is {reversed_word}")
if reversed_word == word:
    print("That is a palindrome")
else:
    print("That is not a palindrome")
```

(Again, `if` is unit 03, so if you have not got there, just print both words and
compare them by eye.)

The clever part is `word[::-1]`, and you were not taught it. Start with the slices you
already know, then extend.

```
word[0:3] start at 0, stop before 3, step forward by 1
word[::2] start at the beginning, go to the end, step 2 (every other character)
word[::-1] step backwards by 1, so the whole thing reversed
```

An empty start means "the beginning", an empty end means "the end", and `-1` as the step
means "go backwards". So `[::-1]` is "the whole string, backwards".

This is really a "wow" moment for beginners, and it is worth enjoying it. It
is also worth knowing that this exact trick appears in every Python codebase in the
world.

The `.lower` matters, so that `Racecar` also works. Try it without the `.lower` and see.

### 2.15 The invisible bug

```python
answer = input("Type the word magic: ")

if answer.strip.lower == "magic":
    print("Correct!")
else:
    print("Wrong, try again")
```

The one sentence explanation. A bug like this is nastier than a crash because there is
no error to point at the problem, and there is no error message telling you what went
wrong.

The broader question is worth asking yourself. How would you have found this bug if you
had not been told where it was? These are good answers to know. Print
`repr(answer)` to see the hidden character. Print `len(answer)` and compare with
`len("magic")`. Compare character by character. All three are real techniques and all
three work.

Finally, `.strip()` on every single `input()` you ever write is a very cheap
and very effective habit.
