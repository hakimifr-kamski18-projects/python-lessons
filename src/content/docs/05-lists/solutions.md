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
string slicing. If you got `[20, 30, 40]`, remember that the end position is not
included.

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

The middle one is the important one. `b = a` does not make a copy. It gives the same list a
second name. Changing it through one name is visible through the other, because there is
only one list.

In the third, `a[:]` makes a really new list with the same contents, so `b` and `a` are
independent afterwards.

Remember this rule: assigning a list does not copy it.

This is different from numbers:

```python
a = 5
b = a
b = 6
print(a) # 5, unchanged
```

Lists can be changed in place and numbers cannot. So `b = 6` just gives `b` a new
value, and `a` stays 5.

### 5.3 Spot the bug

```python
names = []
names = names.append("Ada")
names = names.append("Grace")
print(len(names))
```

The program fails on the third line with `AttributeError: 'NoneType' object has no
attribute 'append'`. After the first `append()`, `names` became `None` (the value that
means "nothing here"). `append()` gives back `None` and does its work by changing the
list, so assigning the result back throws the list away. Then the next `append()` is
asked of `None`, which cannot do it.

The fix.

```python
names = []
names.append("Ada")
names.append("Grace")
print(len(names)) # 2
```

This is the exact opposite of unit 02, where `name = name.upper()`
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

These are two different error types, and the difference is the point.

`IndexError` means the position does not exist. `ValueError` means the value is not in
the list, even though the call itself was perfectly valid.

This mirrors `int("hello")` from unit 02, which is also a `ValueError`, because the kind
of thing was right and the content was wrong.

The second and third lines both raise before `print()` gets a chance to run. Notice this,
because `print(names.remove("Alan"))` looks like it should print something.

### 5.5 Sort or reverse

```python
numbers = [5, 2, 9, 1, 7]
numbers.reverse()
print(numbers) # [7, 1, 9, 2, 5]
```

It is not sorted. `reverse()` flips the order and does nothing else.

- `reverse()` reverses the current order.
- `sort(reverse=True)` sorts, then reverses, giving descending order.

To see the difference, take a shuffled list, run both
operations and compare the outputs. On `[5, 2, 9, 1, 7]`, `reverse()` gives `[7, 1, 9, 2,
5]` and `sort(reverse=True)` gives `[9, 7, 5, 2, 1]`. Very different.

---

## Core

### 5.6 Shopping list

```python
shopping = []

while True:
    item = input("Item (or 'done' to finish): ").strip()

    if item.lower() == "done":
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

Two details to check.

The `if item:` guard skips empty input, so pressing Enter by accident does not add a
blank item. An empty string counts as `False` in an `if` (people say it is "falsy"), so
the guard only lets real text through.

And `sorted(shopping)` rather than `shopping.sort()`, because sorting the original would
change the order the user entered them in, and the exercise prints both orders. Ask
yourself which one you want and why. If you only needed the sorted
version, `shopping.sort()` would be fine and would save a copy.

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

`if scores:` works because an empty list counts as `False` in an `if` (it is "falsy"),
just like an empty string. Both ways of writing the guard work, and this one is shorter
than `if len(scores) > 0`.

### 5.8 Remove the duplicates

```python
items = ["apple", "banana", "apple", "cherry", "banana", "apple"]

unique = []

for item in items:
    if item not in unique:
        unique.append(item)

print(unique) # ['apple', 'banana', 'cherry']
```

The `not in` check against the growing list is the whole technique. Note that this is
slow for large lists, since every item has to be checked against
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

The two negative numbers do different jobs. The middle
one is the stop value and the last one is the step. Print the
range with `list()` before writing the loop to see what it gives.

A common wrong answer is `range(len(items), 0, -1)`. It starts one position too far to
the right, so the first `items[i]` is an `IndexError`. It also stops one too early, so
it would never reach position 0. If you made this mistake, debugging it taught you more
than getting it right the first time.

Once it works, look at `items[::-1]`. Leaving the start and stop empty and using a step
of `-1` gives a reversed copy, and this slicing version is what people usually write.

### 5.10 Biggest, the hard way

```python
numbers = [4, 7, 2, 9, 4]

biggest = numbers[0]

for number in numbers:
    if number > biggest:
        biggest = number

print(biggest) # 9
```

The starting value matters. Starting at `0` works
for lists with positive numbers and fails for lists of all negative numbers, because 0
is bigger than all of them and never gets replaced.

Starting at `numbers[0]` fixes it, because the first element is a real value from
the list and the comparisons after it will do the right thing.

There is one special case. If the list is empty, `numbers[0]` is an `IndexError`. So the
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
for that list shows why the start value matters.

### 5.11 Word lengths

```python
sentence = input("Sentence: ").strip()
words = sentence.split()

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
It is one pattern, not two.

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

