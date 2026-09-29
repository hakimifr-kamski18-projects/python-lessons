# Unit 02 — string methods
# Run this file with:  python3 methods.py

name = "ada lovelace"

print(name.upper())        # ADA LOVELACE
print(name.title())        # Ada Lovelace
print(name.capitalize())   # Ada lovelace
print(name.lower())        # ada lovelace

print()

# ---------------------------------------------------------------
# THE IMPORTANT BIT. Methods give you back a NEW string.
# They do not change the original.

name = "ada lovelace"
name.upper()
print(name)                # still "ada lovelace"  <- nothing happened

# If you want to keep the change, assign it back.
name = name.upper()
print(name)                # ADA LOVELACE

print()

# ---------------------------------------------------------------
# strip() removes spaces from both ends. THE most useful one,
# because users type trailing spaces all the time.

text = "   hello world   "

print(repr(text))              # '   hello world   '
print(repr(text.strip()))      # 'hello world'
print(repr(text.lstrip()))     # 'hello world   '
print(repr(text.rstrip()))     # '   hello world'

# repr() is how you SEE the invisible spaces.

print()

# Without strip(), this kind of comparison fails for a reason you cannot see.
answer = "yes "
print(answer == "yes")             # False! there is a space on the end
print(answer.strip() == "yes")     # True

print()

# ---------------------------------------------------------------
# replace() and count()

sentence = "the cat sat on the mat"
print(sentence.replace("at", "og"))     # the cog sog on the mog
print(sentence.replace("the ", ""))     # cat sat on mat
print(sentence.count("at"))             # 3

print()

# ---------------------------------------------------------------
# split() turns one string into several pieces

words = sentence.split()
print(words)
print(len(words))                       # how many words

data = "10,20,30"
print(data.split(","))

# split() gives back a LIST. The square brackets mean list.
# Lists are unit 05. For now, just know it is a box of several values.

print()

# join() puts them back together. The separator goes BEFORE the dot.

print(" ".join(words))          # the cat sat on the mat
print("-".join(words))          # the-cat-sat-on-the-mat
print(", ".join(words))         # the, cat, sat, on, the, mat

print()

# ---------------------------------------------------------------
# Asking questions about a string

text = "hello world"

print(text.startswith("hello"))     # True
print(text.endswith("world"))       # True
print("world" in text)              # True
print("xyz" in text)                # False
print(text.find("world"))           # 6, the position
print(text.find("xyz"))             # -1, not found

# Prefer "in" when you only want to know whether something is there.
# find() giving -1 is awkward, because -1 is also a valid position.

print()

# ---------------------------------------------------------------
# Chaining, because each method hands back a string for the next one

messy = "  HELLO world  "
print(messy.strip().lower().title())     # Hello World

# Trace it left to right out loud.
# strip() -> "HELLO world"
# lower() -> "hello world"
# title() -> "Hello World"
