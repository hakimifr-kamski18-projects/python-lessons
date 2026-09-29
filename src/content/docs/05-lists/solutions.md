---
title: Unit 05 solutions
sidebar:
  label: Solutions
---
## Warm-ups

### 5.1 Predict the output

```python
numbers = [10, 20, 30, 40, 50]
```

| Expression | Result |
| --- | --- |
| `numbers[0]` | `10` |
| `numbers[-1]` | `50` |
| `numbers[1:3]` | `[20, 30]` |
| `len(numbers)` | `5` |
| `numbers[2]` | `30` |
| `20 in numbers` | `True` |
| `sum(numbers)` | `150` |

`numbers[1:3]` gives positions 1 and 2, so 20 and 30. End position excluded, same as
string slicing. If you got `[20, 30, 40]`, that rule has not stuck yet and it is worth
going back to unit 02 for five minutes.

### 5.2 Predict the mutation

```python
a = [1, 2, 3]
a.append(4)
print(a) # [1, 2, 3, 4]
```

```python
a = [1, 2, 3]
b = a
b.append(4)
print(a) # [1, 2, 3, 4] <- surprising!
```

```python
a = [1, 2, 3]
b = a[:]
b.append(4)
print(a) # [1, 2, 3] <- unchanged
```

The middle one is the lesson. `b = a` does not make a copy. It gives the same list a
second name. Changing it through one name is visible through the other, because there is
only one list.

In the third, `a[:]` makes a really new list with the same contents, so `b` and `a` are
independent afterwards.

Say this sentence. "Assigning a list does not copy it."

Be briefly annoyed that this is different from numbers, because it is:

```python
a = 5
b = a
b = 6
print(a) # 5, unchanged
```

Numbers behave the way you expect. Lists do not. The reason is that numbers are
immutable, so `b = a` for numbers cannot cause this, and `b = 6` is really "reassign
`b`" rather than "change the 5". The rule is what matters
right now.

### 5.3 Spot the bug

```python
names = []
names = names.append("Ada")
names = names.append("Grace")
print(len(names))
```

The immediate failure is on the third line, a `TypeError`, because `names` became `None`
after the first `append()`. `append()` returns `None` and does its work by changing the
list, so assigning the result back destroys the list.

The problem that is hard to see is the first line. It is not wrong exactly, but the `=
[]` is pointless if you are about to overwrite the variable. Your intent is clearly to
start with an empty list, so the first line should be the whole setup.

The fix.

```python
names = []
names.append("Ada")
names.append("Grace")
print(len(names)) # 2
```

Make the connection. This is the exact opposite of unit 02, where `name = name.upper`
was the correct thing to write. Both are correct in their own place, and the way to tell
is to check whether the method gives something back or changes the thing. If you are
unsure, `print()` the result and see.

### 5.4 Finding the error

```python
names[2] # IndexError: list index out of range
names.index("Alan") # ValueError, something about x not being in list
names.remove("Alan") # ValueError, something about x not being in list
```

(The exact wording of the `ValueError` messages changes between Python versions, so do
not expect a character for character match. What matters is the error type and the
meaning.)

Two different error types, and the distinction is the point.

`IndexError` means the position does not exist. `ValueError` means the value is not in
the list, even though the call itself was perfectly valid.

This mirrors `int("hello")` from unit 02, which is also a `ValueError`, because the kind
of thing was right and the content was wrong.

The second and third lines both raise before `print()` gets a chance to run. That is worth
noticing, because `print(names.remove("Alan"))` looks like it should print something.

### 5.5 Sort or reverse

```python
numbers = [5, 2, 9, 1, 7]
numbers.reverse
print(numbers) # [7, 1, 9, 2, 5]
```

It is not sorted. `reverse()` flips the order and does nothing else.

- `reverse()` reverses the current order.
- `sort(reverse=True)` sorts, then reverses, giving descending order.