Filter and transform in one loop. The square of a negative number is positive,
so the output is all positive even though the input was all negative. If you expected
negative numbers, remember that a square is never negative.

If you ever write a negative number directly, use brackets: `(-7) ** 2` is `49`, but
`-7 ** 2` is `-49`, because `**` has higher precedence than the minus sign. Here
`number ** 2` is safe because `number` is a variable that holds the whole value.

### 5.13 Insert and delete

```python
names = ["Ada", "Grace", "Alan", "Edsger", "Barbara"]

names.append("Donald")
names.insert(0, "Katherine")
names.remove("Alan")

last = names.pop()

print(f"Removed: {last}")
print(names)
print(len(names))
```

If you called `remove()` with a name that is not in the list, you got a `ValueError`.
Hitting that error taught you how `remove()` behaves.

Ask yourself what `names.remove("Ada")` does if there are two Adas in
the list. It removes only the first one. This is a common
source of bugs, and it is easy to check.

### 5.14 Sort by length

```python
words = ["apple", "banana", "cherry", "fig", "kiwi"]

print(sorted(words)) # alphabetical
print(sorted(words, key=len)) # shortest first
print(sorted(words, key=len, reverse=True)) # longest first
```

`key=len` means "when deciding the order, use the length of each item rather than the
item itself". Python calls `len()` on each word, sorts by those numbers, and gives you
back the words.

In your own words, it is a way of telling `sorted()` what to compare.

The output of the second line is `['fig', 'kiwi', 'apple', 'banana', 'cherry']`. When
two items tie, Python keeps their original order. Here `banana` and `cherry` both have
length 6, and `banana` stays first. This is called a stable sort (a sort that keeps
the original order of equal items).

---

## Stretch

### 5.15 Report card

```python
names = []
scores = []

count = int(input("How many students? "))
for i in range(count):
    names.append(input(f"Name {i + 1}: ").strip())
    scores.append(float(input(f"Score {i + 1}: ")))

pairs = []
for i in range(len(names)):
    pairs.append([scores[i], names[i]])

pairs.sort(reverse=True)

print()
for pair in pairs:
    print(f"{pair[1]:<10} {pair[0]:>5.1f}")
```

The trick is to store the score first in each pair, so that the normal sort puts them
in score order. Python sorts lists of lists by comparing the first item of each, then
the second if the first ties.

That is why the pair is `[score, name]` and not `[name, score]`. If you build it the
other way round, it sorts alphabetically by name. That is a common first attempt.

On the formatting, `{pair[1]:<10}` left-aligns the name in a width of 10, and
`{pair[0]:>5.1f}` right-aligns the score in a width of 5 with one decimal. The `<` and
`>` are the alignment markers. Without them, numbers align right and text aligns left by
default, which often looks fine anyway. The exact spacing does not matter for the
exercise.

The awkwardness here is the point. Two parallel lists are a poor design,
and keeping them in step by hand easily goes wrong. It would be easy to append a
name without appending the matching score, and then the data is wrong. Unit 07 gives a
much better answer.

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

Here `second` starts as `None`, which means "nothing here yet" (see the glossary). The
check `second is None` is how the code asks "have I found a second value yet?"

The logic is that when you find a new biggest, the old biggest becomes the second
biggest. The `elif number < biggest` is what excludes duplicates, which is why `[5, 5,
3]` gives 3 rather than 5.

This never sorts and never uses `max()`, so it follows the rules of the exercise.
Trace `[5, 5, 3]` by hand and write down `biggest` and `second` after each step.

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

Because both lists are already sorted, the smallest remaining item in
each list is always at its current index. So comparing `a[i]` with `b[j]` tells you
which one is the next smallest overall.

The two loops at the end are the part people forget. When one list runs out, the other
still has items, and they are already in order, so they can just be appended.

This is the merge step of merge sort, one of the standard sorting
algorithms. It is also used to sort very large amounts of data.

Trace it with the small lists by hand, writing out `i` and `j` at each step.
After four or five steps, the pattern becomes clear.

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

The awkward part is writing out the last run after the loop. The last run never gets
written inside the loop, because there is no next character to trigger the `else`. That
"and then handle the last one" shape is very common in string and list processing.

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
a bit more care, and you can try it as an extra challenge.

Also note `character * count`, which is string repetition
from unit 01, and it is exactly the tool for this.
