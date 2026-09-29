# Unit 07 — Dictionaries and tuples

**Goal for the session.** They can store data by name instead of by position, which is
the thing that makes programs deal with real information rather than lists of numbers.

**Time.** Two sessions.

**Prerequisites.** Unit 06. Functions, returning values.

**Files used.** `code/dict_basics.py`, `code/dict_methods.py`, `code/dict_patterns.py`,
`code/tuples.py`

---

## 0. Warm-up

Have them write a function `is_even(n)` that returns a boolean (a value that is True or
False), and use it in a loop to print the even numbers from 1 to 20. That is the unit 06
retrieval check, and the return-not-print habit is the thing to confirm.

Then ask them this. "Store the marks for five subjects. Each subject has a name and a
score." They will reach for two parallel lists, because that is what unit 05 taught. Let
them feel how awkward it is. That is today's motivation.

## 1. What a dictionary is

A dictionary (a collection you look things up in by name) stores values by name rather
than by position.

```python
student = {
    "name": "Ada",
    "age": 36,
    "subject": "maths",
}
```

The shape. Curly brackets, then `key: value` pairs separated by commas. The keys (the
name you look things up by) are usually strings. The values can be anything.

The comparison worth spelling out, using the parallel lists.

```python
# unit 05 way
names = ["Ada", "Grace"]
scores = [88, 95]

# unit 07 way
scores = {"Ada": 88, "Grace": 95}
```

The second one cannot get out of sync with itself, because the name and the score are
one thing rather than two things that have to be kept in step by hand. That is the whole
reason dictionaries exist.

Note the terminology once. Key and value. The key is what you look things up by, the
value is what you get back.

## 2. Getting things out

Open `code/dict_basics.py`.

```python
student = {"name": "Ada", "age": 36, "subject": "maths"}

print(student["name"])      # Ada
print(student["age"])       # 36
```

Unlike a list, the position is not a number. It is the key.

Have them try a key that is not there.

```python
print(student["colour"])     # KeyError
```

Read the error out loud. It names the missing key, which is unusually helpful.
`KeyError: 'colour'` tells you exactly what to fix.

Compare with a list. A list with a bad index (a position, starting at 0) gives
`IndexError` and tells you the number, which is less useful because the number is rarely
a typo. A dictionary with a bad key gives `KeyError` and tells you the key, which is
usually a typo, so the message points straight at the problem.

### `.get()`, for when you are not sure

```python
student = {"name": "Ada"}

print(student.get("name"))           # Ada
print(student.get("colour"))         # None, no error
print(student.get("colour", "unknown"))   # unknown
```

`.get()` gives back `None` if the key is missing, or a default you supply. It does not
raise.

When to use which. Use `student["name"]` when the key must be there and a crash is the
right response to it not being. Use `.get()` when a missing key is a normal situation.

That distinction is worth stating clearly, because beginners often learn `.get()` and
then use it everywhere, which hides real bugs. A missing key that should have been there
is a problem, and crashing is how you find out.

### Checking whether a key is there

```python
student = {"name": "Ada"}

print("name" in student)      # True
print("colour" in student)    # False
```

Note that `in` checks the **keys** by default, not the values. That is a common
confusion. `"Ada" in student` is `False`, because `"Ada"` is a value, not a key.

For values there is `.values()`, which they will meet in a moment.

```python
print("Ada" in student.values())    # True
```

## 3. Changing a dictionary

Open `code/dict_methods.py`.

```python
student = {"name": "Ada"}

student["age"] = 36          # adding a new key
student["name"] = "Grace"    # changing an existing key
del student["age"]           # removing a key
```

Adding and updating look identical, which is convenient. If the key is there, it is
replaced. If it is not, it is created.

Have them add a key, change it, delete it, and print the dictionary after each step so
they can see it changing. That is the same "print the list after every step" habit from
unit 05 and it works just as well here.

Other useful methods.

```python
student = {"name": "Ada", "age": 36}

print(len(student))          # 2, how many key-value pairs
print(student.keys())        # dict_keys(['name', 'age'])
print(student.values())      # dict_values(['Ada', 36])
print(student.items())       # dict_items([('name', 'Ada'), ('age', 36)])
```

Those outputs look strange. `dict_keys` is not a list, though it behaves like one in a
loop. The trick that makes them useful.

```python
print(list(student.keys()))      # ['name', 'age']
```

Worth showing once, so the strange output does not alarm them.

One more.

