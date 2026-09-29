# Unit 05 exercises

Trace and predict before running. When something surprises you, print the list after
every step until you find where your model went wrong.

---

## Warm-ups

### 5.1 Predict the output

```python
numbers = [10, 20, 30, 40, 50]
```

Write down what each gives.

- `numbers[0]`
- `numbers[-1]`
- `numbers[1:3]`
- `len(numbers)`
- `numbers[2]`
- `20 in numbers`
- `sum(numbers)`

### 5.2 Predict the mutation

Predict what each of these prints, then check.

```python
a = [1, 2, 3]
a.append(4)
print(a)
```

```python
a = [1, 2, 3]
b = a
b.append(4)
print(a)
```

```python
a = [1, 2, 3]
b = a[:]
b.append(4)
print(a)
```

The three together are the point of this exercise. Say out loud what the difference is.

### 5.3 Spot the bug

```python
names = []
names = names.append("Ada")
names = names.append("Grace")
print(len(names))
```

Two problems. One is the `TypeError` you get immediately. The other is harder to see,
about the first line. Fix both.

### 5.4 Finding the error

Each of these fails. Say which error type it gives and why.

```python
names = ["Ada", "Grace"]
print(names[2])
```

```python
names = ["Ada", "Grace"]
print(names.index("Alan"))
```

```python
names = ["Ada", "Grace"]
print(names.remove("Alan"))
```

### 5.5 Sort or reverse

```python
numbers = [5, 2, 9, 1, 7]
numbers.reverse
print(numbers)
```

What does this print? Is it sorted? Explain the difference between `reverse()` and
`sort(reverse=True)`.

---

## Core

### 5.6 Shopping list

Ask the user to enter shopping items one at a time until they type `done`. Then print
the list, the number of items, and the items in alphabetical order.

You will need `while True` with `break` from unit 04.

### 5.7 Grades

Ask how many students there are, then ask for each student's score. Store them in a
list. Then print the highest, the lowest, and the average.

You may use `max()` and `min()` this time. Then, as a second version, work out the highest
without using `max()`, with a loop. Both are worth being able to do, and exercise 5.10
asks for the second one properly.

### 5.8 Remove the duplicates

Given a list with repeated items, build a new list containing each item only once.

```python
items = ["apple", "banana", "apple", "cherry", "banana", "apple"]
```

The answer should be `["apple", "banana", "cherry"]`.

Do it with a loop. For each item, check whether it is already in your new list before
appending it. The order should be the order of first appearance, so do not just use
`sorted()`.

### 5.9 Reverse without reverse

Take a list and produce a reversed copy, without using `reverse()`, `reversed()` or slicing.
Use a loop that goes backwards through the positions.

Hint, `range()` with a negative step, from unit 04.

### 5.10 Biggest, the hard way

Write the biggest-of-a-list logic with a loop, without `max()`. Then answer this question.
What did you initialise the "biggest so far" variable to, and what happens if the whole
list is negative?

Fix it, so that it works for a list of nothing but negative numbers.

### 5.11 Word lengths

Ask for a sentence. Build a list of the lengths of each word, then print the sentence,
the list of lengths, and the longest word.

Example for `the quick brown fox`.

```
Lengths: [3, 5, 5, 3]
Longest word: quick
```

If there is a tie, printing either of the tied words is fine.

### 5.12 Filter and transform

Start with this list.

```python
numbers = [4, -7, 2, 9, -4, 1, 8, -3]
```

Build a new list containing the squares of only the negative numbers.

The answer should be `[49, 16, 9]`.

### 5.13 Insert and delete

Start with a list of five names. Then, in order.

- Add a name to the end
- Add a name at the front
- Remove a name by value
- Remove the last name and say which one it was
- Print the final list and its length

### 5.14 Sort by length

Take a list of words sorted alphabetically and print them sorted by length, shortest
first. Use `sorted()` with the `key` argument.

You have not been taught this, so here is the shape.

```python
sorted(words, key=len)
```

Work out what that does from the result, then explain it in your own words.

---

## Stretch

### 5.15 Report card

Ask for student names and scores, storing the names in one list and the scores in
another, so that `names[i]` and `scores[i]` belong to the same person. Then print a
report, one line per student, sorted by score from highest to lowest.

Example.

```
Grace 95
Ada 88
Alan 72
```

The sorting is the hard part, because sorting one list leaves the other one behind.
Think about how to keep them together. There is a way with a list of lists, and there is
a way with just indices and a bit of arithmetic. Either is fine.

Notice how awkward this is. That awkwardness is a real problem with parallel lists, and
unit 07 exists because of it.

### 5.16 Second biggest

Find the second largest value in a list, without sorting it and without `max()`.

Careful with duplicates. In `[5, 5, 3]` the second largest is `3`, not `5`.

### 5.17 Merge two sorted lists

Given two lists that are already sorted, build a single sorted list containing all their
items, in one pass through each, without using `sort()` or `sorted()`.

```python
a = [1, 4, 7, 10]
b = [2, 3, 8, 11]
```

The answer is `[1, 2, 3, 4, 7, 8, 10, 11]`.

The idea is to keep an index into each list, compare the two current items, take the
smaller one, and move that index forward. This really is a real algorithm that real
software uses, and it is the heart of merge sort.

### 5.18 Run length encoding

Given a string, compress it by replacing runs of the same character with the character
and a count.

```
"aaabbc" becomes "a3b2c1"
```

Then, for the harder half, do the reverse. Given `"a3b2c1"`, produce `"aaabbc"`.

The second direction needs you to take two characters at a time, which you can do with a
loop and an index, or with `range(0, len(text), 2)` from unit 04.

---

## Before next session

Be able to do these without notes.

- Make a list, add to it, remove from it, and get items out by position.
- Loop over a list and build a new list from it.
- Say why `b = a` does not copy a list, and how to copy one properly.
- Explain why `names = names.append("Ada")` breaks.
