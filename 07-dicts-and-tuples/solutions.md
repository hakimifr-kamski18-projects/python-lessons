# Unit 07 solutions

## Warm-ups

### 7.1 Predict the output

```python
person = {"name": "Ada", "age": 36, "city": "London"}
```

| Expression | Result |
| --- | --- |
| `person["name"]` | `'Ada'` |
| `len(person)` | `3` |
| `"age" in person` | `True` |
| `"Ada" in person` | `False`, it checks keys |
| `"Ada" in person.values` | `True`, this one checks the values |
| `person.get("job")` | `None` |
| `person.get("job", "none")` | `'none'` |

The two `in` lines are the lesson. `"Ada" in person` is `False` because `"Ada"` is a
value and `in` looks at keys by default. This surprises almost everybody, and the fix is
`.values`.

Some students expect `len(person)` to count the values or the characters. It counts
key-value pairs, so three.

### 7.2 Predict the output

```python
counts = {"a": 1, "b": 2}
counts["a"] += 1
counts["c"] = 3
print(counts)
```

```python
{'a': 2, 'b': 2, 'c': 3}
```

`counts["a"] += 1` is the same as `counts["a"] = counts["a"] + 1`, so it reads the
current value, adds one, and puts it back under the same key. Then `counts["c"] = 3`
creates a new key, since `"c"` was not there.

The order of the output follows the order the keys were created, since modern Python
dictionaries remember that. Do not rely on it, but do not be surprised by it.

### 7.3 Unpacking

It prints.

```
Ada 88
Grace 95
```

And `pairs[0]` on its own is a tuple, `('Ada', 88)`.

The line `for name, score in pairs:` is doing two things at once. It takes each item in
turn, which is a tuple of two things, and then splits it into two variables. The name
and score are separated by the comma in the `for` line, matching the comma in the pair.

Try `for item in pairs: print(item)` to see the tuple before unpacking.

### 7.4 Find the bug

```python
scores = {"Ada": 88, "Grace": 95}
total = 0

for score in scores:
    total += score
```

The error is a `TypeError` about unsupported operand types for `+=`, `int` and `str`.

The cause is that looping over a dictionary directly gives you the **keys**, not the
values. So `score` holds `"Ada"` on the first pass, and adding a string to an integer is
the same `TypeError` you met back in unit 01.

The first fix, ask for the values.

```python
for score in scores.values:
    total += score
```

The second fix, loop over keys and look up each value.

```python
for name in scores:
    total += scores[name]
```

Both are correct. The first is shorter and clearer when you want only the values. The
second is what you need when you want the name as well, which is most of the time.

There is a third way, which is `sum(scores.values)`.

The variable name `score` is also misleading in the original, since it actually holds a
name. Naming things accurately would have made this bug clear much sooner, and that is a
good lesson in itself.

### 7.5 Find the bug, part two

```python
student = {"name": "Ada"}
student = student["age"] = 36
```

It fails with a `TypeError` about an `int` object not supporting item assignment.

The line is a chained assignment, the same kind as `a = b = 0`, which means "give this
value to both targets". Python assigns to the targets left to right, so `student` gets
the number 36 first. By the time the second target runs, `student` is no longer a
dictionary, it is an integer, and `36["age"] =...` makes no sense.

It should be two separate statements (one complete instruction each).

```python
student = {"name": "Ada"}
student["age"] = 36
```

Which is the ordinary way of adding a key, and it is what you should write. The chained
version was a way of trying to do two unrelated things at once, and there is no reason
to.

---

## Core

### 7.6 Phone book

```python
phone_book = {
    "Ada": "555-0101",
    "Grace": "555-0102",
    "Alan": "555-0103",
}

while True:
    name = input("Name (or 'quit'): ").strip

    if name.lower == "quit":
        break

    if name in phone_book:
        print(f"{name}: {phone_book[name]}")
    else:
        print(f"No entry for {name}")

    print()
```

The `if name in phone_book` check is the point of the exercise. It is the safe way to
look something up, and it lets you print a sensible message rather than crashing.

The alternative using `.get`.

```python
    number = phone_book.get(name, "no entry")
    print(f"{name}: {number}")
```