The way to make this concrete. Take a shuffled list and run both
operations and compare the outputs. On `[5, 2, 9, 1, 7]`, `reverse()` gives `[7, 1, 9, 2,
5]` and `sort(reverse=True)` gives `[9, 7, 5, 2, 1]`. Very different.

---

## Core

### 5.6 Shopping list

```python
shopping = []

while True:
    item = input("Item (or 'done' to finish): ").strip

    if item.lower == "done":
        break

    if item:
        shopping.append(item)

print()
print(f"You have {len(shopping)} items:")
for item in shopping:
    print(f" - {item}")

print()
print("In alphabetical order:")
for item in sorted(shopping):
    print(f" - {item}")
```

Two details worth checking.

The `if item:` guard skips empty input, so pressing Enter by accident does not add a
blank item. That is the truthiness point from unit 03 in real use.

And `sorted(shopping)` rather than `shopping.sort`, because sorting the original would
change the order the user entered them in, and the exercise prints both orders. This is
a good opportunity to ask yourself which one you want and why. If you only needed the sorted
version, `shopping.sort` would be fine and would save a copy.

### 5.7 Grades

```python
how_many = int(input("How many students? "))
scores = []

for i in range(how_many):
    score = float(input(f"Score {i + 1}: "))
    scores.append(score)

if scores:
    print(f"Highest: {max(scores):.1f}")
    print(f"Lowest: {min(scores):.1f}")
    print(f"Average: {sum(scores) / len(scores):.1f}")
else:
    print("No scores entered")
```

The `if scores:` guard is the important part. Without it, a count of 0 gives a
`ZeroDivisionError` on the average line, exactly like exercise 4.8.

Note that `if scores:` works because an empty list is falsy, which is unit 03's
truthiness rule applied to a list. That is the reason the guard is written this way
rather than `if len(scores) > 0`.

### 5.8 Remove the duplicates

```python
items = ["apple", "banana", "apple", "cherry", "banana", "apple"]

unique = []

for item in items:
    if item not in unique:
        unique.append(item)

print(unique) # ['apple', 'banana', 'cherry']
```

The `not in` check against the growing list is the whole technique. It is also worth
noting that this is slow for large lists, since every item has to be checked against
everything already collected. There is a much faster way using a dictionary, which is
unit 07 material.

The order is preserved because items are processed in order and only the first
occurrence of each is kept. If you used `sorted()` you would lose the original order,
which is why the exercise asked not to.

### 5.9 Reverse without reverse

```python
items = ["a", "b", "c", "d", "e"]

reversed_items = []

for i in range(len(items) - 1, -1, -1):
    reversed_items.append(items[i])

print(reversed_items) # ['e', 'd', 'c', 'b', 'a']
```

The interesting part is `range(len(items) - 1, -1, -1)`.

```
len(items) - 1 start at the last valid position, 4
-1 stop before -1, so the last value is 0
-1 step backwards
```

Both of the negative numbers are doing different jobs, which is confusing. The middle
one is the stop value and the last one is the step. Trace it and print the
range with `list()` before writing the loop.

The common wrong answer is `range(len(items), 0, -1)`, which starts one too far to the
right and gives an `IndexError` immediately, then stops one too early and never reaches
position 0. Getting that wrong and debugging it is more valuable than getting it right
first time.

Once it works, look at `items[::-1]` from unit 02 and note that the slicing version is
what people actually write.

### 5.10 Biggest, the hard way

```python
numbers = [4, 7, 2, 9, 4]

biggest = numbers[0]

for number in numbers:
    if number > biggest:
        biggest = number

print(biggest) # 9
```

The answer to the question is that the starting value matters. Initialising to `0` works
for lists with positive numbers and fails for lists of all negative numbers, because 0
is bigger than all of them and never gets replaced.

Initialising to `numbers[0]` fixes it, because the first element is a real value from
the list and the comparisons after it will do the right thing.

