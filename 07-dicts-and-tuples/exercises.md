# Unit 07 exercises

Remember the question for every one of these. Would a list, a dictionary (a collection
you look things up in by name), or a tuple (like a list that cannot be changed) be the
right shape for this data?

---

## Warm-ups

### 7.1 Predict the output

```python
person = {"name": "Ada", "age": 36, "city": "London"}
```

Write down what each gives.

- `person["name"]`
- `len(person)`
- `"age" in person`
- `"Ada" in person`
- `"Ada" in person.values`
- `person.get("job")`
- `person.get("job", "none")`

### 7.2 Predict the output

```python
counts = {"a": 1, "b": 2}
counts["a"] += 1
counts["c"] = 3
print(counts)
```

### 7.3 Unpacking

```python
pairs = [("Ada", 88), ("Grace", 95)]
for name, score in pairs:
    print(name, score)
```

What does this print, and what does `pairs[0]` look like on its own?

### 7.4 Find the bug

This is meant to add up all the scores in a dictionary. It crashes.

```python
scores = {"Ada": 88, "Grace": 95}
total = 0

for score in scores:
    total += score

print(total)
```

Explain what went wrong, then fix it two different ways.

### 7.5 Find the bug, part two

```python
student = {"name": "Ada"}
student = student["age"] = 36
print(student)
```

---

## Core

### 7.6 Phone book

Store a few names and phone numbers in a dictionary. Ask the user for a name and print
the number, or a message saying it is not there.

Then wrap the lookup in a `while True` loop so they can look up several numbers until
they type `quit`.

### 7.7 Word count

Ask for a sentence. Count how many times each word appears. Print the results one per
line.

So `the cat and the dog` gives this.

```
the 2
cat 1
and 1
dog 1
```

Lowercase the input first so that `The` and `the` count as the same word.

### 7.8 Two lists into a dictionary

Given these two lists, build a dictionary that pairs them up.

```python
names = ["Ada", "Grace", "Alan"]
scores = [88, 95, 72]
```

The answer should be `{"Ada": 88, "Grace": 95, "Alan": 72}`.

You will need the loop with an index from unit 05, `for i in range(len(names))`.

Then think about what this answers about exercise 5.15. You were building two parallel
lists and then fighting to keep them together. What should you have done instead?

### 7.9 Inventory

Start with this dictionary.

```python
inventory = {"apples": 5, "bananas": 3, "cherries": 12}
```

Then do these things, printing the inventory after each step.

- Add 4 to the apples
- Sell all the bananas, so remove the key entirely
- Add a new item, `"dates"` with 7
- Print the total number of items across all the fruit, not the number of kinds

For that last one, you need a loop over `.values` (a value is the thing you get back)
and an accumulator from unit 04.

### 7.10 Letter frequency

Ask for some text. Count how many times each letter appears, ignoring uppercase and
ignoring spaces.

So `hello` gives `h 1, e 1, l 2, o 1`.

Then print the letters in alphabetical order.

### 7.11 Votes

You are counting votes in an election. Ask for names one at a time until the user types
`done`. Print how many votes each candidate got, and who won.

Ties are possible, so decide what happens then and make it do that.

### 7.12 Grade book

Store student marks for several subjects, in this shape.

```python
grades = {
    "Ada": {"maths": 90, "english": 85},
    "Grace": {"maths": 95, "english": 92},
}
```

Let the user add a new subject mark for a student that already exists, and add a whole
new student. Then print every student and their average across subjects.

The average needs a loop inside a loop, or a loop over `.values`.

### 7.13 Sort by value

Take a dictionary of names and scores and print it sorted by score, highest first.

You did the technique in the lesson with the word counter. Build a list of pairs with
the score first, sort it, then print.

Then answer this. Why does putting the score first make the sort work?

---

## Stretch

### 7.14 Group by first letter

Given a list of words, build a dictionary that groups them by their first letter. You
did this in the lesson, so do it without looking.

```python
words = ["apple", "banana", "avocado", "cherry", "blueberry"]
```

Result.

```python
{"a": ["apple", "avocado"], "b": ["banana", "blueberry"], "c": ["cherry"]}
```

Then print each group on its own line, sorted alphabetically.

### 7.15 The most common word

Take a long piece of text. Find the word that appears most often.

Then answer these. What is the second most common? What happens if two words tie?

### 7.16 Invert a dictionary

Given a dictionary, produce a new one where the keys and values are swapped.

```python
original = {"a": 1, "b": 2, "c": 3}
```

Should give `{1: "a", 2: "b", 3: "c"}`.

Then think about this. What happens if two keys have the same value? Try it and explain
the result.

### 7.17 Combined word count

Ask for two pieces of text. Count the words in both, combined into a single dictionary.
So a word that appears 3 times in the first and 2 times in the second should show 5.

Then print only the words that appear in both texts.

### 7.18 Word length histogram

Ask for a sentence. Build a dictionary where the keys are word lengths and the values
are how many words have that length.

So `the quick brown fox` gives `{3: 2, 5: 2}`.

Then print it as a simple bar chart, one `*` per word.

```
3: **
5: **
```

### 7.19 Tuples as keys

A dictionary key does not have to be a string. It can be a tuple.

```python
distances = {
    ("London", "Paris"): 344,
    ("Paris", "Berlin"): 878,
}
```

Build a small version of this, and write a function that takes two city names and
returns the distance, in either order.

So looking up both `("London", "Paris")` and `("Paris", "London")` should work.

The trick is to normalise the pair (put it in a fixed form so two equal things really
are equal) before looking it up, by putting them in a fixed order first.

---

## Before next session

Be able to do these without notes.

- Make a dictionary, add to it, remove from it, and get values out by key.
- Loop over the keys, the values, and the pairs.
- Explain the difference between `d["key"]` and `d.get("key")`.
- Count how many times each thing appears in a list.
- Say when you would use a list rather than a dictionary.