Which is shorter, and it loses the ability to respond differently to a miss. Both are
fine. Ask yourself which you prefer and why. The version with the `in` check is usually
better when the two cases need different output.

One more thing worth checking. The user types `ada` lowercase, and the dictionary has
`Ada`. That is a miss. If you want the lookup to be case insensitive, you either
lowercase the keys when building the dictionary or lowercase both sides when comparing.
This is worth noticing, since it is the same class of problem as the `strip()` and
`lower()` issues from unit 02.

### 7.7 Word count

```python
sentence = input("Sentence: ").lower.strip
words = sentence.split

counts = {}

for word in words:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1

for word, count in counts.items:
    print(f"{word} {count}")
```

For `the cat and the dog`, this prints `the 2`, then the others with 1.

The `.lower` is essential, since `The` and `the` would otherwise be different keys. The
`.strip` handles a trailing space, which would produce an empty string as the last word
and count it.

Checking for the empty string is worth doing if you left the `.strip` off.

```python
for word in words:
    if word:
        ...
```

Since an empty string is falsy, that guard skips it.

If you want the output in a fixed order, `for word in sorted(counts):`.

### 7.8 Two lists into a dictionary

```python
names = ["Ada", "Grace", "Alan"]
scores = [88, 95, 72]

result = {}

for i in range(len(names)):
    result[names[i]] = scores[i]

print(result) # {'Ada': 88, 'Grace': 95, 'Alan': 72}
```

The index loop is the right tool here, and this is a genuine case of needing the
position, even though unit 05 said to avoid it. The reason is that you are walking two
lists at once, so you need a shared index.

There is a neater way, using `zip`, which is a unit 09 thing.

```python
result = dict(zip(names, scores))
```

The answer to the second part of the exercise. In exercise 5.15 you were keeping two
parallel lists and then trying to sort one while keeping the other in step. The right
answer was to build a single dictionary, or a list of dictionaries, so that the name and
score travel together. Two parallel lists are a design mistake from the start, not a
problem you fix afterwards. That is exactly why dictionaries exist.

### 7.9 Inventory

```python
inventory = {"apples": 5, "bananas": 3, "cherries": 12}

inventory["apples"] += 4
print(inventory)

del inventory["bananas"]
print(inventory)

inventory["dates"] = 7
print(inventory)

total = 0
for count in inventory.values:
    total += count

print(f"Total items: {total}") # 28
```

After the changes, the inventory is `{'apples': 9, 'cherries': 12, 'dates': 7}`, which
adds up to 28.

The `for count in inventory.values` loop is the accumulator pattern from unit 04,
applied to a dictionary. Note that `sum(inventory.values)` does the same thing in one
line, and both are worth knowing.

The distinction the exercise is testing. `len(inventory)` is 3, the number of kinds of
fruit. The loop gives 28, the number of pieces of fruit. Those are different questions
and it is easy to answer the wrong one by accident.

### 7.10 Letter frequency

```python
text = input("Text: ").lower

counts = {}

for character in text:
    if character == " ":
        continue
    if character in counts:
        counts[character] += 1
    else:
        counts[character] = 1

for letter in sorted(counts):
    print(f"{letter} {counts[letter]}")
```

For `hello`, the output is `e 1`, `h 1`, `l 2`, `o 1`, in alphabetical order.

The `continue` skips spaces. An alternative is to not count them at all.

```python
if character.isalpha:
```

Which would also skip punctuation and digits, and is probably what you want in real
code. `.isalpha` is worth knowing alongside `.isdigit` from unit 04.

Sorting the keys before printing is what gives the alphabetical order, since
dictionaries remember insertion order and `hello` would otherwise come out as `h`, `e`,
`l`, `o`.

### 7.11 Votes

```python
votes = {}

while True:
    name = input("Candidate (or 'done'): ").strip

    if name.lower == "done":
        break

    if not name:
        continue

    votes[name] = votes.get(name, 0) + 1

print()
for name, count in votes.items:
    print(f"{name}: {count}")

# find the winner
if votes:
    top_count = 0
    for name, count in votes.items:
        if count > top_count:
            top_count = count
            winner = name

    winners = []
    for name, count in votes.items:
        if count == top_count:
            winners.append(name)

    if len(winners) == 1:
        print(f"\nWinner: {winners[0]}")
    else:
        print(f"\nTie between: {', '.join(winners)}")
```

