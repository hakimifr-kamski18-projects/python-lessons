# Unit 05 — Lists

**Goal for the session.** They can hold a collection of values in one variable, walk
through it, add to it, and pull values out of it.

**Time.** Two sessions. Lists are where loops stop being an exercise and start being
useful, so the material is dense and the exercises matter more than the explanations.

**Prerequisites.** Unit 04. Loops, accumulators, `range`.

**Files used.** `code/list_basics.py`, `code/list_methods.py`, `code/list_loops.py`,
`code/list_traps.py` (this one is broken on purpose)

---

## 0. Warm-up

Have them write a loop that sums the numbers 1 to 20 and prints the total. That is the
accumulator pattern from unit 04, and it needs to be automatic before lists make sense.

Then ask the question that motivates today. "What if you had twenty numbers, not 1 to 20
but twenty numbers that could be anything you got from a user? Store them all, then add
them up." Twenty variables is clearly absurd, and that is the point.

## 1. What a list is

Open `code/list_basics.py`.

A list is several values in one variable, in order.

```python
numbers = [1, 2, 3, 4, 5]
names = ["Ada", "Grace", "Alan"]
mixed = [1, "two", 3.0, True]
empty = []
```

The square brackets make a list. Commas separate the items. The items can be any type,
and they can be mixed, though a mixed list is usually a sign that something is confused.

They have already met lists several times without knowing it. `split()` gives one, and
`in ["yes", "y"]` from unit 03 is one. Point that out.

### Getting things out

Exactly the same as strings, which is deliberate.

```python
names = ["Ada", "Grace", "Alan"]

print(names[0])      # Ada
print(names[2])      # Alan
print(names[-1])     # Alan, the last one
print(len(names))    # 3
print(names[0:2])    # ['Ada', 'Grace'], a slice (a piece cut out) is also a list
```

Ask them to predict `names[3]` before running. It is an `IndexError`, and the reason is
the same one as with strings. Positions start at zero.

Have them say the sentence again. The first item is at position zero.

### The big difference from strings. Lists can be changed

```python
names = ["Ada", "Grace", "Alan"]
names[0] = "Katherine"

print(names)     # ['Katherine', 'Grace', 'Alan']
```

This is a real difference from unit 02, where `word[0] = "J"` was a `TypeError`. Strings
are immutable (cannot be changed) and lists are not. Have them try the string version
again if they have forgotten, and put the two side by side.

```python
word = "Ada"
word[0] = "K"     # TypeError, strings cannot be changed

names = ["Ada", "Grace", "Alan"]
names[0] = "K"    # works fine
```

That contrast is the lesson. Give them the words, mutable (can be changed) and
immutable, once, and then use the words so they stick.

## 2. List methods

Open `code/list_methods.py`. This is a big block, so introduce the methods in groups and
let them try each one rather than reading a wall of code.

### Adding things

```python
names = ["Ada", "Grace"]

names.append("Alan")        # add to the end
print(names)                # ['Ada', 'Grace', 'Alan']

names.insert(0, "Katherine")    # insert at a position
print(names)                # ['Katherine', 'Ada', 'Grace', 'Alan']
```

`append()` is the one they will use constantly. Note that `append()` takes the item
itself, so `names.append("Alan")` and not `names.append(["Alan"])`, which would add a
list inside a list.

### Removing things

```python
names = ["Ada", "Grace", "Alan"]

names.remove("Grace")       # remove by VALUE
print(names)                # ['Ada', 'Alan']

last = names.pop()          # remove and give back the LAST item
print(last)                 # 'Alan'
print(names)                # ['Ada']

names.pop(0)                # remove and give back the item at position 0
```

The distinction worth making. `remove()` takes the value and finds it. `pop()` takes a
position and gives you back what it removed. `pop()` with nothing in the brackets is the
last item.

### Now the important discovery

Unlike string methods, list methods mostly change the list in place (changed directly,
without a copy). Have them predict this before running it, based on unit 02 where
`name.upper()` changed nothing.

```python
names = ["Ada", "Grace"]
names.append("Alan")
print(names)     # ['Ada', 'Grace', 'Alan']
```

It did change. `append()` returns `None` and modifies the list itself. String methods
return new strings and leave the original alone. Lists do not.

Which produces this classic bug.

