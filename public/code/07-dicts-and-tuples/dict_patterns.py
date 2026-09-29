# Unit 07 — dictionary patterns
# Run this with the Run button in your editor.

# ---------------------------------------------------------------
# THE COUNTING PATTERN
# The single most useful dictionary technique there is.

words = ["apple", "banana", "apple", "cherry", "banana", "apple"]

counts = {}

for word in words:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1

print(counts)       # {'apple': 3, 'banana': 2, 'cherry': 1}

# TRACE IT ON PAPER for the first three words.
# counts starts empty
# "apple" not in counts -> counts["apple"] = 1
# "banana" not in counts -> counts["banana"] = 1
# "apple" IS in counts -> counts["apple"] = 2

print()

# The shorter version everyone writes once they are comfortable.

counts = {}

for word in words:
    counts[word] = counts.get(word, 0) + 1

print(counts)

# Read it out loud:
# "set this word's count to whatever it is now, or zero if it is not
# there yet, plus one"

print()

# ---------------------------------------------------------------
# GROUPING
# The same shape, but the values are lists.

words = ["apple", "avocado", "banana", "blueberry", "cherry"]

by_letter = {}

for word in words:
    first = word[0]

    if first not in by_letter:
        by_letter[first] = []       # make sure the container exists first

    by_letter[first].append(word)

print(by_letter)

# The "make sure the container exists, then add to it" pattern shows up
# constantly. Trace it carefully.

print()

# ---------------------------------------------------------------
# A LIST OF DICTIONARIES
# This is what most real data looks like.

students = [
    {"name": "Ada", "score": 88},
    {"name": "Grace", "score": 95},
    {"name": "Alan", "score": 72},
]

for student in students:
    print(f"{student['name']} scored {student['score']}")

# Note the quotes inside the f-string. The inner ones must be different
# from the outer ones, or it is a mess.

print()

# ---------------------------------------------------------------
# A DICTIONARY OF DICTIONARIES
# Same double indexing idea as grid[2][1] from unit 05,
# but with names instead of positions.

grades = {
    "Ada": {"maths": 90, "english": 85},
    "Grace": {"maths": 95, "english": 92},
}

print(grades["Ada"]["maths"])       # 90
print(grades["Grace"]["english"])   # 92

print()

# ---------------------------------------------------------------
# PUTTING IT TOGETHER. Word frequency counter.
# Run this and type a sentence.

text = input("Enter some text: ").lower()
words = text.split()

counts = {}
for word in words:
    word = word.strip(".,!?;:")
    if word:
        counts[word] = counts.get(word, 0) + 1

print(f"\n{len(counts)} different words\n")

# Sorting by count, using only things you already know.
# Note that we put the COUNT first, so the default sort orders by count.

pairs = []
for word, count in counts.items():
    pairs.append([count, word])

pairs.sort(reverse=True)

for count, word in pairs:
    print(f"{word:15} {count}")