```python
student = {"name": "Ada", "age": 36}
removed = student.pop("age")

print(removed)     # 36
print(student)     # {'name': 'Ada'}
```

`pop()` works on dictionaries too, and it takes a key rather than a position.

## 4. Looping over a dictionary

This is where most of the value is.

```python
scores = {"Ada": 88, "Grace": 95, "Alan": 72}

for name in scores:
    print(name)
```

Just the keys. Then values.

```python
for score in scores.values():
    print(score)
```

And the one they will use most.

```python
for name, score in scores.items():
    print(f"{name} scored {score}")
```

`items()` gives back pairs, and the `for name, score in` unpacks (take apart into
separate variables) each pair. That unpacking comes from tuples (like a list that cannot
be changed), which is section 6, so it is worth saying "these two variables come as a
pair and the loop separates them" and moving on.

Have them trace it. `name` gets `"Ada"` and `score` gets `88`, then the next pass, and
so on.

If they write `for item in scores.items():` and then use `item[0]` and `item[1]`, that
also works and is worth showing once so the pair form makes sense.

### A note on order

Dictionaries in modern Python remember the order you added things in. That is convenient
but it is not a promise you should rely on. If the order matters, sort the keys.

```python
for name in sorted(scores):
    print(f"{name} scored {scores[name]}")
```

## 5. The counting pattern

Open `code/dict_patterns.py`. This is the single most useful dictionary technique, and
it is worth the whole session on its own.

Counting how many times each thing appears in a list.

```python
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]

counts = {}

for word in words:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1

print(counts)     # {'apple': 3, 'banana': 2, 'cherry': 1}
```

Trace it on paper for the first three words. The dictionary starts empty. The first
`"apple"` is not in it, so it is set to 1. The second `"apple"` is in it, so it goes up
to 2. And so on.

The shorter version with `.get()`.

```python
counts = {}

for word in words:
    counts[word] = counts.get(word, 0) + 1
```

Read that out loud. "Set this word's count to whatever it currently is, or zero if it is
not there, plus one." It is dense and it is what everyone writes once they are
comfortable. Show both, let them use either, and make sure they can explain the
`.get(word, 0)` part.

This pattern generalises to all sorts of things. Counting words in a text, counting
votes, counting how many times a value appears. It is worth having them do it from
scratch a few times rather than copying it.

### Grouping

The same shape, with values that are lists.

```python
words = ["apple", "avocado", "banana", "blueberry", "cherry"]

by_letter = {}

for word in words:
    first = word[0]
    if first not in by_letter:
        by_letter[first] = []
    by_letter[first].append(word)

print(by_letter)
# {'a': ['apple', 'avocado'], 'b': ['banana', 'blueberry'], 'c': ['cherry']}
```

This one is more advanced because of the empty list that has to be created before you
can append to it. Trace it carefully. The pattern of "make sure the container exists,
then add to it" appears constantly.

## 6. Tuples

Open `code/tuples.py`.

A tuple is like a list that cannot be changed.

```python
point = (3, 4)
print(point[0])       # 3
print(len(point))     # 2

# point[0] = 5        # TypeError
```

Round brackets instead of square. Immutable (cannot be changed), like strings and unlike
lists.

They have already been using tuples without knowing it.

```python
def min_and_max(numbers):
    return min(numbers), max(numbers)

low, high = min_and_max([3, 1, 4, 1, 5])
```

That `return` with a comma makes a tuple. And the assignment on the other side unpacks
it.

```python
point = (3, 4)
x, y = point
```

Which is the same thing as.

```python
x = point[0]
y = point[1]
```

And this, which they met in unit 01.

```python
a, b = b, a
```

That is tuple unpacking doing the swap.

### When to use a tuple rather than a list

The honest answer for beginners. Use a list unless you have a specific reason not to. A
tuple is right when the items are a fixed set that belong together and the order has
meaning, like coordinates in `(x, y)`, or a name and a score as a pair.

The practical difference. A list is a collection of things you might add to or remove
from. A tuple is a fixed group of things. If you find yourself wanting to append to it,
it should have been a list.

Do not make them memorise rules. Give them the feel for it and let it settle over time.
Also worth noting that a function returning several values is the most common place they
will actually create a tuple, so they are already using them.

### A small neat thing

```python
point = (3, 4)
print(point)              # (3, 4)

single = (5)
print(type(single))       # int, not a tuple! The brackets are just grouping

actual_single = (5,)
print(type(actual_single))    # tuple
```