```python
names = ["Ada", "Grace"]
names = names.append("Alan")     # names is now None
print(names)                     # None
print(len(names))                # TypeError
```

Have them run it. This mistake is worth the ten minutes it takes to untangle, because it
follows directly from unit 02's lesson and shows that the two rules do not agree. Do not
apologise for the inconsistency, name it. Some methods return new values and some change
things in place, and the way to know is to check.

The rule of thumb. In Python, most of the method names that sound like commands
(`append`, `sort`, `reverse`) change the thing. The ones that sound like descriptions
(`upper`, `split`) give you back something new.

### Sorting and reversing

```python
numbers = [3, 1, 4, 1, 5, 9, 2, 6]

numbers.sort()
print(numbers)              # [1, 1, 2, 3, 4, 5, 6, 9]

numbers.sort(reverse=True)
print(numbers)              # [9, 6, 5, 4, 3, 2, 1, 1]

numbers.reverse()
print(numbers)              # back to ascending, but not sorted
```

Two things.

`reverse()` reverses the order. `sort(reverse=True)` sorts and then reverses, which is
different. Have them do `reverse()` on an unsorted list to see the difference. A common
beginner belief is that `reverse()` sorts descending, and it does not.

And `sorted()` as an alternative that does not change the original.

```python
numbers = [3, 1, 4]
print(sorted(numbers))      # [1, 3, 4]
print(numbers)              # [3, 1, 4], untouched
```

### Asking questions

```python
numbers = [3, 1, 4, 1, 5]

print(len(numbers))         # 5
print(3 in numbers)         # True
print(10 in numbers)        # False
print(numbers.count(1))     # 2
print(numbers.index(4))     # 2, the position of the first 4
print(sum(numbers))         # 14
print(min(numbers))         # 1
print(max(numbers))         # 5
```

`sum`, `min` and `max` are built in and free. Have them redo one of their unit 04
accumulator exercises using `sum()` and compare the two. The loop version still matters,
because sometimes you need to do something more complicated than adding up, but knowing
that `sum()` exists saves a lot of code.

`index()` raises a `ValueError` if the item is not there, which is a different error
from the `IndexError` you get from a bad position. Worth letting them see both, since
the names are confusingly similar.

## 3. Loops and lists together

Open `code/list_loops.py`. This is where the unit pays off.

A loop over a list, without `range` and without indices (positions, starting at 0).

```python
names = ["Ada", "Grace", "Alan"]

for name in names:
    print(f"Hello, {name}!")
```

Point out that there is no `range`, no `len`, and no index. The loop variable `name`
takes each item in turn. This is the natural way to loop over a list, and it is what
they should reach for by default.

Compare with the indexed version, which is more work and rarely needed.

```python
for i in range(len(names)):
    print(f"{i}: {names[i]}")
```

Show it once, say it is occasionally necessary, and say that reaching for it by habit is
a mistake. If they write this version when they do not need the index, ask them what the
extra machinery is buying them.

### Building a list in a loop

The accumulator pattern, but with a list.

```python
squares = []

for number in range(1, 6):
    squares.append(number ** 2)

print(squares)     # [1, 4, 9, 16, 25]
```

This is a very common shape. Start with an empty list, append inside the loop, use the
list afterwards. Have them trace it once.

### Filtering

```python
numbers = [4, 7, 2, 9, 4, 1, 8]

evens = []
for number in numbers:
    if number % 2 == 0:
        evens.append(number)

print(evens)       # [4, 2, 4, 8]
```

Same shape, with a condition. Building a new list from an old one, keeping only what
passes a test. This is one of the most common things a program does.

### Transforming

```python
names = ["ada", "grace", "alan"]

loud = []
for name in names:
    loud.append(name.upper())

print(loud)        # ['ADA', 'GRACE', 'ALAN']
```

And here is the right moment to mention the shortcut, once they have done it the long
way.

```python
loud = [name.upper() for name in names]
```

That is a list comprehension (a short way of writing a loop that builds a list). It is
short and it is everywhere in real Python code, and it is not taught on purpose in this
course. Tell them it exists, tell them they will see it, tell them to write the loop
version for now, and that the comprehension is a unit ten topic once loops feel easy.
Students who have the loop version solid pick up comprehensions in twenty minutes later.
Students who learn comprehensions first often cannot write the loop.