The counting uses `.get(name, 0) + 1`, which is the pattern from the lesson.

The winner logic finds the top count first, then collects everyone who has that count.
Doing it in that order is what handles ties correctly. A version that just tracked "the
biggest so far" and overwrote the winner would silently pick whichever tied candidate
came last, which is the wrong answer.

This is worth noticing. Being asked to handle ties forces you to write slightly more
code, and it produces a better answer. Real specifications are full of these little
details.

`", ".join(winners)` is the join from unit 02, doing real work.

### 7.12 Grade book

```python
grades = {
    "Ada": {"maths": 90, "english": 85},
    "Grace": {"maths": 95, "english": 92},
}

student = input("Student: ").strip.title
subject = input("Subject: ").strip.lower
score = int(input("Score: "))

if student not in grades:
    grades[student] = {}

grades[student][subject] = score

print()
for name, subjects in grades.items:
    total = 0
    for subject, score in subjects.items:
        total += score
    average = total / len(subjects)
    print(f"{name}: average {average:.1f}")
```

The key line is the guard.

```python
if student not in grades:
    grades[student] = {}
```

If the student is new, you have to create the inner dictionary before you can add
anything to it. The next line `grades[student][subject] = score` reaches into the inner
dictionary by name and adds a key, and it needs the inner dictionary to exist first.

That is exactly the grouping pattern from the lesson, one level deeper. It is worth
noticing the connection, because "make sure the container exists before adding to
it" is a shape that keeps coming back.

The `title()` on the student name and the `lower()` on the subject keep the dictionary keys
consistent, so `ada` and `Ada` do not become two different students.

### 7.13 Sort by value

```python
scores = {"Grace": 95, "Ada": 88, "Alan": 72}

pairs = []
for name, score in scores.items:
    pairs.append([score, name])

pairs.sort(reverse=True)

for score, name in pairs:
    print(f"{name}: {score}")
```

Output.

```
Grace: 95
Ada: 88
Alan: 72
```

The answer to the question. Python sorts lists by comparing them item by item, starting
with the first. If the first items are equal, it compares the second, and so on. So
putting the score first means the list is sorted by score. Putting the name first would
sort alphabetically by name instead.

That "compare the first, then the second to break ties" behaviour is really useful. If
two students tie on score, they will be ordered alphabetically by name, which is a nice
accident.

If you want ascending, drop the `reverse=True`.

---

## Stretch

### 7.14 Group by first letter

```python
words = ["apple", "banana", "avocado", "cherry", "blueberry"]

groups = {}

for word in words:
    first = word[0]
    if first not in groups:
        groups[first] = []
    groups[first].append(word)

for letter in sorted(groups):
    print(f"{letter}: {', '.join(sorted(groups[letter]))}")
```

Output.

```
a: apple, avocado
b: banana, blueberry
c: cherry
```

The `", ".join(...)` works here because the values are lists of strings. That
combination of sorting, joining, and looping over a dictionary is a good consolidation
of the last few units.

### 7.15 The most common word

```python
text = input("Text: ").lower
counts = {}

for word in text.split:
    word = word.strip(".,!?;:")
    if word:
        counts[word] = counts.get(word, 0) + 1

pairs = []
for word, count in counts.items:
    pairs.append([count, word])

pairs.sort(reverse=True)

print(f"Most common: {pairs[0][1]} ({pairs[0][0]} times)")
print(f"Second: {pairs[1][1]} ({pairs[1][0]} times)")
```

Answers to the questions.

The second most common is `pairs[1]`, since the list is sorted by count.

For a tie, the sort compares the second item of each pair, which is the word, and sorts
them in reverse alphabetical order because of `reverse=True`. So for two words with the
same count, whichever is later alphabetically comes first. Which one comes first does
not matter, but it is predictable, and the trick with `reverse=True` on a pair is worth
noticing. It reverses the tie-breaking order too, which is sometimes not what you want.