The trailing comma is what makes a one-item tuple. This catches people out occasionally
and it is funny enough to be memorable.

## 7. Choosing between the three

A short discussion, worth having spelled out.

**List.** An ordered collection of things of the same kind, where you might add or
remove, and where position matters. `["a", "b", "c"]`, a list of scores, a list of
names.

**Dictionary.** A collection you look things up by name. `{"Ada": 88}`, a phone book, a
configuration, anything where you ask "what is the value for this key".

**Tuple.** A small fixed group of related values. `(3, 4)` coordinates, a name and age
as a pair.

A good question to ask them. "If I have a list of students and each one has a name and a
score, what should the data look like?" The answer is a list of dictionaries, which is
the shape of the next section.

## 8. Combining them

A list of dictionaries, which is how most real data looks.

```python
students = [
    {"name": "Ada", "score": 88},
    {"name": "Grace", "score": 95},
    {"name": "Alan", "score": 72},
]

for student in students:
    print(f"{student['name']} scored {student['score']}")
```

Note the quotes inside the f-string. `student['name']` needs the inner quotes to be
different from the outer ones, or you get a mess. Have them hit that problem and fix it,
because it comes up constantly.

And a dictionary of dictionaries.

```python
grades = {
    "Ada": {"maths": 90, "english": 85},
    "Grace": {"maths": 95, "english": 92},
}

print(grades["Ada"]["maths"])     # 90
```

Same double indexing idea as `grid[2][1]` from unit 05, but with names instead of
positions. That is a good moment to note that the shape of the code is the same, and
only the thing in the brackets has changed.

## 9. Putting it together

Build a word frequency counter together.

```python
text = input("Enter some text: ").lower()

words = text.split()
counts = {}

for word in words:
    word = word.strip(".,!?;:")
    if word:
        counts[word] = counts.get(word, 0) + 1

print(f"\n{len(counts)} different words\n")

for word, count in sorted(counts.items(), key=lambda pair: pair[1], reverse=True):
    print(f"{word:15} {count}")
```

That `lambda` is beyond them, so either skip the sorting by count, or write it out
properly.

```python
pairs = []
for word, count in counts.items():
    pairs.append([count, word])

pairs.sort(reverse=True)

for count, word in pairs:
    print(f"{word:15} {count}")
```

Which uses only things they already know, and is a nice callback to exercise 5.15. That
is the version to teach.

Then extend it together.

- Show the ten most common words.
- Ignore very short words.
- Count letters instead of words, which is the same pattern.
- Ask for a second text and count both together.

---

## Teaching notes for this unit

**The parallel list comparison is the motivation, and it should come from them.** Ask
them how they would store a name and a score together before showing them dictionaries,
and let the awkwardness of their answer do the work.

**`KeyError` versus `.get()` is a judgement call, not a rule.** The dangerous habit is
using `.get()` everywhere to avoid crashes. A missing key that should have been there is
a bug, and crashing is how you find out. Say that clearly.

**`in` checks keys, not values.** This catches almost everybody. Say it when you
introduce `in`, and expect to say it again.

**The counting pattern is the highest value thing in the unit.** Make them write it from
scratch, trace it on paper, and then use it in three different exercises. It comes up
everywhere.

**Tuple unpacking is mostly free.** They have been using it since unit 01 with `a, b =
b, a` and since unit 06 with multiple returns. The formal name and the comparison to
lists is all that is new.

**Do not teach `defaultdict` or `Counter`.** They are the standard library answers to
the counting pattern, and they are really better, and they belong in unit 09 or later
once the manual version is solid.

**Do not teach `lambda`.** The sorting-by-value exercise has a version using only known
syntax, and that is the one to use. Show the `lambda` version for ten seconds if they
are curious, and say it is a later thing.

**The list of dictionaries is what real data usually looks like,** and it is worth
showing even if there is no time for exercises with it. Almost everything they will ever
load from a file or an API looks like that.

**Exercise 7.4, the `sum()` third way.** Mention it once they have the loop working.

**Exercise 7.8, the `zip` shortcut.** Do not teach it here, but it is worth knowing that the ugly version is not the only option.

**Exercise 7.17, the `dict(first)` copy.** Worth re-testing their understanding here.

**Exercise 7.19, the unhashable list error.** That error is worth explaining if it comes up.

**Preview of next unit.** They can represent data properly. Next session they read it
from files and write it back, and they learn to handle the input being wrong without the
program falling over.