### Looping with the index when you need it

Not for now. If they ask, say there is a tool called `enumerate` and it is a unit 09
thing.

## 4. The traps

Open `code/list_traps.py`. This file is broken on purpose, and it contains a set of
mistakes to work through together. Read the error, predict the fix, then compare.

The three traps it covers.

**Changing a list while looping over it.** Items get skipped, for reasons that are hard
to see. The rule is to loop over a copy (`for n in numbers[:]`) or build a new list.

**Two names for one list.** This is the surprising one.

```python
a = [1, 2, 3]
b = a
b.append(4)
print(a)      # [1, 2, 3, 4]
```

Ask them to predict before running. Most will say `[1, 2, 3]` and be wrong. The
explanation, in one sentence. `b = a` does not copy the list, it gives the same list a
second name. Both names point at the same thing.

The fix if you want a real copy.

```python
b = a[:]        # a slice of the whole thing
b = list(a)     # or this
```

Do not go deep into why. Just make the rule memorable. Assigning a list does not copy
it.

**The off-by-one at the end.**

```python
names = ["Ada", "Grace", "Alan"]
print(names[len(names)])     # IndexError
```

The last valid position is `len - 1`, so the last item is `names[len(names) - 1]`, or
more simply `names[-1]`.

## 5. Lists of lists

Brief, but worth showing so it does not look strange later.

```python
grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

print(grid[0])         # [1, 2, 3]
print(grid[0][0])      # 1
print(grid[2][1])      # 8
```

That double indexing `grid[2][1]` is the same idea as `parts[0][0]` from unit 02, just
one level up. Read it inside out. Take item 2 of the outer list, which is a list, then
take item 1 of that.

A loop over it.

```python
for row in grid:
    for value in row:
        print(value, end=" ")
    print()
```

## 6. Putting it together

Build a small shopping list program together.

```python
shopping = []

while True:
    item = input("Item (or 'done' to finish): ").strip()

    if item.lower() == "done":
        break

    shopping.append(item)

print()
print(f"Your list has {len(shopping)} items:")
for item in shopping:
    print(f"  - {item}")
```

Then extend it together.

- Print the items in alphabetical order with `sorted()`.
- Ask for a price for each item and store the prices in a second list, then print
  the total. Two parallel lists is a slightly awkward design, and it is worth
  letting them feel that, because unit 07 offers a better answer.
- Allow removing an item with a `remove` command.
- Print how many items there are before and after removing one.

---

## Teaching notes for this unit

**The mutability contrast with strings is the core idea.** Everything else is
vocabulary. Spend the time on `word[0] = "K"` failing and `list[0] = "K"` working, and
on `names.append` changing the list while `name.upper` does not.

**`names = names.append("Alan")` will happen, and it deserves real time.** It follows
directly from the correct lesson in unit 02, so it is not carelessness. It is a genuine
inconsistency in the language, name it as such, and give them the rule about
command-sounding names changing things.

**Loop over the list, not the indices.** Students who get into the `range(len(...))`
habit write much clumsier code for the rest of their lives. When you see it and the
index is not needed, ask what the index is for.

**Comprehensions are a deliberate omission.** Mention that they exist, mention that they
will see them, and do not teach them. A student with solid loops learns them in minutes.
A student who skipped loops is stuck.

**The aliasing trap (two names for the same thing) is the most surprising thing in the
unit.** Let them predict wrong, then explain it in one sentence and move on. Do not go
into identity versus equality yet.

**`list_traps.py` is meant to be worked through as a debugging exercise,** not read.
Have them run each broken section, read the error out loud, and predict the fix before
making it.

**If they are flying, the pair of parallel lists is a good stretch,** and it sets up
unit 07 nicely. If they are struggling, skip the list-of-lists section entirely and
spend the time on building lists in loops.

**On why numbers and lists differ, in 5.2.** Do not go deeper than that.

**On the `**` binding detail in 5.12.** Not worth raising unless they ask.

**On `key=len` in 5.14.** Do not go into how `key` works as a function argument, since
`len()` being passed around as a value is a really advanced idea and it can wait.

**On the `second is None` alternatives in 5.16.** Do not insist on any particular
version here.

**Preview of next unit.** They can hold many values. Next session they learn to name a
piece of work, which is the beginning of writing programs that are more than one long
script.