If you want ties broken alphabetically in the normal direction, you need to sort in
two passes, or use a `key`. Both are beyond this course. Noticing that the problem
exists is the point.

The `pairs[0][1]` syntax looks ugly. Pulling it into variables first reads better.

```python
top_count, top_word = pairs[0]
print(f"Most common: {top_word} ({top_count} times)")
```

### 7.16 Invert a dictionary

```python
original = {"a": 1, "b": 2, "c": 3}

inverted = {}
for key, value in original.items:
    inverted[value] = key

print(inverted) # {1: 'a', 2: 'b', 3: 'c'}
```

For the question about duplicate values.

```python
original = {"a": 1, "b": 1}
inverted = {}
for key, value in original.items:
    inverted[value] = key

print(inverted) # {1: 'b'}
```

Only one entry survives, because a dictionary cannot have duplicate keys. Setting
`inverted[1]` twice just overwrites the first one, and the last key processed wins.

This is a real problem with inverting a dictionary, and it shows well that dictionaries
enforce uniqueness of keys. If you wanted to keep both, the values would have to be
lists, which is the grouping pattern again.

### 7.17 Combined word count

```python
def count_words(text):
    counts = {}
    for word in text.lower.split:
        word = word.strip(".,!?;:")
        if word:
            counts[word] = counts.get(word, 0) + 1
    return counts # return the result

first = count_words(input("First text: "))
second = count_words(input("Second text: "))

combined = dict(first) # a copy of the first

for word, count in second.items:
    combined[word] = combined.get(word, 0) + count

print("\nCombined counts:")
for word in sorted(combined):
    print(f"{word}: {combined[word]}")

print("\nIn both:")
for word in sorted(combined):
    if word in first and word in second:
        print(word)
```

Two things worth checking.

`combined = dict(first)` makes a copy. Without it, `combined = first` would give the
same dictionary a second name, and the next loop would modify `first` as well. That is
the aliasing trap from unit 05, applying to dictionaries in exactly the same way.

The final loop checks membership in both dictionaries. `word in first` works because
`in` checks keys, which is exactly what is wanted.

### 7.18 Word length histogram

```python
sentence = input("Sentence: ").strip

lengths = {}

for word in sentence.split:
    length = len(word)
    lengths[length] = lengths.get(length, 0) + 1

for length in sorted(lengths):
    print(f"{length}: {'*' * lengths[length]}")
```

For `the quick brown fox`, the output is `3: **` and `5: **`.

Two nice things here. The keys of the dictionary are integers rather than strings, which
dictionaries allow. And `'*' * count` is string repetition from unit 01, doing the
actual bar chart.

`sorted(lengths)` sorts the integer keys numerically, which is what you want. If the
keys were strings, they would sort alphabetically, which would put `10` before `2`. That
is a real gotcha when sorting numbers stored as text, and it is worth remembering if you
have hit it.

### 7.19 Tuples as keys

```python
distances = {
    ("London", "Paris"): 344,
    ("Paris", "Berlin"): 878,
}

def distance(city_a, city_b):
    key = tuple(sorted([city_a, city_b]))
    return distances.get(key, "unknown")

print(distance("London", "Paris")) # 344
print(distance("Paris", "London")) # 344
print(distance("London", "Berlin")) # unknown
```

The trick is normalising (putting it in a fixed form so two equal things really are
equal). Because a lookup has to match the key exactly, and a tuple of `("Paris",
"London")` is not the same key as `("London", "Paris")`, you have to put the two cities
into a fixed order before looking up. Sorting them alphabetically does that, so both
orders produce the same key.

Note the `sorted([city_a, city_b])` returns a list, and `tuple(...)` converts it back to
a tuple, because lists cannot be dictionary keys at all. Try it without the
`tuple` and read the error.

Dictionary keys have to be hashable,
which means they cannot be changed, so they can be used as a key. Lists can change, so
they are not allowed as keys. Tuples cannot change, so they are fine.

The concept of normalising data before comparing it, so that two things that should be
equal actually are, is a really useful idea that goes well beyond this exercise. The
`strip.lower` on input from unit 02 is the same idea.
