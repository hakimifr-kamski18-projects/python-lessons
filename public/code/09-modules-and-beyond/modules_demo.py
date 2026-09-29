# Unit 09 — a tour of the standard library
# Run this with the Run button in your editor.

# ---------------------------------------------------------------
# random

import random

print(random.randint(1, 6))                 # 1 to 6, both included
print(random.choice(["rock", "paper", "scissors"]))
print(random.sample([1, 2, 3, 4, 5], 3))    # three DIFFERENT items

items = [1, 2, 3, 4, 5]
random.shuffle(items)
print(items)                                # shuffled in place

# shuffle() changes the list and gives back None, exactly like sort()
# and append() from unit 05. The command-sounding name rule again.

print()

# ---------------------------------------------------------------
# math

import math

print(math.sqrt(16))        # 4.0
print(math.pi)              # 3.141592653589793
print(math.floor(3.7))      # 3
print(math.ceil(3.2))       # 4
print(math.factorial(5))    # 120

# Watch this one. int truncates toward zero, floor goes DOWN.

print(int(-3.7))            # -3
print(math.floor(-3.7))     # -4
print(math.ceil(-3.7))      # -3

print()

# ---------------------------------------------------------------
# statistics

import statistics

numbers = [4, 7, 2, 9, 4]

print(statistics.mean(numbers))     # 5.2
print(statistics.median(numbers))   # 4
print(statistics.mode(numbers))     # 4

# All of which you wrote by hand back in unit 04.

print()

# ---------------------------------------------------------------
# datetime

import datetime

now = datetime.datetime.now()
print(now.year, now.month, now.day)
print(now.strftime("%Y-%m-%d %H:%M"))

# strftime formats a date as text. The percent codes are fiddly and
# there is no point memorising them. Search for "python strftime"
# when you need one.

print()

# ---------------------------------------------------------------
# The point of the tour.
#
# There are hundreds of modules. Nobody knows them all. The skill is
# knowing that the standard library probably has something for your
# problem, and being able to find it.
#
# Two habits worth more than any list:
# 1. Search "python how to do X" and expect a standard library answer
# 2. Read docs.python.org. It has a search box and it is better than
# most tutorials.

# ---------------------------------------------------------------
# THE THREE WAYS TO IMPORT

# 1. import the module, use it with a dot. USE THIS ONE.
import random
print(random.randint(1, 6))

# 2. import names directly
from random import randint
print(randint(1, 6))

# 3. import with a nickname
import random as rnd
print(rnd.randint(1, 6))

# The dot in form 1 is a feature, not annoying. It tells you where the
# name came from. Six months later, random.randint() is clear and
# randint() could be anything.

# NEVER use "from module import *". It pulls in every name without
# telling you what they are, and it can silently overwrite your own
# variables. You will see it in tutorials. Do not copy it.

# ---------------------------------------------------------------
# Uncomment to see what a missing module looks like.
# import maths