There is one edge case. If the list is empty, `numbers[0]` is an `IndexError`. So the
fully correct version is this.

```python
if numbers:
    biggest = numbers[0]
    for number in numbers:
        if number > biggest:
            biggest = number
    print(biggest)
else:
    print("The list is empty")
```

Test with `[-3, -7, -2]` on both versions. Seeing the `0` version print `0`
for that list is the moment the lesson lands.

### 5.11 Word lengths

```python
sentence = input("Sentence: ").strip
words = sentence.split

lengths = []
for word in words:
    lengths.append(len(word))

print(f"Lengths: {lengths}")

longest = words[0]
for word in words:
    if len(word) > len(longest):
        longest = word

print(f"Longest word: {longest}")
```

This is the same "biggest so far" pattern as 5.10, comparing lengths instead of values.
Noticing that connection is valuable. It is one pattern, not two.

Note the `words[0]` initialisation for the same reason as 5.10. It makes ties work out
in favour of whichever tied word comes first, which is fine.

### 5.12 Filter and transform

```python
numbers = [4, -7, 2, 9, -4, 1, 8, -3]

result = []
for number in numbers:
    if number < 0:
        result.append(number ** 2)

print(result) # [49, 16, 9]
```

Filter and transform in one loop. Note that the square of a negative number is positive,
so the output is all positive even though the input was all negative. Some students
expect negative output, which is worth catching.

Also note `number ** 2` gives the right answer even for negatives, because `-7 ** 2` is
49 in Python. That is because `**` binds tighter than the unary minus. Were it the other
way round it would be `-(7 ** 2)` which is also 49, so this particular case is safe
either way.

### 5.13 Insert and delete

```python
names = ["Ada", "Grace", "Alan", "Edsger", "Barbara"]

names.append("Donald")
names.insert(0, "Katherine")
names.remove("Alan")

last = names.pop

print(f"Removed: {last}")
print(names)
print(len(names))
```

If you called `remove()` with a name that is not in the list, you got a `ValueError`.
That is a good thing to have hit.

One question worth asking yourself. What does `names.remove("Ada")` do if there are two Adas in
the list? The answer is that it removes only the first one. That is really a common
source of bugs, and it is easy to check.

### 5.14 Sort by length

```python
words = ["banana", "fig", "apple", "kiwi", "cherry"]

print(sorted(words)) # alphabetical
print(sorted(words, key=len)) # shortest first
print(sorted(words, key=len, reverse=True)) # longest first
```

`key=len` means "when deciding the order, use the length of each item rather than the
item itself". Python calls `len()` on each word, sorts by those numbers, and gives you
back the words.

The explanation in your own words. It is a way of telling
`sorted()` what to compare.

Ties are broken by keeping the original order, which is stable. So `fig` and `kiwi` both
of length 3 stay in their original relative order. Python's sort is stable, which is a
nice guarantee and worth knowing.

---

## Stretch

### 5.15 Report card

```python
names = []
scores = []

count = int(input("How many students? "))
for i in range(count):
    names.append(input(f"Name {i + 1}: ").strip)
    scores.append(float(input(f"Score {i + 1}: ")))

pairs = []
for i in range(len(names)):
    pairs.append([scores[i], names[i]])

pairs.sort(reverse=True)

print()
for pair in pairs:
    print(f"{pair[1]:<10} {pair[0]:>5.1f}")
```

The trick is to store the score first in each pair, so that the default sort puts them
in score order. Python sorts lists of lists by comparing the first item of each, then
the second if the first ties.

That is why the pair is `[score, name]` and not `[name, score]`. If you build it the
other way round, it sorts alphabetically by name, which is a very common first attempt
and a good thing to debug.

On the formatting, `{pair[1]:<10}` left-aligns the name in a width of 10, and
`{pair[0]:>5.1f}` right-aligns the score in a width of 5 with one decimal. The `<` and
`>` are the alignment markers. Without them, numbers align right and text aligns left by
default, which often looks fine anyway.

The awkwardness you should feel here is the point. Two parallel lists are a bad design,
and keeping them in sync by hand is error prone. Notice how easy it would be to append a
name without appending the matching score and end up with garbage. Unit 07 gives a much
better answer.

### 5.16 Second biggest

```python
numbers = [5, 5, 3]

biggest = numbers[0]
second = None

for number in numbers:
    if number > biggest:
        second = biggest
        biggest = number
    elif number < biggest:
        if second is None or number > second:
            second = number

print(second) # 3
```

The logic is that when you find a new biggest, the old biggest becomes the second
biggest. The `elif number < biggest` is what excludes duplicates, which is why `[5, 5,
3]` gives 3 rather than 5.

There is a simpler approach that handles duplicates naturally.

```python
unique = []
for number in numbers:
    if number not in unique:
        unique.append(number)

unique.sort
print(unique[-2])
```

This deduplicates, sorts, and takes the second from the last. It is easier to follow and
slower for big lists, and either is a fine answer.

Note the `second is None` check. `None` is not taught until unit 08, so if you have not
met it, you can use a flag instead.

```python
found_second = False
...
    if not found_second or number > second:
```

Or initialise `second` to the smallest possible value with `float("-inf")`, which also
works and looks mysterious. The thinking
about duplicates is the exercise.

### 5.17 Merge two sorted lists

```python
a = [1, 4, 7, 10]
b = [2, 3, 8, 11]

merged = []
i = 0
j = 0

while i < len(a) and j < len(b):
    if a[i] <= b[j]:
        merged.append(a[i])
        i += 1
    else:
        merged.append(b[j])
        j += 1

while i < len(a):
    merged.append(a[i])
    i += 1

while j < len(b):
    merged.append(b[j])
    j += 1

print(merged)
```

Output is `[1, 2, 3, 4, 7, 8, 10, 11]`.

The reasoning. Because both lists are already sorted, the smallest remaining item in
each list is always at its current index. So comparing `a[i]` with `b[j]` tells you
which one is the next smallest overall.

The two loops at the end are the part people forget. When one list runs out, the other
still has items, and they are already in order, so they can just be appended.

This really is the merge step of merge sort, which is one of the standard sorting
algorithms, and it is the foundation of how large datasets get sorted. The exercise is a
real algorithm, not a toy.

Trace it with the small lists by hand, writing out `i` and `j` at each step.
Four or five steps in, the pattern becomes clear.

### 5.18 Run length encoding

Encoding.

```python
text = "aaabbc"

encoded = ""

if text:
    current = text[0]
    count = 0

    for character in text:
        if character == current:
            count += 1
        else:
            encoded += current + str(count)
            current = character
            count = 1

    encoded += current + str(count)

print(encoded) # a3b2c1
```

The awkward part is the final flush after the loop. The last run never gets written
inside the loop, because there is no next character to trigger the `else`. That "and
then handle the last one" shape is extremely common in string and list processing, and
it is worth feeling it directly rather than being told.

The `if text:` guard handles the empty string, which would otherwise crash on `text[0]`.

Decoding.

```python
encoded = "a3b2c1"

decoded = ""

for i in range(0, len(encoded), 2):
    character = encoded[i]
    count = int(encoded[i + 1])
    decoded += character * count

print(decoded) # aaabbc
```

`range(0, len(encoded), 2)` gives 0, 2, 4, taking every other position. Then `i + 1` is
the character just after, which holds the count.

Note that this only works if counts are single digits. `a12` would break it, since the
`1` and the `2` would be read as separate characters. Handling multi-digit counts needs
a bit more care, and it is a legitimate stretch on top of the stretch if you are
enjoying yourself.

The other thing worth pointing out is `character * count`, which is string repetition
from unit 01, and it is exactly the tool for this.
